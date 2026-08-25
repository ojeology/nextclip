/* BRYME analytics loader (GA4). */
(function () {
  "use strict";
  var GA_ID = "G-NQKHPBYFE8";
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
