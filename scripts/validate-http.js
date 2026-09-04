#!/usr/bin/env node
/* Local HTTP contract: routing, containment, status codes and security headers. */
"use strict";
process.env.WATCHDOG = "off";
process.env.TELEGRAM_ENABLED = "0";
const { server } = require("../server/server.js");

const failures = [];
function check(ok, message) { if (!ok) failures.push(message); }
async function get(base, pathname, options = {}) {
  return fetch(base + pathname, { redirect: "manual", ...options });
}

server.listen(0, "127.0.0.1", async () => {
  const address = server.address();
  const base = `http://127.0.0.1:${address.port}`;
  try {
    let r = await get(base, "/");
    check(r.status === 200, `/ returned ${r.status}`);
    check((r.headers.get("content-type") || "").startsWith("text/html"), "/ is not HTML");
    for (const h of ["content-security-policy", "referrer-policy", "permissions-policy", "strict-transport-security", "x-content-type-options"]) {
      check(Boolean(r.headers.get(h)), `/ missing ${h}`);
    }
    check((await r.text()).includes("Direct sources. Human checks. Nigeria context."), "/ does not contain focused homepage copy");

    for (const [p, status, location] of [
      ["/jobs", 308, "/jobs/"],
      ["/jobs/index.html", 308, "/jobs/"],
      ["/movie/breaking-bad/", 301, "/series/breaking-bad/"],
    ]) {
      r = await get(base, p);
      check(r.status === status, `${p} returned ${r.status}, expected ${status}`);
      check(r.headers.get("location") === location, `${p} location is ${r.headers.get("location")}, expected ${location}`);
    }

    r = await get(base, "/channels/netflix/");
    check(r.status === 410, `retired channel returned ${r.status}`);
    check((await r.text()).includes("Collection retired"), "410 response lacks retirement explanation");

    for (const p of [
      "/does-not-exist", "/server/server.js", "/scripts/build-focus-site.py",
      "/reports/site-inventory.csv", "/package.json", "/content/jobs.json",
      "/.git/HEAD", "/assets/../../server/server.js"
    ]) {
      r = await get(base, p);
      check(r.status === 404, `${p} should be 404, got ${r.status}`);
      const body = await r.text();
      check(/noindex/i.test(body), `${p} 404 body lacks noindex`);
    }

    for (const p of ["/favicon.ico", "/google2ec8f794263d784f.html", "/content/competitions.json", "/assets/bryme-v2.css"]) {
      r = await get(base, p);
      check(r.status === 200, `${p} returned ${r.status}`);
      await r.arrayBuffer();
    }

    r = await get(base, "/api/sports/competitions");
    check(r.status === 200, `sports API returned ${r.status}`);
    const data = await r.json();
    check(Array.isArray(data.competitions) && data.competitions.length === 6, "sports API shape is invalid");

    r = await get(base, "/jobs/", { method: "POST", body: "x" });
    check(r.status === 405, `POST to static route returned ${r.status}`);
    check((r.headers.get("allow") || "").includes("GET"), "405 response lacks Allow header");

    r = await get(base, "/jobs/", { method: "HEAD" });
    check(r.status === 200, `HEAD /jobs/ returned ${r.status}`);
    check((await r.text()) === "", "HEAD response unexpectedly has a body");
  } catch (error) {
    failures.push(error && error.stack || String(error));
  } finally {
    server.close(() => {
      if (failures.length) {
        console.error(`FAIL (${failures.length})`);
        failures.forEach(x => console.error("  - " + x));
        process.exitCode = 1;
      } else {
        console.log(JSON.stringify({ ok: true, checks: "routing, 404/410, allowlist, headers, API, HEAD" }, null, 2));
      }
    });
  }
});
