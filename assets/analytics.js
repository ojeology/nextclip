/* BRYME analytics loader.
   To activate Google Analytics 4, paste your measurement ID below, e.g. GA_ID = "G-XXXXXXXXXX".
   Nothing loads and no data is collected until an ID is set. */
(function () {
  "use strict";
  var GA_ID = "G-NQKHPBYFE8"; /* GA4 measurement ID */
  if (!GA_ID || !/^G-[A-Z0-9]+$/.test(GA_ID)) return;
  var s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag("js", new Date());
  gtag("config", GA_ID, { anonymize_ip: true });
})();
