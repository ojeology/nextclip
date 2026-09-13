/* BRYME Tech — security checklist scorecard (batch 52, 13 Sep 2026).
   CSP-safe IIFE; mounts at #security-checklist-calc. 16 checks in 5 groups,
   weighted (critical=3, high=2, good=1). Live score, honest verdict, and a
   "your next three" panel listing the highest-weight unchecked items with
   links into the desk's guides. Session-only (no storage). General guidance,
   never a security guarantee. */
(function () {
  "use strict";
  var root = document.getElementById("security-checklist-calc");
  if (!root) return;

  var GROUPS = [
    ["accounts", "Accounts & logins"],
    ["devices", "Devices"],
    ["browsing", "Browsing habits"],
    ["money", "Money & scams"],
    ["backups", "Backups"]
  ];
  var ITEMS = [
    { c: "accounts", t: "2FA on your main email", w: 3, u: "/tech/two-factor-authentication-setup/", why: "your email is the reset key to everything else you own" },
    { c: "accounts", t: "2FA on banking and money apps", w: 3, u: "/tech/two-factor-authentication-setup/", why: "it survives a stolen password" },
    { c: "accounts", t: "A password manager generating unique logins", w: 3, u: "/tech/best-password-manager-for-you/", why: "memory alone means reuse, and reuse means one leak becomes ten" },
    { c: "accounts", t: "No password reused across accounts", w: 3, u: "/tech/password-manager-or-browser/", why: "the single most common domino in account takeovers" },
    { c: "accounts", t: "2FA backup codes stored offline", w: 2, u: "/tech/how-to-reset-forgotten-passwords/", why: "a lost phone should lock you out for minutes, not forever" },
    { c: "devices", t: "Automatic OS and browser updates on", w: 3, why: "updates are shipped fixes for holes attackers already know" },
    { c: "devices", t: "Lock screen with PIN or biometrics", w: 3, why: "a lost device is only as safe as its lock" },
    { c: "devices", t: "Find-my-device enabled", w: 2, why: "you can locate, lock and wipe remotely" },
    { c: "browsing", t: "You check links before clicking them", w: 2, u: "/tech/how-to-spot-a-suspicious-link/", why: "you are the anti-phishing tool; no software replaces the pause" },
    { c: "browsing", t: "Browser privacy settings tuned", w: 1, u: "/tech/browser-privacy-settings/", why: "fewer trackers, fewer fingerprinting surfaces" },
    { c: "browsing", t: "You know what a VPN can and can't do", w: 2, u: "/tech/vpn-and-password-safety-table/", why: "right tool for hostile networks, optional at home" },
    { c: "money", t: "Banking only via bookmarks or the official app", w: 3, u: "/tech/how-to-spot-a-suspicious-link/", why: "removes the entire class of fake-link bank theft" },
    { c: "money", t: "You never move money on an unexpected call or text", w: 3, why: "every \u201cbank security team\u201d call is a scam until proven otherwise \u2014 hang up, call back on the official number" },
    { c: "backups", t: "Automatic backup of irreplaceable files", w: 2, u: "/tech/cloud-storage-mistakes/", why: "ransomware and lost laptops are backups\u2019 whole job" },
    { c: "backups", t: "One backup reachable without the internet", w: 1, why: "an offline copy survives account lockouts and cloud mistakes" },
    { c: "backups", t: "Cloud sharing settings reviewed", w: 1, u: "/tech/cloud-storage-mistakes/", why: "\u201canyone with the link\u201d folders leak quietly for years" }
  ];

  function checkedMap() {
    var m = {};
    var boxes = root.querySelectorAll("input[type=checkbox]");
    for (var i = 0; i < boxes.length; i++) m[boxes[i].getAttribute("data-i")] = boxes[i].checked;
    return m;
  }

  function score() {
    var total = 0, got = 0, m = checkedMap();
    for (var i = 0; i < ITEMS.length; i++) {
      total += ITEMS[i].w;
      if (m[i]) got += ITEMS[i].w;
    }
    return { pct: Math.round((got / total) * 100), missing: m };
  }

  function nextThree(m) {
    var left = [];
    for (var i = 0; i < ITEMS.length; i++) if (!m[i]) left.push(ITEMS[i]);
    left.sort(function (a, b) { return b.w - a.w; });
    return left.slice(0, 3);
  }

  function verdict(pct) {
    if (pct === 100) return "Hardened. There is nothing left on this list \u2014 keep the habits, and re-check after any new device, app or life change.";
    if (pct >= 80) return "Solidly protected. What\u2019s left is finishing work, not exposure \u2014 close it out anyway.";
    if (pct >= 50) return "A real foundation, but the gaps below are the ones attackers actually use. Work the list top-down.";
    if (pct >= 20) return "Exposed. Don\u2019t panic \u2014 the next three moves below remove most of the realistic risk in under an hour.";
    return "Wide open. One evening of work changes this completely \u2014 start with the first three below.";
  }

  function render() {
    var m = checkedMap();
    var s = score();
    var bar = document.getElementById("sc-bar");
    var num = document.getElementById("sc-num");
    var say = document.getElementById("sc-verdict");
    bar.style.width = s.pct + "%";
    num.textContent = s.pct + "%";
    say.textContent = verdict(s.pct);
    var nx = nextThree(s.missing);
    var h = nx.length ? "<p class='sc-nx-title'>Your next three moves</p><ol>" : "<p class='sc-nx-title'>Nothing left on the list.</p>";
    for (var i = 0; i < nx.length; i++) {
      h += "<li><b>" + nx[i].t + "</b>" + (nx[i].u ? " \u2014 <a href='" + nx[i].u + "'>how</a>" : "") +
           "<span class='sc-why'>" + nx[i].why + "</span></li>";
    }
    if (nx.length) h += "</ol>";
    h += "<button type='button' class='sc-reset' id='sc-reset'>Reset</button>";
    document.getElementById("sc-next").innerHTML = h;
  }

  var h = "<div class='sc-scorewrap'><div class='sc-scorehead'><span class='sc-num' id='sc-num'>0%</span><span class='sc-scale'>secure right now</span></div><div class='sc-track'><div class='sc-bar' id='sc-bar'></div></div><p class='sc-verdict' id='sc-verdict'>Tick what\u2019s already true for you.</p></div>";
  for (var g = 0; g < GROUPS.length; g++) {
    h += "<p class='sc-group'>" + GROUPS[g][1] + "</p>";
    for (var i = 0; i < ITEMS.length; i++) {
      if (ITEMS[i].c !== GROUPS[g][0]) continue;
      h += "<label class='sc-item'><input type='checkbox' data-i='" + i + "'><span><b>" + ITEMS[i].t + "</b>" +
           (ITEMS[i].u ? " <a class='sc-mini' href='" + ITEMS[i].u + "'>guide</a>" : "") + "</span></label>";
    }
  }
  h += "<div id='sc-next'></div>";
  h += "<p class='sc-disc'>Weighted scorecard (critical \u00d73, high \u00d72, good \u00d71), session-only \u2014 nothing you tick leaves this page. General guidance, never a security guarantee.</p>";
  root.innerHTML = h;

  root.addEventListener("change", render);
  root.addEventListener("click", function (e) {
    if (e.target && e.target.id === "sc-reset") {
      var boxes = root.querySelectorAll("input[type=checkbox]");
      for (var i = 0; i < boxes.length; i++) boxes[i].checked = false;
      render();
    }
  });
  render();

  var css = document.createElement("style");
  css.textContent =
    ".sc-scorewrap{border:1px solid var(--line-strong);border-radius:12px;background:var(--sheet);padding:14px 16px;max-width:640px;margin:12px 0}" +
    ".sc-scorehead{display:flex;align-items:baseline;gap:10px}" +
    ".sc-num{font-size:34px;font-weight:800}" +
    ".sc-scale{font-size:13px;color:var(--dim)}" +
    ".sc-track{height:8px;border-radius:999px;background:var(--line);margin:10px 0 8px;overflow:hidden}" +
    ".sc-bar{height:100%;width:0;border-radius:999px;background:var(--accent);transition:width .3s}" +
    ".sc-verdict{font-size:14px;margin:6px 0 0}" +
    ".sc-group{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin:18px 0 6px}" +
    ".sc-item{display:flex;gap:10px;align-items:baseline;padding:7px 0;border-bottom:1px solid var(--line);max-width:640px;font-size:14.5px;cursor:pointer}" +
    ".sc-item input{width:17px;height:17px;flex:none}" +
    ".sc-mini{font-size:12px}" +
    ".sc-nx-title{font-weight:700;margin:14px 0 4px}" +
    "#sc-next ol{margin:0 0 10px 20px;max-width:640px}" +
    "#sc-next li{font-size:14px;margin:7px 0}" +
    ".sc-why{display:block;font-size:12.5px;color:var(--dim)}" +
    ".sc-reset{border:1px solid var(--line-strong);background:var(--card);border-radius:8px;padding:6px 14px;font:inherit;font-size:13px;cursor:pointer}" +
    ".sc-disc{font-size:12px;color:var(--dim);margin-top:12px}";
  document.head.appendChild(css);
})();
