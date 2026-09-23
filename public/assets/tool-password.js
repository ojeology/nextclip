/* BRYME password strength checker — client-side only, CSP-safe (no inline JS).
   Heuristic estimator: length, character classes, dictionary + leet check,
   sequences, repeats, keyboard runs, dates. Nothing is transmitted. */
(function () {
  "use strict";
  var COMMON = ("123456 password 123456789 12345678 12345 qwerty 1234567 111111 1234567890 " +
    "123123 abc123 1234 password1 iloveyou 000000 qwerty123 zaq12wsx dragon monkey " +
    "letmein football welcome admin login abc12345 qwertyuiop master sunshine trustno1 " +
    "hello freedom whatever qazwsx password123 654321 superman batman starwars " +
    "michael jennifer jordan harley ranger hunter buster soccer hockey killer george " +
    "charlie andrew thomas robert access love pepper ginger summer winter london " +
    "chelsea arsenal liverpool united rangers celtic charlie shadow mongoose asdfgh " +
    "tigger purple cheese computer internet samsung google apple ninja").split(" ");
  var ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "1234567890"];
  var LEET = { "4": "a", "@": "a", "8": "b", "3": "e", "1": "l", "!": "i", "0": "o", "5": "s", "$": "s", "7": "t", "+": "t" };

  var pw = document.getElementById("tt-pw");
  var show = document.getElementById("tt-show");
  var calc = document.getElementById("tt-calc");
  var out = document.getElementById("tt-out");
  var msg = document.getElementById("tt-msg");

  function leetDecode(s) {
    return s.toLowerCase().split("").map(function (c) { return LEET[c] || c; }).join("");
  }

  function hmsName(sec) {
    if (sec < 1) return "instantly";
    var u = [[60, "seconds"], [60, "minutes"], [24, "hours"], [365, "days"], [100, "years"]];
    var v = sec, n = "";
    for (var i = 0; i < u.length; i++) { n = u[i][1]; if (v < u[i][0]) break; v = v / u[i][0]; }
    if (n === "years" && v > 1000) return "millions of years";
    return "about " + (v < 10 ? v.toFixed(1) : Math.round(v).toLocaleString()) + " " + n;
  }

  function go() {
    msg.textContent = ""; out.textContent = "";
    var s = pw.value || "";
    if (!s.length) { msg.textContent = "Type a password to check (try a few of your real ones - nothing leaves this page)."; return; }
    var notes = [];
    var pool = 0;
    if (/[a-z]/.test(s)) pool += 26;
    if (/[A-Z]/.test(s)) pool += 26;
    if (/[0-9]/.test(s)) pool += 10;
    if (/[^a-zA-Z0-9]/.test(s)) pool += 33;
    var bits = s.length * (Math.log(pool || 1) / Math.LN2);
    var low = s.toLowerCase();
    var lowLeet = leetDecode(s);
    var isCommon = COMMON.indexOf(low) !== -1 || COMMON.indexOf(lowLeet) !== -1;
    var i, hit;
    for (i = 0; i < COMMON.length; i++) {
      if (low.indexOf(COMMON[i]) !== -1 || lowLeet.indexOf(COMMON[i]) !== -1) { hit = COMMON[i]; break; }
    }
    if (isCommon) { bits = Math.min(bits, 10); notes.push("this is one of the most-used passwords in the world - it is in every attacker's list"); }
    else if (hit) { bits -= 25; notes.push("contains the common word '" + hit + "' - dictionary attacks try those first (swapped letters like @ for a do not help)"); }
    if (/(.)\1\1/.test(s)) { bits -= 8; notes.push("three or more of the same character in a row add very little strength"); }
    for (i = 0; i < ROWS.length; i++) {
      for (var j = 0; j + 4 <= ROWS[i].length; j++) {
        if (low.indexOf(ROWS[i].substring(j, j + 4)) !== -1) { bits -= 10; notes.push("keyboard runs like '" + ROWS[i].substring(j, j + 4) + "' are tried early"); j = 999; break; }
      }
    }
    if (/(012|123|234|345|456|567|678|789|abc|bcd|cde|def)/i.test(s)) { bits -= 8; notes.push("sequences (abc, 123) are cheap to guess"); }
    if (/(19|20)\d{2}/.test(s)) { bits -= 5; notes.push("years are the first thing tried around any name or word"); }
    if (/^\d+$/.test(s)) { bits -= 10; notes.push("digits only - just 10 symbols per position"); }
    if (s.length < 8) bits = Math.min(bits, 20);
    bits = Math.max(bits, 1);
    var verdict = bits < 28 ? "Very weak" : bits < 40 ? "Weak" : bits < 60 ? "Fair" : bits < 80 ? "Strong" : "Very strong";
    var offline = Math.pow(2, bits) / 2 / 1e11;
    var online = Math.pow(2, bits) / 2 / 100;
    var lines = [verdict + "  (about " + Math.round(bits) + " bits of entropy)", "",
      "If a site's password database leaks, a serious offline cracking rig",
      "would typically try every combination like yours in " + hmsName(offline) + ".",
      "Against a website's login form (throttled), far longer: " + hmsName(online) + "."];
    if (notes.length) { lines.push("", "Why not stronger:"); notes.forEach(function (n) { lines.push(" - " + n); }); }
    lines.push("", "What moves the needle:");
    if (s.length < 16) lines.push(" - Length beats cleverness: 4-5 random words (a passphrase) outclass symbol soup");
    if (!/[A-Z]/.test(s) || !/[0-9]/.test(s) || !/[^a-zA-Z0-9]/.test(s)) lines.push(" - mixing character types raises the search space (worth less than length, but free)");
    lines.push(" - unique per site: one reused password turned against you opens every door");
    lines.push(" - a password manager remembers all of this for you");
    out.textContent = lines.join("\n");
  }

  if (show && pw) {
    show.addEventListener("change", function () { pw.type = show.checked ? "text" : "password"; });
  }
  if (calc) { calc.addEventListener("click", go); }
})();
