#!/usr/bin/env node
/* Deep-link boot test — runs the REAL miniapp/app.js in a stubbed browser
 * and asserts the destination resolves correctly for every carrier:
 * hash (primary), ?r= (bot fallback), ?section=, tgWebAppStartParam.
 * This guards the "everything opens Home" fix. */
"use strict";
const fs = require("fs"), vm = require("vm"), path = require("path");
const src = fs.readFileSync(path.join(__dirname, "..", "miniapp", "app.js"), "utf8");
function boot(url) {
  const u = new URL(url);
  let replaced = null;
  const stubEl = () => ({ addEventListener() {}, appendChild() {}, setAttribute() {}, classList: { toggle() {}, add() {}, remove() {} }, style: {}, querySelector: () => null, querySelectorAll: () => [] });
  const sandbox = {
    console, URL, URLSearchParams, fetch: () => Promise.resolve({ ok: true, json: () => Promise.resolve({}) }),
    location: { hash: u.hash, search: u.search, replace: (h) => { replaced = h; } },
    document: { getElementById: stubEl, createElement: stubEl, querySelectorAll: () => [], addEventListener() {}, readyState: "complete" },
    window: {}, setTimeout, clearInterval, setInterval
  };
  sandbox.window = sandbox; sandbox.self = sandbox;
  try { vm.createContext(sandbox); vm.runInContext(src, sandbox); } catch (e) { /* stubbed DOM ends execution after boot */ }
  return { hash: u.hash, replaced };
}
const CASES = [
  ["bot money btn (full URL)", "https://bryme.onrender.com/miniapp?api=https%3A%2F%2Fbryme-backend.onrender.com&r=money#/money", "#/money"],
  ["fragment dropped (regression bug)", "https://bryme.onrender.com/miniapp?api=https%3A%2F%2Fbryme-backend.onrender.com&r=money", "#/money"],
  ["article, fragment dropped", "https://bryme.onrender.com/miniapp?api=X&r=article%2Fwriting-opportunities", "#/article/writing-opportunities"],
  ["competition", "https://bryme.onrender.com/miniapp?api=X&r=comp%2Fla-liga", "#/comp/la-liga"],
  ["menu button (home)", "https://bryme.onrender.com/miniapp/?api=X#/home", "#/home"],
  ["startapp param (Telegram-appended)", "https://bryme.onrender.com/miniapp/?api=X&tgWebAppStartParam=sports", "#/sports"],
  ["?section= fallback", "https://bryme.onrender.com/miniapp?section=comics", "#/comics"],
  ["no destination -> home", "https://bryme.onrender.com/miniapp?api=X", "#/home"]
];
let pass = 0;
for (const [name, url, want] of CASES) {
  const r = boot(url);
  const finalHash = r.hash && /^#\/.+/.test(r.hash) ? r.hash : (r.replaced || "#/home");
  const ok = finalHash === want;
  console.log((ok ? "  ✔ " : "  ✘ ") + name + " -> " + finalHash);
  if (ok) pass++;
}
console.log(pass + "/" + CASES.length + " deep-link boot cases pass");
process.exit(pass === CASES.length ? 0 : 1);
