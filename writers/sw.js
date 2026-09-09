// stale-SW cleanup: unregisters the legacy service worker and clears caches
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", (e) => { e.waitUntil((async () => {
  const keys = await caches.keys(); await Promise.all(keys.map((k) => caches.delete(k)));
  await self.registration.unregister();
})()); });
