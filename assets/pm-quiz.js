/* BRYME Tech — password-manager chooser quiz (batch 49, 12 Sep 2026).
   CSP-safe IIFE; mounts at #pm-quiz-calc. Three questions, tag-scored verdict
   over the 2026 field (prices checked 12 Sep 2026: itechguides, guptadeepak,
   usecarly guides). Directional and dated — pricing changes; your threat model
   decides. General guidance, never a security guarantee. */
(function () {
  "use strict";
  var root = document.getElementById("pm-quiz-calc");
  if (!root) return;

  /* [name, price line, tags] */
  var PM = [
    ["Apple Passwords", "free (built into Apple devices)", ["apple", "free", "simple"]],
    ["Bitwarden", "free unlimited; Premium $10\u201319.80/yr; Families \u2248$40\u201348/yr", ["free", "cheap", "family", "control", "mixed"]],
    ["KeePassXC", "free \u2014 fully local, you manage sync", ["free", "control"]],
    ["Proton Pass", "free; Pass Plus \u2248$24\u201336/yr", ["cheap", "privacy", "mixed"]],
    ["1Password", "no free tier; from \u2248$48/yr", ["premium", "simple", "family", "mixed"]],
    ["Dashlane", "no free tier; \u2248$60/yr; 10 family seats", ["premium", "family"]],
    ["NordPass", "free (1 device); from \u2248$1.4\u20133/mo", ["cheap", "simple", "mixed"]]
  ];

  var QS = [
    ["pm-q1", "Your devices are\u2026", [["apple", "All Apple (iPhone/Mac/iPad)"], ["mixed", "A mix of platforms"], ["any", "Anything reliable"]]],
    ["pm-q2", "Your budget is\u2026", [["free", "Free only"], ["cheap", "Up to a few dollars a month"], ["premium", "Worth it if it's the best"]]],
    ["pm-q3", "You want\u2026", [["simple", "Set-and-forget simplicity"], ["family", "Sharing with family"], ["control", "Maximum control (local/offline vaults)"], ["privacy", "Privacy-first ecosystem"]]]
  ];

  var h = '<p class="pq-note">Three questions \u2014 one honest match. Prices checked 12 Sep 2026.</p><div id="pq-body"></div><div id="pq-out" aria-live="polite"></div>';
  h += '<p class="pq-disc">General guidance, not a security guarantee \u2014 whichever manager you pick, the habits matter more than the brand: unique passwords, 2FA everywhere (<a href="/tech/two-factor-authentication-setup/">2FA done right</a>), and an exported backup.</p>';
  root.innerHTML = h;

  var body = document.getElementById("pq-body");
  function render() {
    var answers = {};
    for (var q = 0; q < QS.length; q++) {
      var val = (window.__pqAnswers || {})[QS[q][0]];
      if (val) answers[QS[q][0]] = val;
    }
    var h2 = "";
    for (var i = 0; i < QS.length; i++) {
      h2 += '<p class="pq-q">' + QS[i][1] + "</p><div class=\"pq-opts\">";
      for (var j = 0; j < QS[i][2].length; j++) {
        var tag = QS[i][2][j][0], sel = answers[QS[i][0]] === tag;
        h2 += '<button type="button" class="pq-opt' + (sel ? " pq-sel" : "") + '" data-q="' + QS[i][0] + '" data-v="' + tag + '">' + QS[i][2][j][1] + "</button>";
      }
      h2 += "</div>";
    }
    body.innerHTML = h2;
  }
  window.__pqAnswers = {};
  render();

  root.addEventListener("click", function (e) {
    var b = e.target;
    if (!b.matches || !b.matches(".pq-opt")) return;
    window.__pqAnswers[b.getAttribute("data-q")] = b.getAttribute("data-v");
    render();
    verdict();
  });

  function verdict() {
    var a = window.__pqAnswers;
    if (!a["pm-q1"] || !a["pm-q2"] || !a["pm-q3"]) return;
    var tags = [a["pm-q1"], a["pm-q2"], a["pm-q3"]];
    if (a["pm-q2"] === "free" && a["pm-q3"] === "privacy") tags.push("privacy");
    var scored = [];
    for (var i = 0; i < PM.length; i++) {
      var hits = 0;
      for (var j = 0; j < tags.length; j++) if (PM[i][2].indexOf(tags[j]) > -1) hits++;
      scored.push([PM[i][0], hits, PM[i][1]]);
    }
    scored.sort(function (x, y) { return y[1] - x[1]; });
    var out = document.getElementById("pq-out");
    if (scored[0][1] === 0) { out.innerHTML = '<p class="pq-note">No clean match for that exact combination \u2014 loosen one answer.</p>'; return; }
    var runners = "";
    for (var k = 1; k < scored.length && k < 3; k++) if (scored[k][1] === scored[0][1]) runners += "<li><b>" + scored[k][0] + "</b> \u2014 " + scored[k][2] + "</li>";
    out.innerHTML = '<div class="pq-verdict"><p class="pq-match">Your match: <b>' + scored[0][0] + "</b></p><p class=\"pq-price\">" + scored[0][1] + "</p>" +
      (runners ? '<p class="pq-note">Equally good for your answers:</p><ul>' + runners + "</ul>" : "") +
      '<p class="pq-note">Then do these once: export a backup, turn on 2FA on the vault itself, and let it replace your reused passwords gradually.</p></div>';
  }

  var css = document.createElement("style");
  css.textContent =
    ".pq-note{font-size:13px;color:var(--dim);margin:6px 0}" +
    ".pq-q{font-size:16px;margin:14px 0 6px}" +
    ".pq-opts{display:flex;flex-wrap:wrap;gap:8px}" +
    ".pq-opt{border:1px solid var(--line-strong);border-radius:999px;padding:8px 14px;font:inherit;font-size:14px;background:var(--card);cursor:pointer}" +
    ".pq-opt:hover{border-color:var(--accent)}" +
    ".pq-sel{border-color:var(--accent);background:var(--sheet);font-weight:700}" +
    ".pq-verdict{border:1px solid var(--line-strong);border-radius:12px;padding:14px 16px;background:var(--sheet);margin-top:12px;max-width:640px}" +
    ".pq-match{font-size:19px;margin:0 0 4px}" +
    ".pq-price{font-size:14px;color:var(--dim);margin:0 0 8px}";
  document.head.appendChild(css);
})();
