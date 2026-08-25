/* BRYME service worker v2 — fast repeat visits.
   Assets: cache-first. Pages: network-first with cache fallback. */
const VER = 'bryme-v3-2026-08-25-design-restore';
const ASSETS = `${VER}-assets`;
const PAGES = `${VER}-pages`;
self.addEventListener('install', e => { self.skipWaiting(); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => !k.startsWith(VER)).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin) return;
  if (url.pathname.startsWith('/assets/')) {
    e.respondWith(caches.open(ASSETS).then(c => c.match(e.request).then(r => r || fetch(e.request).then(res => { c.put(e.request, res.clone()); return res; }))));
  } else if (e.request.mode === 'navigate') {
    e.respondWith(fetch(e.request).then(res => { caches.open(PAGES).then(c => c.put(e.request, res.clone())); return res; })
      .catch(() => caches.match(e.request).then(r => r || caches.match('/'))));
  }
});
