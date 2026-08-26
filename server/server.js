/* BRYME backend — one zero-dependency Node service powering:
 *   • the content API  (bot + Mini App read the same JSON index)
 *   • the Telegram bot webhook
 *   • static hosting for the Telegram Mini App
 *
 * Run:          PORT=8787 node server/server.js
 * Environment:  TELEGRAM_BOT_TOKEN, TELEGRAM_WEBHOOK_SECRET,
 *               MINI_APP_URL (public https URL of this service — BotFather needs it),
 *               TELEGRAM_API_BASE (optional, for tests/mocks)
 *
 * Content source of truth: content/posts-index.json + content/posts-bodies.json
 * (built by scripts/build-posts-index.js from the same files the website uses).
 * The files are watched by mtime — publishing + rebuilding propagates here
 * without a restart.
 */
"use strict";

const http = require("http");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const MINIAPP_DIR = path.join(ROOT, "miniapp");
const PORT = Number(process.env.PORT || 8787);
const TOKEN = process.env.TELEGRAM_BOT_TOKEN || "";
const SECRET = process.env.TELEGRAM_WEBHOOK_SECRET || "";
const API_BASE = process.env.TELEGRAM_API_BASE || "https://api.telegram.org";
const MINI_APP_URL = process.env.MINI_APP_URL || "";

const { createBot } = require("./bot");

/* ---------- content cache (mtime-refreshed) ---------- */
const INDEX_PATH = path.join(ROOT, "content", "posts-index.json");
const BODIES_PATH = path.join(ROOT, "content", "posts-bodies.json");
let cache = { posts: [], bodies: {}, mtime: 0, bodiesMtime: 0 };

function loadContent() {
  try {
    const m = fs.statSync(INDEX_PATH).mtimeMs;
    const bm = fs.statSync(BODIES_PATH).mtimeMs;
    if (m !== cache.mtime) {
      const idx = JSON.parse(fs.readFileSync(INDEX_PATH, "utf8"));
      cache = { posts: idx.posts || [], bodies: cache.bodies, mtime: m, bodiesMtime: cache.bodiesMtime, builtAt: idx.builtAt };
    }
    if (bm !== cache.bodiesMtime) {
      cache.bodies = JSON.parse(fs.readFileSync(BODIES_PATH, "utf8"));
      cache.bodiesMtime = bm;
    }
  } catch (e) {
    /* keep last good cache */
  }
  return cache;
}

/* ---------- telegram sender ---------- */
function telegram(method, payload) {
  if (!TOKEN) return Promise.reject(new Error("TELEGRAM_BOT_TOKEN not set"));
  return fetch(API_BASE + "/bot" + TOKEN + "/" + method, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(payload)
  }).then((r) => r.json());
}

function miniBase(req) {
  if (MINI_APP_URL) return MINI_APP_URL.replace(/\/+$/, "");
  const host = (req.headers["x-forwarded-host"] || req.headers.host || "localhost:" + PORT).split(",")[0].trim();
  const proto = req.headers["x-forwarded-proto"] || (String(host).startsWith("localhost") || String(host).startsWith("127.") ? "http" : "https");
  return proto + "://" + host;
}

function botFor(req) {
  return createBot({
    getPosts: () => loadContent().posts,
    miniAppBase: miniBase(req),
    send: telegram,
    answerCallback: (id) => telegram("answerCallbackQuery", { callback_query_id: id })
  });
}

/* ---------- helpers ---------- */
const MIME = {
  ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8", ".json": "application/json; charset=utf-8",
  ".png": "image/png", ".jpg": "image/jpeg", ".svg": "image/svg+xml", ".ico": "image/x-icon",
  ".webmanifest": "application/manifest+json"
};
function json(res, code, obj) {
  const body = JSON.stringify(obj);
  res.writeHead(code, {
    "content-type": "application/json; charset=utf-8",
    "access-control-allow-origin": "*",
    "cache-control": "no-cache"
  });
  res.end(body);
}
function readBody(req, limit) {
  return new Promise((resolve, reject) => {
    let size = 0; const chunks = [];
    req.on("data", (c) => { size += c.length; if (size > (limit || 1e6)) { reject(new Error("too large")); req.destroy(); } else chunks.push(c); });
    req.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
    req.on("error", reject);
  });
}
function sendFile(res, abs) {
  fs.readFile(abs, (err, buf) => {
    if (err) { res.writeHead(404, { "content-type": "text/plain" }); res.end("not found"); return; }
    res.writeHead(200, { "content-type": MIME[path.extname(abs)] || "application/octet-stream", "cache-control": "no-cache" });
    res.end(buf);
  });
}

function publicPost(p, body) {
  return {
    title: p.title, slug: p.slug, category: p.category, categoryLabel: p.categoryLabel,
    excerpt: p.excerpt, image: p.image, publishedAt: p.publishedAt, author: p.author,
    readingTime: p.readingTime, url: p.url, miniAppRoute: "#/article/" + p.slug,
    status: "published", hasBody: Boolean(body)
  };
}

/* ---------- request router ---------- */
const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, "http://x");
  const p = url.pathname.replace(/\/+$/, "") || "/";

  try {
    /* health */
    if (p === "/healthz") return json(res, 200, { ok: true, posts: loadContent().posts.length });

    /* ---- API ---- */
    if (p === "/api/posts/latest") {
      const limit = Math.min(Number(url.searchParams.get("limit") || 8), 20);
      const { posts } = loadContent();
      return json(res, 200, { count: Math.min(limit, posts.length), posts: posts.slice(0, limit).map((x) => publicPost(x)) });
    }
    if (p.startsWith("/api/posts/category/")) {
      const cat = decodeURIComponent(p.split("/")[4] || "");
      const limit = Math.min(Number(url.searchParams.get("limit") || 12), 30);
      const { posts } = loadContent();
      const list = posts.filter((x) => x.category === cat).slice(0, limit);
      return json(res, 200, { category: cat, count: list.length, posts: list.map((x) => publicPost(x)) });
    }
    if (p.startsWith("/api/posts/") && p.split("/").length === 4) {
      const slug = decodeURIComponent(p.split("/")[3]);
      const { posts, bodies } = loadContent();
      const post = posts.find((x) => x.slug === slug);
      if (!post) return json(res, 404, { error: "not_found", message: "We couldn't find that article.", fallback: { miniAppRoute: "#/home", label: "Latest posts" } });
      return json(res, 200, Object.assign(publicPost(post, bodies[slug]), { body: bodies[slug] || "" }));
    }
    if (p === "/api/categories") {
      const { posts } = loadContent();
      const counts = {};
      posts.forEach((x) => (counts[x.category] = (counts[x.category] || 0) + 1));
      return json(res, 200, { categories: Object.entries(counts).map(([k, v]) => ({ key: k, count: v })) });
    }

    /* ---- Telegram webhook ---- */
    if (p === "/telegram/webhook") {
      if (req.method !== "POST") return json(res, 405, { error: "method_not_allowed" });
      if (SECRET && req.headers["x-telegram-bot-api-secret-token"] !== SECRET) {
        return json(res, 401, { error: "unauthorized" });
      }
      let update;
      try { update = JSON.parse(await readBody(req)); } catch (e) { return json(res, 400, { error: "bad_json" }); }
      json(res, 200, { ok: true }); // ack immediately; reply goes via Bot API
      try { await botFor(req).handleUpdate(update); } catch (e) { /* logged, never leaked */ }
      return;
    }

    /* ---- Mini App static hosting (/ and /miniapp/*) ---- */
    let file = null;
    if (p === "/" || p === "/index.html" || p.startsWith("/#/")) file = "index.html";
    else if (p.startsWith("/miniapp/")) file = p.slice("/miniapp/".length);
    else if (p === "/app.js" || p === "/app.css" || p === "/telegram-web-app.js") file = path.basename(p);
    if (file) {
      const abs = path.normalize(path.join(MINIAPP_DIR, file));
      if (abs.startsWith(MINIAPP_DIR)) return sendFile(res, abs);
    }

    res.writeHead(404, { "content-type": "text/plain" });
    res.end("not found");
  } catch (e) {
    json(res, 500, { error: "internal", message: "Something went wrong. Try again." });
  }
});

if (!module.parent) {
  server.listen(PORT, "0.0.0.0", () => {
    console.log("BRYME server on :" + PORT + " | posts:", loadContent().posts.length,
      "| bot:", TOKEN ? "token set" : "TOKEN MISSING (webhook will 500 politely)",
      "| mini app:", MINI_APP_URL || "derived from request host");
  });
}
module.exports = { server, loadContent, telegram };
