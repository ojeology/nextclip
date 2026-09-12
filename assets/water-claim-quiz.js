/* BRYME - "Will my water damage claim be covered?" interactive quiz (batch 33, 12 Sep 2026).
   General guidance only, never insurance advice. CSP-safe external script. */
(function () {
  "use strict";
  var root = document.getElementById("water-claim-quiz");
  if (!root) return;
  var Q = [
    { id: "src", t: "Where did the water come from?",
      o: [["inside", "Inside the home \u2014 a pipe, appliance or plumbing fixture"],
          ["outside", "Outside the home \u2014 rising water, storm surge or surface flooding"]] },
    { id: "sud", t: "How suddenly did it happen?",
      o: [["sudden", "Suddenly and unexpectedly"],
          ["gradual", "Gradually \u2014 over days, weeks or longer"],
          ["unsure", "Not sure yet"]] },
    { id: "maint", t: "Had the affected area been regularly maintained?",
      o: [["yes", "Yes \u2014 regular checks and upkeep"],
          ["no", "No \u2014 or there was a known issue left unfixed"],
          ["unsure", "Not sure"]] }
  ];
  var a = {}, step = 0;
  function esc(s){ return String(s).replace(/[&<>]/g, function(c){ return {"&":"&amp;","<":"&lt;",">":"&gt;"}[c]; }); }
  function render() {
    var h = '<p class="wcq-kick">Will my claim be covered?</p>';
    if (step < Q.length) {
      h += '<p class="wcq-q"><b>' + (step + 1) + ' of ' + Q.length + '.</b> ' + esc(Q[step].t) + '</p><div class="wcq-opts">';
      Q[step].o.forEach(function (o) {
        h += '<button type="button" data-v="' + o[0] + '">' + esc(o[1]) + '</button>';
      });
      h += '</div>';
      if (step > 0) h += '<button type="button" class="wcq-back" data-back>Back</button>';
    } else { h += result(); }
    root.innerHTML = h;
    var bs = root.querySelectorAll("[data-v]");
    for (var i = 0; i < bs.length; i++) bs[i].addEventListener("click", function () {
      a[Q[step].id] = this.getAttribute("data-v"); step++; render();
    });
    var bk = root.querySelector("[data-back]");
    if (bk) bk.addEventListener("click", function () { step--; render(); });
    var rs = root.querySelector("[data-restart]");
    if (rs) rs.addEventListener("click", function () { a = {}; step = 0; render(); });
  }
  function result() {
    var v, t;
    if (a.src === "outside") {
      v = 'Almost certainly not covered \u2014 this is a flood';
      t = '<p>Water from an external source \u2014 rising rivers, storm surge, surface water \u2014 is <b>flood</b>, and standard homeowners policies exclude it. Flood cover lives in a separate policy: the NFIP or a private insurer in the US (FEMA: one inch of floodwater can cause up to $25,000 of damage), Flood Re-backed policies in the UK, and overland-water endorsements in Canada.</p>'
        + '<p><b>Do now:</b> stay safe (never walk in moving water), photograph everything, and call your insurer or broker about flood cover and any disaster assistance that may apply.</p>';
    } else if (a.sud === "gradual" || (a.maint === "no" && a.sud !== "sudden")) {
      v = 'At high risk of denial \u2014 gradual damage or maintenance';
      t = '<p>Insurance is built for <b>sudden and accidental</b> events. Damage that built up over time, or traces to a known, unfixed issue, sits in the exclusions most denials cite.</p>'
        + '<p><b>Do now:</b> stop the source, mitigate further damage, and document honestly anyway \u2014 if any part of the loss was sudden (a final burst after discovery, for example), a plumber\u2019s letter saying so matters. Then fix the underlying cause so the next event is clean.</p>';
    } else if (a.src === "inside" && a.sud === "sudden" && a.maint === "yes") {
      v = 'Likely covered \u2014 the sudden-and-accidental case';
      t = '<p>A sudden, accidental failure inside the home \u2014 a burst pipe, an appliance overflow \u2014 with the area maintained is exactly what these policies are designed to pay for (the water damage, though not usually upgrading the failed component itself).</p>'
        + '<p><b>Do now:</b> shut off the water, call mitigation fast (water degrades from clean to contaminated within about 48 hours), document everything \u2014 wide shots, close-ups, the source, a dated room-by-room log, receipts \u2014 and report the claim promptly. Mold is covered only while you mitigated quickly.</p>';
    } else {
      v = 'Gray area \u2014 the details decide';
      t = '<p>Your answers sit where claims are genuinely contested: sudden components with maintenance questions, or unclear timing. These are decided on evidence.</p>'
        + '<p><b>Do now:</b> mitigate and document as if the claim will be disputed \u2014 photos, dated notes, the plumber\u2019s findings on the failed part \u2014 then ask the insurer direct questions: is this event covered, what is my deductible, and do I need repair estimates? Sewer or sump-pump backup is only covered with a specific endorsement; mold follows the fate of the initial event.</p>';
    }
    return '<p class="wcq-kick">Your answers suggest:</p><p class="wcq-verdict">' + v + '</p>' + t
      + '<p class="wcq-disc">General guidance only \u2014 never insurance advice. Your policy wording decides; when money is significant, a licensed adjuster or public adjuster reviews it with you.</p>'
      + '<p><a class="btn secondary" href="#claim-process">The full claim walkthrough</a> <button type="button" class="btn secondary" data-restart>Start again</button></p>';
  }
  render();
})();
/* styles are injected by the article page (inline <style>), keeping this file logic-only */
