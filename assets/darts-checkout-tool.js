/* BRYME Sport — darts checkout trainer (2026-09-29).
   Deterministic arithmetic only: exhaustive search of legal three-dart
   checkouts (the final dart must be a double: D1-D20 or DB, the bull
   counting as double 25). On-device only — no storage, no network,
   no betting content. The page shows the working; this file runs it.
   Result-card share object: bryme.checkout.v1 (canvas card + Web Share). */
(function () {
  "use strict";

  var TARGETS = [];
  for (var n = 1; n <= 20; n++) {
    TARGETS.push(["S" + n, n]);
    TARGETS.push(["D" + n, 2 * n]);
    TARGETS.push(["T" + n, 3 * n]);
  }
  TARGETS.push(["SB", 25]);
  TARGETS.push(["DB", 50]);
  var DOUBLES = TARGETS.filter(function (t) { return t[0][0] === "D" && t[0] !== "DB"; })
    .concat([["DB", 50]]);
  /* finish-double preference: D20 first (playable with two darts in hand),
     then the bull, then the even doubles players actually practise. */
  var FINISH_PREF = ["D20", "DB", "D16", "D8", "D10", "D18", "D12", "D4", "D2", "D6", "D14"];

  function val(t) {
    for (var i = 0; i < TARGETS.length; i++) if (TARGETS[i][0] === t) return TARGETS[i][1];
    return 0;
  }
  function finRank(t) {
    var i = FINISH_PREF.indexOf(t);
    return i === -1 ? 99 + val(t) / 1000 : i;
  }

  function findRoutes(score) {
    var out = [];
    var i, j, k;
    for (i = 0; i < DOUBLES.length; i++) {
      if (DOUBLES[i][1] === score) out.push([DOUBLES[i][0]]);
    }
    if (out.length) return out;
    for (i = 0; i < TARGETS.length; i++) {
      for (j = 0; j < DOUBLES.length; j++) {
        if (TARGETS[i][1] + DOUBLES[j][1] === score) out.push([TARGETS[i][0], DOUBLES[j][0]]);
      }
    }
    if (out.length) return out;
    for (i = 0; i < TARGETS.length; i++) {
      for (j = 0; j < TARGETS.length; j++) {
        for (k = 0; k < DOUBLES.length; k++) {
          if (TARGETS[i][1] + TARGETS[j][1] + DOUBLES[k][1] === score) {
            out.push([TARGETS[i][0], TARGETS[j][0], DOUBLES[k][0]]);
          }
        }
      }
    }
    return out;
  }

  function preferredRoute(routes) {
    /* fewest darts (routes are already grouped that way), then best finish
       double per FINISH_PREF, then the biggest first dart, then the biggest
       second dart. The page states this rule so the choice is checkable. */
    return routes.slice().sort(function (a, b) {
      var fa = a[a.length - 1], fb = b[b.length - 1];
      if (finRank(fa) !== finRank(fb)) return finRank(fa) - finRank(fb);
      var pa = a.length > 1 ? val(a[0]) : 0, pb = b.length > 1 ? val(b[0]) : 0;
      if (pa !== pb) return pb - pa;
      var qa = a.length > 2 ? val(a[1]) : 0, qb = b.length > 2 ? val(b[1]) : 0;
      return qb - qa;
    })[0];
  }

  var el = document.getElementById("darts-checkout-trainer");
  if (!el) return;

  el.innerHTML =
    '<div class="pr-card">' +
    '<div class="pr-flds">' +
    '<label>Score left (2-170)<input id="dc-score" type="number" min="1" max="180" step="1" value="121" inputmode="numeric"></label>' +
    '<label>&nbsp;<button id="dc-go" style="padding:12px 18px;border:0;border-radius:8px;background:var(--accent);color:#fff;font-weight:700;font-size:16px;cursor:pointer">Show the checkout</button></label>' +
    "</div>" +
    '<div class="pr-out" id="dc-out" aria-live="polite"></div>' +
    '<p class="pr-privacy">Runs entirely in your browser &mdash; nothing is stored or sent. Game arithmetic, never a bet.</p>' +
    "</div>";

  var out = document.getElementById("dc-out");

  function workingLine(route) {
    var parts = route.map(function (t) {
      return t + " = " + val(t);
    });
    var sum = route.reduce(function (a, t) { return a + val(t); }, 0);
    return parts.join(" + ") + " = " + sum;
  }

  function renderCard(score, route, nRoutes, nDarts) {
    /* bryme.checkout.v1 — the shareable result card, drawn on canvas. */
    var W = 1000, H = 1250;
    var c = document.createElement("canvas");
    c.width = W; c.height = H;
    var g = c.getContext("2d");
    g.fillStyle = "#f6f2e8"; g.fillRect(0, 0, W, H);
    g.strokeStyle = "#8f6a1e"; g.lineWidth = 3; g.strokeRect(40, 40, W - 80, H - 80);
    g.fillStyle = "#8f6a1e";
    g.font = "bold 34px Georgia, serif";
    g.fillText("THE BRYME \u00B7 DARTS CHECKOUT TRAINER", 90, 140);
    g.strokeStyle = "#8f6a1e"; g.lineWidth = 2;
    g.beginPath(); g.moveTo(90, 185); g.lineTo(W - 90, 185); g.stroke();
    g.fillStyle = "#1d2531";
    g.font = "bold 120px Georgia, serif";
    g.fillText(String(score) + "  in " + nDarts, 90, 360);
    g.font = "bold 64px Georgia, serif";
    var y = 500;
    route.forEach(function (t, i) {
      g.fillStyle = i === route.length - 1 ? "#e4572e" : "#1d2531";
      g.fillText((i + 1) + ".  " + t + "   (" + val(t) + ")", 90, y);
      y += 110;
    });
    g.fillStyle = "#5c6675";
    g.font = "32px Georgia, serif";
    g.fillText(workingLine(route), 90, y + 30);
    g.fillText(nRoutes + " legal route" + (nRoutes === 1 ? "" : "s") + " exist \u2014 this one is ours.", 90, y + 90);
    g.strokeStyle = "#8f6a1e"; g.beginPath(); g.moveTo(90, H - 220); g.lineTo(W - 90, H - 220); g.stroke();
    g.fillStyle = "#e4572e"; g.font = "bold 44px Georgia, serif";
    g.fillText("thebryme.com", 90, H - 150);
    g.fillStyle = "#1d2531"; g.font = "30px Georgia, serif";
    g.fillText("Every route computed. The working shown. Never a bet.", 90, H - 100);
    return c;
  }

  function go() {
    var raw = parseInt(document.getElementById("dc-score").value, 10);
    if (isNaN(raw) || raw < 1 || raw > 180) {
      out.innerHTML = '<h3>Enter a score between 1 and 180.</h3>';
      return;
    }
    var routes = findRoutes(raw);
    if (!routes.length) {
      out.innerHTML =
        "<h3>" + raw + " has no three-dart checkout.</h3>" +
        "<p>The arithmetic is final: the last dart must land on a double, and no combination of three darts reaches " +
        raw + " that way. The scores below 171 with no checkout are 1, 159, 162, 163, 165, 166, 168, 169 &mdash; " +
        "everything from 2 to 170 except those can be finished. (Folklore sometimes adds 157 and 158 to the bogey list; " +
        "the table says otherwise: 157 = T19, T20, D20 and 158 = T20, T20, D19.)</p>" +
        '<p class="pr-warn">Leave a number you can finish instead.</p>';
      return;
    }
    var route = preferredRoute(routes);
    var alts = routes.filter(function (r) { return r.join(" ") !== route.join(" "); }).slice(0, 3);
    var html =
      "<h3>" + raw + " in " + route.length + " dart" + (route.length === 1 ? "" : "s") + "</h3>" +
      "<p><b>Our route:</b> " + route.join(", ") + "</p>" +
      "<p><b>The working:</b> " + workingLine(route) + "</p>" +
      "<p><b>How we pick it:</b> fewest darts first, then the finish double players practise most (D20, " +
      "then the bull, then the even doubles), then the biggest first and second darts. " +
      routes.length + " legal route" + (routes.length === 1 ? " exists" : "s exist") +
      " &mdash; the televised route may differ, and any legal route scores the same.</p>";
    if (alts.length) {
      html += "<p><b>Also legal:</b> " + alts.map(function (r) { return r.join("-"); }).join(" &middot; ") + "</p>";
    }
    html +=
      '<p style="margin-top:14px"><button id="dc-share" style="padding:10px 16px;border:1px solid var(--line-strong);' +
      'border-radius:8px;background:var(--paper);font-weight:600;cursor:pointer">Share this checkout</button> ' +
      '<button id="dc-card" style="padding:10px 16px;border:1px solid var(--line-strong);border-radius:8px;' +
      'background:var(--paper);font-weight:600;cursor:pointer">Download result card</button> ' +
      '<span id="dc-msg" style="margin-left:8px;color:var(--muted)"></span></p>';
    out.innerHTML = html;

    var card = {
      type: "bryme.checkout.v1",
      score: raw,
      darts: route.length,
      route: route,
      working: workingLine(route),
      routes_total: routes.length,
      url: "https://thebryme.com/sports/darts-checkout-trainer/"
    };
    var text =
      "Checkout " + raw + " in " + route.length + ": " + route.join(" \u2192 ") +
      " (" + card.working + ") \u2014 thebryme.com/sports/darts-checkout-trainer/";

    var msg = document.getElementById("dc-msg");
    document.getElementById("dc-share").addEventListener("click", function () {
      if (navigator.share) {
        navigator.share({ title: "Darts checkout " + raw, text: text, url: card.url })
          .catch(function () {});
      } else if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(function () { msg.textContent = "Copied."; });
      }
    });
    document.getElementById("dc-card").addEventListener("click", function () {
      renderCard(raw, route, routes.length, route.length).toBlob(function (blob) {
        var a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "bryme-checkout-" + raw + ".png";
        a.click();
        URL.revokeObjectURL(a.href);
        msg.textContent = "Card saved.";
      });
    });
  }

  document.getElementById("dc-go").addEventListener("click", go);
  document.getElementById("dc-score").addEventListener("keydown", function (e) {
    if (e.key === "Enter") go();
  });
  go();
})();
