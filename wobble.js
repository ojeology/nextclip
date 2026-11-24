const { chromium } = require('playwright');
const routes = ['/writers/', '/writers/writing/', '/writers/catalogue/', '/writers/writing/wired/', '/writers/learn/writing-basics/active-vs-passive-voice/', '/writers/articles/', '/writers/tools/'];
(async () => {
  const b = await chromium.launch();
  for (const w of [320, 360, 390, 414]) {
    const p = await b.newPage({ viewport: { width: w, height: 780 }, isMobile: true, hasTouch: true });
    for (const r of routes) {
      await p.goto('http://127.0.0.1:8787' + r, { waitUntil: 'networkidle' });
      await p.waitForTimeout(200);
      const out = await p.evaluate((vw) => {
        const doc = document.documentElement;
        const over = [...document.querySelectorAll('body *')]
          .map(el => { const r = el.getBoundingClientRect(); return { el, r }; })
          .filter(({ r }) => r.width > 0 && (r.right > vw + 1 || r.left < -1))
          .filter(({ el, r }) => {
            // ignore things inside a deliberately scrollable container
            let a = el.parentElement;
            while (a && a !== document.body) {
              const cs = getComputedStyle(a);
              if (cs.overflowX === 'auto' || cs.overflowX === 'scroll') return false;
              a = a.parentElement;
            }
            return true;
          })
          .slice(0, 6)
          .map(({ el, r }) => `${el.tagName.toLowerCase()}.${(el.className || '').toString().split(' ').slice(0,3).join('.')} left=${Math.round(r.left)} right=${Math.round(r.right)} w=${Math.round(r.width)}`);
        return { scrollW: doc.scrollWidth, clientW: doc.clientWidth, bodyScroll: document.body.scrollWidth, offenders: over };
      }, w);
      if (out.scrollW > out.clientW + 1 || out.offenders.length) {
        console.log(`\n=== ${w}px ${r}  scrollW=${out.scrollW} clientW=${out.clientW}`);
        out.offenders.forEach(o => console.log('   ', o));
      }
    }
    await p.close();
  }
  await b.close();
})();
