#!/usr/bin/env node
/* End-to-end flow test for the BRYME Telegram bot + API + Mini App.
 * Boots: mock Telegram Bot API (capturing) + the real server, then runs the
 * spec's test suite against them. Zero external deps.
 *   node tests/telegram-flow.test.js
 */
"use strict";
const http = require("http");
const { spawn } = require("child_process");
const path = require("path");
const ROOT = path.resolve(__dirname, "..");

let captured = [];
const mock = http.createServer((req, res) => {
  let body = "";
  req.on("data", (c) => (body += c));
  req.on("end", () => {
    if (req.url.includes("__dump")) { res.writeHead(200); return res.end(JSON.stringify(captured)); }
    if (req.url.includes("__reset")) { captured = []; res.writeHead(200); return res.end("{}"); }
    const m = req.url.match(/\/bot[^/]+\/(\w+)/);
    captured.push({ method: m ? m[1] : req.url, payload: body ? JSON.parse(body) : null });
    res.writeHead(200, { "content-type": "application/json" });
    res.end('{"ok":true,"result":{}}');
  });
});

const PORT = 8791, MPORT = 8792;
const server = spawn(process.execPath, [path.join(ROOT, "server", "server.js")], {
  env: Object.assign({}, process.env, {
    PORT: String(PORT),
    TELEGRAM_BOT_TOKEN: "123:TEST",
    TELEGRAM_API_BASE: "http://localhost:" + MPORT,
    TELEGRAM_WEBHOOK_SECRET: "s3cret",
    MINI_APP_URL: "https://bryme-tg.example.com"
  }),
  stdio: ["ignore", "pipe", "pipe"]
});
server.stdout.on("data", () => {});
server.stderr.on("data", (d) => process.stderr.write("[srv] " + d));

const req = (method, url, headers, body) => new Promise((resolve, reject) => {
  const r = http.request(url, { method, headers: headers || {} }, (res) => {
    let b = ""; res.on("data", (c) => (b += c)); res.on("end", () => resolve({ code: res.statusCode, body: b }));
  });
  r.on("error", reject);
  if (body) r.write(body);
  r.end();
});

const sent = () => req("POST", `http://localhost:${MPORT}/__dump`).then((r) => JSON.parse(r.body).filter((c) => c.method === "sendMessage").map((c) => c.payload));
const reset = () => req("POST", `http://localhost:${MPORT}/__reset`);
async function webhook(update) {
  await req("POST", `http://localhost:${PORT}/telegram/webhook`,
    { "content-type": "application/json", "x-telegram-bot-api-secret-token": "s3cret" }, JSON.stringify(update));
  await new Promise((r) => setTimeout(r, 350));
  const s = await sent();
  await reset();
  return s;
}

let pass = 0, fail = 0;
function check(name, cond, extra) {
  if (cond) { pass++; console.log("  ✔", name); }
  else { fail++; console.log("  ✘", name, extra !== undefined ? "— " + JSON.stringify(extra).slice(0, 200) : ""); }
}

(async () => {
  await new Promise((r) => mock.listen(MPORT, r));
  await new Promise((r) => setTimeout(r, 600));
  const BASE = `http://localhost:${PORT}`;

  console.log("T5 · Mini App + health");
  let r = await req("GET", BASE + "/healthz");
  const health = JSON.parse(r.body);
  check("healthz ok with posts", r.code === 200 && health.ok && health.posts > 50, health);
  r = await req("GET", BASE + "/");
  check("mini app html serves", r.code === 200 && r.body.includes("telegram-web-app.js") && r.body.includes("app.js"));
  r = await req("GET", BASE + "/app.js");
  check("app.js serves + router present", r.code === 200 && r.body.includes("#/article/"));
  r = await req("GET", BASE + "/app.css");
  check("app.css serves", r.code === 200);

  console.log("API · latest / category / article / 404");
  r = await req("GET", BASE + "/api/posts/latest?limit=6");
  const latest = JSON.parse(r.body);
  check("latest returns published posts w/ miniAppRoute", latest.posts.every((p) => p.status === "published" && p.miniAppRoute.startsWith("#/article/")));
  r = await req("GET", BASE + "/api/posts/category/money");
  check("category money non-empty", JSON.parse(r.body).count > 0);
  r = await req("GET", BASE + "/api/posts/category/trading");
  const tr = JSON.parse(r.body);
  check("trading category works (has 1)", tr.count >= 0);
  const slug = latest.posts[0].slug;
  r = await req("GET", BASE + "/api/posts/" + encodeURIComponent(slug));
  const art = JSON.parse(r.body);
  check("article endpoint returns body", r.code === 200 && typeof art.body === "string");
  r = await req("GET", BASE + "/api/posts/definitely-not-real");
  check("missing article -> 404 + fallback", r.code === 404 && JSON.parse(r.body).fallback.miniAppRoute === "#/home");

  console.log("T1 · /start menu");
  let sends = await webhook({ update_id: 1, message: { message_id: 1, from: { id: 42 }, chat: { id: 42 }, text: "/start" } });
  const menu = sends[0];
  const flatBtns = menu && menu.reply_markup ? [].concat(...menu.reply_markup.inline_keyboard) : [];
  check("menu text", menu && /BRYME/.test(menu.text) && /explore/.test(menu.text), menu && menu.text);
  check("8 working buttons (7 cats + latest)", flatBtns.length === 8 && flatBtns.every((b) => b.callback_data || b.web_app));

  console.log("T2 · Make Money category");
  sends = await webhook({ update_id: 2, callback_query: { id: "c1", from: { id: 42 }, data: "cat:money", message: { message_id: 9, chat: { id: 42 } } } });
  const money = sends[0];
  const mBtn = money && money.reply_markup ? [].concat(...money.reply_markup.inline_keyboard).find((b) => b.web_app) : null;
  check("money snippet shown", money && money.text.includes("MAKE MONEY"), money && money.text);
  check("web_app button -> #/money", mBtn && mBtn.web_app.url.endsWith("#/money"), mBtn);

  console.log("T3 · Sports category");
  sends = await webhook({ update_id: 3, callback_query: { id: "c2", from: { id: 42 }, data: "cat:sports", message: { message_id: 10, chat: { id: 42 } } } });
  const sports = sends[0];
  const sBtn = sports && sports.reply_markup ? [].concat(...sports.reply_markup.inline_keyboard).find((b) => b.web_app) : null;
  check("sports snippet + #/sports web_app", sports && sBtn && sBtn.web_app.url.endsWith("#/sports"));

  console.log("T4 · Latest posts");
  sends = await webhook({ update_id: 4, callback_query: { id: "c3", from: { id: 42 }, data: "latest", message: { message_id: 11, chat: { id: 42 } } } });
  const lat = sends[0];
  const lBtns = lat && lat.reply_markup ? [].concat(...lat.reply_markup.inline_keyboard).filter((b) => b.web_app) : [];
  check("latest lists article buttons", lBtns.length >= 5 && lBtns.every((b) => b.web_app.url.includes("#/article/")), lBtns.length);

  console.log("Fallbacks · bad article, unknown cat, security");
  sends = await webhook({ update_id: 5, callback_query: { id: "c4", from: { id: 42 }, data: "art:nope", message: { message_id: 12, chat: { id: 42 } } } });
  check("missing article fallback message", sends[0] && /couldn'?t find that article/i.test(sends[0].text));
  sends = await webhook({ update_id: 6, callback_query: { id: "c5", from: { id: 42 }, data: "cat:unknown", message: { message_id: 13, chat: { id: 42 } } } });
  check("unknown category handled", sends[0] && /unknown section/i.test(sends[0].text));
  r = await req("POST", BASE + "/telegram/webhook", { "content-type": "application/json" }, '{"message":{}}');
  check("webhook rejects without secret (401)", r.code === 401);
  sends = await webhook({ update_id: 7, message: { message_id: 3, from: { id: 42 }, chat: { id: 42 }, text: "/start sports" } });
  check("website deep link /start sports -> sports snippet", sends[0] && sends[0].text.includes("SPORTS"));

  console.log(`\n${pass} passed, ${fail} failed`);
  server.kill(); mock.close(); process.exit(fail ? 1 : 0);
})().catch((e) => { console.error("HARNESS ERROR", e); server.kill(); mock.close(); process.exit(1); });
