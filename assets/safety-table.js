/* BRYME Tech — VPN & password safety table (batch 50, 12 Sep 2026).
   CSP-safe IIFE; mounts at #safety-table-calc. Pick a scenario, get the honest
   protection matrix: what a VPN does there, what helps more, the 2FA answer and
   the password move. Desk-firsthand content — evergreen mechanics, no dates to
   rot. General guidance, never a security guarantee. */
(function () {
  "use strict";
  var root = document.getElementById("safety-table-calc");
  if (!root) return;

  var SCENARIOS = {
    wifi: {
      label: "Public Wi-Fi (café, airport, hotel)",
      rows: [
        ["Does a VPN help here?", "<b>Yes — this is its home turf.</b> It encrypts your traffic so the network, its operator and other devices on it can\u2019t read or tamper with what you do."],
        ["What helps even more", "HTTPS does most of the work on modern sites (look for the padlock \u2014 <a href=\"/tech/what-is-ssl-https/\">what it really means</a>); avoid installing anything the network prompts you to."],
        ["2FA", "Yes, everywhere \u2014 it survives even a snooped password."]
      ],
      more: "The full risk list lives in <a href=\"/tech/public-wifi-risks/\">public Wi-Fi risks</a>; the VPN layer is <a href=\"/tech/vpn-what-it-protects/\">what a VPN protects</a>."
    },
    home: {
      label: "Everyday browsing at home",
      rows: [
        ["Does a VPN help here?", "<b>Rarely needed.</b> Your HTTPS traffic is already encrypted end-to-end; a VPN mainly moves who can see connection metadata (your ISP \u2192 the VPN provider)."],
        ["What helps even more", "Router firmware updates, browser privacy settings (<a href=\"/tech/browser-privacy-settings/\">the settings that matter</a>), and a password manager generating unique logins."],
        ["2FA", "Yes on every account that offers it."]
      ],
      more: "If your reason is \u201cI don\u2019t trust my ISP\u201d \u2014 that\u2019s a fair choice, just know what you\u2019re trading: trust shifts, it doesn\u2019t disappear."
    },
    bank: {
      label: "Online banking & payments",
      rows: [
        ["Does a VPN help here?", "<b>Not really.</b> Banks are already HTTPS-encrypted; a VPN can even trigger fraud flags by moving your apparent location. It protects against threats you don\u2019t have here."],
        ["What helps even more", "Bookmarked URLs or your own app \u2014 never links from texts/emails (<a href=\"/tech/how-to-spot-a-suspicious-link/\">spotting suspicious links</a>); a hardware key on accounts that offer it."],
        ["2FA", "Non-negotiable \u2014 prefer an authenticator app or hardware key over SMS."]
      ],
      more: "Your password for the bank should be unique and manager-generated (<a href=\"/tech/best-password-manager-for-you/\">pick a manager</a>)."
    },
    travel: {
      label: "Traveling (borders, roaming, new networks)",
      rows: [
        ["Does a VPN help here?", "<b>Often, yes.</b> Hotel and airport networks are hostile territory, and a trusted home-country exit keeps your accounts behaving normally. Set it up <em>before</em> you fly."],
        ["What helps even more", "Updated devices, printed 2FA backup codes (in case SIMs and apps misbehave), and never charging data off public USB ports."],
        ["2FA", "Yes \u2014 with backup codes stored offline, separately from the device."]
      ],
      more: "Disable auto-join on Wi-Fi before you travel; the network you didn\u2019t choose is the one that profiles you."
    },
    share: {
      label: "Sharing logins (family, partner, flat)",
      rows: [
        ["Does a VPN help here?", "<b>No \u2014 this isn\u2019t a network problem.</b> Sharing passwords by chat is the actual risk: screenshots, backups, ex-contacts."],
        ["What helps even more", "A password manager\u2019s built-in sharing: family plans hand out logins safely, revocably, and without exposure (<a href=\"/tech/password-manager-or-browser/\">manager vs browser</a>)."],
        ["2FA", "Each person keeps their own 2FA; shared accounts use the family plan\u2019s structure, not a shared phone number."]
      ],
      more: "The streaming-password era is over anyway \u2014 the family seat is the legal route and it\u2019s a few dollars a month."
    },
    work: {
      label: "Work accounts from home",
      rows: [
        ["Does a VPN help here?", "<b>Your company\u2019s VPN is theirs to run.</b> A personal VPN doesn\u2019t substitute for it and doesn\u2019t make you compliant \u2014 connect exactly the way your IT team says."],
        ["What helps even more", "Separating work and personal: different browser profile, never reusing work passwords elsewhere, work data never in personal clouds."],
        ["2FA", "Required \u2014 and if your employer offers hardware keys, take them."]
      ],
      more: "The separation habit is the security control here; the tech is secondary."
    }
  };

  var h = '<p class="sf-note">Pick what you\u2019re doing \u2014 get the honest protection picture for exactly that scenario.</p>';
  h += '<div class="sf-chips">';
  for (var k in SCENARIOS) if (SCENARIOS.hasOwnProperty(k)) h += '<button type="button" class="sf-chip" data-k="' + k + '">' + SCENARIOS[k].label + "</button>";
  h += '</div><div id="sf-out" aria-live="polite"></div>';
  h += '<p class="sf-disc">General guidance, never a security guarantee. The depth versions: <a href="/tech/vpn-what-it-protects/">what a VPN protects</a> \u00b7 <a href="/tech/public-wifi-risks/">public Wi-Fi risks</a> \u00b7 <a href="/tech/two-factor-authentication-setup/">2FA done right</a> \u00b7 <a href="/tech/best-password-manager-for-you/">choosing a password manager</a>.</p>';
  root.innerHTML = h;

  var css = document.createElement("style");
  css.textContent =
    ".sf-note{font-size:13px;color:var(--dim);margin:6px 0}" +
    ".sf-chips{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}" +
    ".sf-chip{border:1px solid var(--line-strong);border-radius:999px;padding:8px 14px;font:inherit;font-size:13.5px;background:var(--card);cursor:pointer}" +
    ".sf-chip:hover{border-color:var(--accent)}" +
    "#sf-out table{width:100%;max-width:760px;border-collapse:collapse;margin:10px 0}" +
    "#sf-out td{padding:8px 8px;border-bottom:1px solid var(--line);font-size:14px;vertical-align:top}" +
    "#sf-out td:first-child{font-weight:700;width:34%}" +
    ".sf-more{font-size:13px;color:var(--dim)}";
  document.head.appendChild(css);

  root.addEventListener("click", function (e) {
    var b = e.target;
    if (!b.matches || !b.matches(".sf-chip")) return;
    var sc = SCENARIOS[b.getAttribute("data-k")];
    var t = "<table>";
    for (var i = 0; i < sc.rows.length; i++) t += "<tr><td>" + sc.rows[i][0] + "</td><td>" + sc.rows[i][1] + "</td></tr>";
    t += "</table><p class=\"sf-more\">" + sc.more + "</p>";
    document.getElementById("sf-out").innerHTML = t;
  });
})();
