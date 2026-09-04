"use strict";
/*
 * BRYME Google Indexing API integration (architecture).
 *
 * PURPOSE
 *   Notify Google when a *qualifying* JobPosting page is published / updated /
 *   removed. This is a crawler notification mechanism only — it is NOT a
 *   general-purpose indexer for ordinary articles and it does NOT guarantee
 *   indexing. Google decides what to crawl and index.
 *
 * WHEN TO USE (and when NOT to)
 *   - Use only for pages that legitimately qualify (e.g. a real, currently
 *     open JobPosting page that carries valid JobPosting structured data).
 *   - Do NOT use for evergreen guides, hubs, or articles.
 *   - Do NOT use to notify removal of a page that is not genuinely gone.
 *
 * CONFIG (via env, see render.yaml)
 *   SITE_URL                        canonical origin (e.g. https://bryme.example)
 *   INDEXING_API_TOKEN              shared secret guarding the notify endpoint
 *   GOOGLE_INDEXING_CREDENTIALS     path to a service-account JSON key (optional)
 *
 * When no service account is configured the module runs in DRY-RUN mode: it
 * records what would have been sent and returns a clear message, without making
 * a network call. Nothing is sent to Google until a JSON key is provided and a
 * service account is authorised for the Indexing API.
 */
const https = require("https");
const fs = require("fs");
const path = require("path");

const SITE_URL = (process.env.SITE_URL || "https://bryme.onrender.com").replace(/\/+$/, "");
const CREDENTIALS = process.env.GOOGLE_INDEXING_CREDENTIALS || "";
const LOG_PATH = path.join(__dirname, "indexing-log.jsonl");
// Avoid re-submitting the same url+type within this window (in ms).
const DEDUP_WINDOW_MS = Number(process.env.INDEXING_DEDUP_MS || 6 * 60 * 60 * 1000);
const PUBLISHER_TOKEN = process.env.INDEXING_API_TOKEN || "";

const INDEXING_SCOPE = "https://www.googleapis.com/auth/indexing";

function enabled() {
  return Boolean(CREDENTIALS && fs.existsSync(CREDENTIALS));
}

function log(entry) {
  try {
    // Always record a numeric timestamp so the dedup window can be computed.
    const row = { timestamp: Date.now(), at: new Date().toISOString(), ...entry };
    fs.appendFileSync(LOG_PATH, JSON.stringify(row) + "\n", "utf8");
  } catch (_) {
    /* logging must never break the request */
  }
}

function loadRecent() {
  try {
    if (!fs.existsSync(LOG_PATH)) return new Map();
    const rows = fs
      .readFileSync(LOG_PATH, "utf8")
      .split(/\r?\n/)
      .filter(Boolean)
      .map((line) => {
        try { return JSON.parse(line); } catch (_) { return null; }
      })
      .filter(Boolean);
    const map = new Map();
    for (const row of rows) {
      const key = row.type + "|" + row.url;
      map.set(key, row.timestamp);
    }
    return map;
  } catch (_) {
    return new Map();
  }
}

function recent(key) {
  return loadRecent().get(key);
}

// Minimal JWT + OAuth2 token exchange for the Indexing API using a service key.
// Kept dependency-free. Only used when a credentials JSON is present.
function getAccessToken() {
  return new Promise((resolve, reject) => {
    let creds;
    try {
      creds = JSON.parse(fs.readFileSync(CREDENTIALS, "utf8"));
    } catch (err) {
      return reject(new Error("Could not read INDEXING credentials: " + err.message));
    }
    const now = Math.floor(Date.now() / 1000);
    const header = { alg: "RS256", typ: "JWT" };
    const claim = {
      iss: creds.client_email,
      scope: INDEXING_SCOPE,
      aud: creds.token_uri || "https://oauth2.googleapis.com/token",
      iat: now,
      exp: now + 3600,
    };
    const b64 = (obj) => Buffer.from(JSON.stringify(obj)).toString("base64url");
    const signingInput = b64(header) + "." + b64(claim);
    let sig;
    try {
      const crypto = require("crypto");
      sig = crypto.createSign("RSA-SHA256").update(signingInput).sign(
        creds.private_key,
        "base64"
      );
    } catch (err) {
      return reject(new Error("Could not sign JWT: " + err.message));
    }
    const assertion = signingInput + "." + sig.replace(/=+$/, "");
    const body = JSON.stringify({
      grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer",
      assertion,
    });
    const req = https.request(
      creds.token_uri || "https://oauth2.googleapis.com/token",
      { method: "POST", headers: { "content-type": "application/json", "content-length": Buffer.byteLength(body) } },
      (res) => {
        let data = "";
        res.on("data", (c) => (data += c));
        res.on("end", () => {
          try {
            const parsed = JSON.parse(data);
            if (parsed.access_token) resolve(parsed.access_token);
            else reject(new Error("OAuth error: " + (parsed.error_description || data)));
          } catch (err) {
            reject(new Error("Bad OAuth response: " + err.message));
          }
        });
      }
    );
    req.on("error", reject);
    req.write(body);
    req.end();
  });
}

function sendIndexingNotification(url, type) {
  const typePath = type === "deleted" ? "delete" : "urlNotifications:publish";
  return getAccessToken().then(
    (token) =>
      new Promise((resolve, reject) => {
        const body = JSON.stringify({ url: SITE_URL + url });
        const req = https.request(
          "https://indexing.googleapis.com/v3/urlNotifications/" + typePath,
          {
            method: "POST",
            headers: {
              authorization: "Bearer " + token,
              "content-type": "application/json",
              "content-length": Buffer.byteLength(body),
            },
          },
          (res) => {
            let data = "";
            res.on("data", (c) => (data += c));
            res.on("end", () => resolve({ status: res.statusCode, body: data }));
          }
        );
        req.on("error", reject);
        req.write(body);
        req.end();
      })
  );
}

/**
 * Notify Google about a qualifying page.
 * @param {string} url  site-relative path, e.g. "/jobs/example-123/"
 * @param {"published"|"updated"|"deleted"} type
 */
async function notify(url, type) {
  const cleanUrl = "/" + String(url).replace(/^\/+/, "").replace(/\/+$/, "") + "/";
  const valid = ["published", "updated", "deleted"];
  if (!valid.includes(type)) return { ok: false, error: "invalid type" };
  if (!cleanUrl.startsWith("/jobs/")) {
    // The Indexing API is reserved for eligible JobPosting pages in BRYME's design.
    return { ok: false, error: "non-qualifying route (job pages only)" };
  }
  const key = type + "|" + cleanUrl;
  const prior = recent(key);
  if (prior && Date.now() - prior < DEDUP_WINDOW_MS) {
    log({ at: new Date().toISOString(), type, url: cleanUrl, status: "skipped-duplicate", note: "within dedup window" });
    return { ok: true, deduplicated: true, url: SITE_URL + cleanUrl, type };
  }
  if (!enabled()) {
    log({ at: new Date().toISOString(), type, url: cleanUrl, status: "dry-run", note: "no GOOGLE_INDEXING_CREDENTIALS configured" });
    return { ok: true, dryRun: true, url: SITE_URL + cleanUrl, type, note: "Indexing API not configured; nothing sent to Google." };
  }
  try {
    const result = await sendIndexingNotification(cleanUrl, type);
    log({ at: new Date().toISOString(), type, url: cleanUrl, status: String(result.status), body: result.body });
    return { ok: result.status >= 200 && result.status < 300, status: result.status, url: SITE_URL + cleanUrl, type };
  } catch (err) {
    log({ at: new Date().toISOString(), type, url: cleanUrl, status: "error", error: err.message });
    return { ok: false, error: err.message };
  }
}

module.exports = { notify, enabled, PUBLISHER_TOKEN, SITE_URL };
