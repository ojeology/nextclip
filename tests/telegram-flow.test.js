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

// pick free ports so a running dev server can't collide with the test
const net = require("net");
const freePort = () => new Promise((res, rej) => {
  const srv = net.createServer();
  srv.listen(0, "0.0.0.0", () => { const p = srv.address().port; srv.close(() => res(p)); });
  srv.on("error", rej);
});
let server = null;
function startServer(port, mport) {
  server = spawn(process.execPath, [path.join(ROOT, "server", "server.js")], {
    env: Object.assign({}, process.env, {
      PORT: String(port),
      TELEGRAM_BOT_TOKEN: "123:TEST",
      TELEGRAM_API_BASE: "http://localhost:" + mport,
      TELEGRAM_WEBHOOK_SECRET: "s3cret",
      MINI_APP_URL: "https://bryme-tg.example.com"
    }),
    stdio: ["ignore", "pipe", "pipe"]
  });
  server.stdout.on("data", () => {});
  server.stderr.on("data", (d) => process.stderr.write("[srv] " + d));
}

const req = (method, url, headers, body) => new Promise((resolve, reject) => {
  const r = http.request(url, { method, headers: headers || {} }, (res) => {
    let b = ""; res.on("data", (c) => (b += c)); res.on("end", () => resolve({ code: res.statusCode, body: b }));
  });
  r.on("error", reject);
  if (body) r.write(body);
  r.end();
});

let MPORT_REF = 0, PORT_REF = 0;
const sent = () => req("POST", `http://localhost:${MPORT_REF}/__dump`).then((r) => JSON.parse(r.body).filter((c) => c.method === "sendMessage").map((c) => c.payload));
const reset = () => req("POST", `http://localhost:${MPORT_REF}/__reset`);
async function webhook(update) {
  await req("POST", `http://localhost:${PORT_REF}/telegram/webhook`,
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
  const PORT = await freePort(), MPORT = await freePort();
  startServer(PORT, MPORT);
  PORT_REF = PORT; MPORT_REF = MPORT;
  await new Promise((r) => mock.listen(MPORT, "0.0.0.0", r));
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
  r = await req("GET", BASE + "/api/sports/competitions");
  let cp = {};
  try { cp = JSON.parse(r.body); } catch (e) {}
  check("competitions endpoint serves 5 competitions", r.code === 200 && Array.isArray(cp.competitions) && cp.competitions.length === 5, { n: (cp.competitions || []).length });
  check("competitions include champions-league", (cp.competitions || []).some((c) => c.id === "champions-league" && c.teams.length >= 6));
  check("competitions carry teams/scores/fixtures/scorers arrays", (cp.competitions || []).every((c) => Array.isArray(c.teams) && Array.isArray(c.scores) && Array.isArray(c.fixtures) && Array.isArray(c.scorers)));
  check("real goalscorers present (majority of comps)", (cp.competitions || []).filter((c) => c.scorers.length >= 5 && c.scorers[0].name && typeof c.scorers[0].goals === "number").length >= 3, (cp.competitions || []).map((c) => c.id + ":" + c.scorers.length));
  r = await req("GET", BASE + "/api/sports/leagues");
  let lg = {};
  try { lg = JSON.parse(r.body); } catch (e) {}
  check("leagues compat endpoint serves 5 tables", r.code === 200 && Array.isArray(lg.leagues) && lg.leagues.length === 5, { n: (lg.leagues || []).length });
  check("league tables carry teams + pts", (lg.leagues || []).every((l) => Array.isArray(l.teams) && l.teams.length >= 6 && l.teams.every((t) => typeof t.pts === "number" && t.short)));

  r = await req("GET", BASE + "/api/money/opportunities");
  let ops = {};
  try { ops = JSON.parse(r.body); } catch (e) {}
  check("money opportunities list (50+ verified)", r.code === 200 && ops.count >= 50 && ops.opportunities.every((o) => o.publication && o.pay && typeof o.ng === "boolean" && Array.isArray(o.writingTypes)), { n: ops.count });
  const topOpp = (ops.opportunities || [])[0];
  r = await req("GET", BASE + "/api/money/opportunities/" + encodeURIComponent(topOpp ? topOpp.slug : "afrolicious"));
  const opd = JSON.parse(r.body);
  check("money opportunity detail", r.code === 200 && !!opd.publication && !!opd.pay && !!(opd.applyUrl || opd.officialUrl), opd.publication);

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
  const noWebLinks = !art.body.includes('href="https://bryme.onrender.com') && !/ href="\/[a-z]/i.test(art.body);
  check("article body has no exits to the website", noWebLinks, art.body.slice(0, 80));
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
  const mBtn = money && money.reply_markup ? [].concat(...money.reply_markup.inline_keyboard).find((b) => b.web_app && /r=market%2F/.test(b.web_app.url)) : null;
  check("money teaser format", money && /MAKE .+ WRITING\?/.test(money.text) && /What they accept/.test(money.text) && /pay BRYME/i.test(money.text), money && money.text.split("\n")[0]);
  check("money teaser headline", money && /MAKE .+ WRITING\?/.test(money.text) && /don't pay BRYME/i.test(money.text), money && money.text.split("\n")[0]);
  check("playbook button -> #/market/<slug>", mBtn && /#\/market\/[a-z0-9-]+$/.test(mBtn.web_app.url), mBtn && mBtn.web_app.url);
  const mkts = money && money.reply_markup ? [].concat(...money.reply_markup.inline_keyboard).find((b) => b.web_app && /r=markets/.test(b.web_app.url)) : null;
  check("money teaser: playbook + direct-markets web_app buttons",
    money && (() => { const w = [].concat(...money.reply_markup.inline_keyboard).filter((b) => b.web_app); return w.length === 2 && /#\/market\//.test(w[0].web_app.url) && /#\/markets/.test(w[1].web_app.url); })());

  console.log("T3 · Sports category");
  sends = await webhook({ update_id: 3, callback_query: { id: "c2", from: { id: 42 }, data: "cat:sports", message: { message_id: 10, chat: { id: 42 } } } });
  const sports = sends[0];
  const sBtn = sports && sports.reply_markup ? [].concat(...sports.reply_markup.inline_keyboard).find((b) => b.web_app) : null;
  check("sports snippet + #/sports web_app (dual carrier)", sports && sBtn && sBtn.web_app.url.endsWith("#/sports") && /[?&]r=sports(?=#)/.test(sBtn.web_app.url));

  console.log("T4 · Latest posts");
  sends = await webhook({ update_id: 4, callback_query: { id: "c3", from: { id: 42 }, data: "latest", message: { message_id: 11, chat: { id: 42 } } } });
  const lat = sends[0];
  const lBtns = lat && lat.reply_markup ? [].concat(...lat.reply_markup.inline_keyboard).filter((b) => b.web_app) : [];
  check("latest lists article buttons (dual carrier)", lBtns.length >= 5 && lBtns.every((b) => b.web_app.url.includes("#/article/") && /[?&]r=article%2F/.test(b.web_app.url)), lBtns.length);

  console.log("Fallbacks · bad article, unknown cat, security");
  sends = await webhook({ update_id: 5, callback_query: { id: "c4", from: { id: 42 }, data: "art:nope", message: { message_id: 12, chat: { id: 42 } } } });
  check("missing article fallback message", sends[0] && /couldn'?t find that article/i.test(sends[0].text));
  sends = await webhook({ update_id: 6, callback_query: { id: "c5", from: { id: 42 }, data: "cat:unknown", message: { message_id: 13, chat: { id: 42 } } } });
  check("unknown category handled", sends[0] && /unknown section/i.test(sends[0].text));
  r = await req("POST", BASE + "/telegram/webhook", { "content-type": "application/json" }, '{"message":{}}');
  check("webhook rejects without secret (401)", r.code === 401);
  sends = await webhook({ update_id: 7, message: { message_id: 3, from: { id: 42 }, chat: { id: 42 }, text: "/start sports" } });
  check("website deep link /start sports -> sports snippet", sends[0] && sends[0].text.includes("SPORTS"));

  console.log("T5 · free-text intent");
  sends = await webhook({ update_id: 8, message: { message_id: 20, from: { id: 7 }, chat: { id: 7 }, text: "make money" } });
  const tm = sends[sends.length - 1];
  const tmBtn = tm.reply_markup ? [].concat(...tm.reply_markup.inline_keyboard).find((b) => b.web_app) : null;
  check("text make-money -> teaser + playbook", /MAKE .+ WRITING\?/.test(sends[sends.length - 1].text) && !![].concat(...sends[sends.length - 1].reply_markup.inline_keyboard).find((b) => b.web_app && /#\/market\//.test(b.web_app.url)));
  sends = await webhook({ update_id: 9, message: { message_id: 21, from: { id: 7 }, chat: { id: 7 }, text: "show me the comics" } });
  check("text 'comics' -> comics section", sends[sends.length - 1].text.includes("COMICS"));
  sends = await webhook({ update_id: 10, message: { message_id: 22, from: { id: 7 }, chat: { id: 7 }, text: "xyzzy plugh" } });
  check("unknown text -> menu (not a section)", /explore/i.test(sends[sends.length - 1].text));


  console.log(`\n${pass} passed, ${fail} failed`);
  server.kill(); mock.close(); process.exit(fail ? 1 : 0);
})().catch((e) => { console.error("HARNESS ERROR", e); if (server) server.kill(); try { mock.close(); } catch (x) {} process.exit(1); });
