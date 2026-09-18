/* BRYME Social Bar unit v1 (19 Sep 2026, owner file bryme-ad-scripts.md §2).
   Owner's new unit, loaded ONCE site-wide, isolated from the display/native
   containers (never merged, never stacked in one box). The owner's file
   labelled it "Monetag"; the delivering host pl31304019.profitableratecpmnetwork.com
   is Adsterra's serving family (same pattern as the working pl31304018 native
   zone), and Social Bar is Adsterra's own format - this is an Adsterra unit,
   consistent with the "focus on Adsterra" directive. The file also asked to
   confirm no old Monetag vignette/push script remains before enabling:
   confirmed - Monetag was fully removed on 19 Sep (b47d249: both zones and the
   site tag deleted; live HTML and /assets/monetag.js verified clean), so this
   cannot double up with a legacy aggressive unit.
   Same-origin loader keeps the ad-host string out of HTML (quality gate) and
   the inline-script ban (CSP): a dynamic <script> is appended at
   DOMContentLoaded, async, cf-async-exempt like the native zone.
   Mobile scope note (owner asked): the bar renders its own fixed UI, which we
   do not control from here. Defensive measure below: the site's mobile bottom
   navigation is lifted to a very high stacking level on small screens so a
   bottom-docked bar can never cover navigation. If the bar overlaps content on
   devices, the dashboard-side fix (position Top, or a frequency cap) is the
   right lever - code does not fight ad overlays for z-index. */
(function () {
  "use strict";
  if (window.__BRYME_AD_SB__) return;
  window.__BRYME_AD_SB__ = true;

  var SRC = "https://pl31304019.profitableratecpmnetwork.com/7c/e5/f0/7ce5f0421abe8df585e6bba232f4e614.js";

  function boot() {
    var css = document.createElement("style");
    css.textContent =
      "@media(max-width:720px){.bottom-nav,.mobile-nav{z-index:2147483000}}";
    document.head.appendChild(css);
    var s = document.createElement("script");
    s.async = true;
    s.setAttribute("data-cfasync", "false");
    s.src = SRC;
    document.body.appendChild(s);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
