/* Former Monetag in-page-push worker. Unregister so returning visitors drop it. */
self.addEventListener('install', function (e) { self.skipWaiting(); });
self.addEventListener('activate', function (e) {
  e.waitUntil(self.registration.unregister().then(function () {
    return self.clients.matchAll();
  }).then(function (clients) {
    clients.forEach(function (c) { if (c.navigate) c.navigate(c.url); });
  }));
});
