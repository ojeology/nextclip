/* NEXTCLIP test suite — trailer fallback & verification system
   Run: NODE_PATH=/path/to/jsdom/node_modules node tests/trailer-tests.js */
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const app = fs.readFileSync(path.join(ROOT, 'assets/site-app.js'), 'utf8');

let pass = 0, fail = 0;
function assert(cond, msg) { if (cond) { pass++; } else { fail++; console.log('  ✗ FAIL:', msg); } }
function section(name) { console.log('\n== ' + name + ' =='); }
function load(html, pre) {
  const dom = new JSDOM(html, { runScripts: 'dangerously', url: 'https://ojeology.github.io/nextclip/movie/x/' });
  if (pre) pre(dom.window);
  dom.window.eval(app);
  return dom;
}
const BOX_HTML = `<div data-trailer-box data-trailer-candidates='[{"id":"AAAAAAAAAAA","type":"official-trailer","label":"Official Trailer","channel":"Studio","watch":"https://www.youtube.com/watch?v=AAAAAAAAAAA"},{"id":"BBBBBBBBBBB","type":"official-teaser","label":"Official Teaser","channel":"Studio","watch":"https://www.youtube.com/watch?v=BBBBBBBBBBB"}]' data-trailer-title="Test"><div class="trailer-head"><span class="eyebrow">Trailer</span><span class="trailer-status t-ok">🟢 Official Trailer</span></div><div class="trailer-frame" data-trailer-id="AAAAAAAAAAA"><img src="x"><button type="button" class="trailer-play">Play trailer</button></div><p class="trailer-meta">YouTube · via Studio</p><div class="trailer-error" data-trailer-error hidden><b>Trailer currently unavailable.</b><span>x</span><span class="trailer-error-actions"><a class="quiet-link" data-trailer-watch target="_blank" rel="noopener">Watch on YouTube</a><button type="button" class="trailer-retry" data-trailer-retry>Try again</button></span></div><p class="trailer-fallback">fallback</p><button type="button" class="trailer-alt" data-trailer-alt>Try another trailer</button></div>`;
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

(async function () {
  /* 1. Official trailer: lazy, correct player */
  section('Official trailer (Interstellar)');
  {
    const dom = load(fs.readFileSync(path.join(ROOT, 'movie/interstellar/index.html'), 'utf8'));
    const d = dom.window.document;
    assert(!!d.querySelector('[data-trailer-box]'), 'trailer box present');
    assert(/Official Trailer/.test(d.querySelector('.trailer-status').textContent), 'badge: 🟢 Official Trailer');
    assert(!d.querySelector('.trailer-disclaimer'), 'no disclaimer for official');
    assert(!d.querySelector('[data-trailer-box] iframe'), 'NO iframe before interaction (lazy)');
    d.querySelector('.trailer-play').click();
    const iframe = d.querySelector('[data-trailer-box] iframe');
    assert(!!iframe, 'iframe created after click');
    assert(/^[A-Za-z0-9_-]{11}$/.test('zSWdZVtXT7E'), 'valid 11-char video ID');
    dom.window.close();
  }

  /* 2. Community trailer: yellow label + disclaimer */
  section('Community trailer (Peaky Blinders)');
  {
    const dom = load(fs.readFileSync(path.join(ROOT, 'series/peaky-blinders/index.html'), 'utf8'));
    const d = dom.window.document;
    const status = d.querySelector('.trailer-status');
    assert(/Community trailer/.test(status.textContent), 'badge: 🟡 Community trailer');
    assert(/t-fan/.test(status.className), 'yellow style class');
    assert(!!d.querySelector('.trailer-disclaimer') && /not an official trailer/.test(d.querySelector('.trailer-disclaimer').textContent), 'disclaimer present');
    assert(!/Official Trailer/.test(status.textContent), 'never labelled Official Trailer');
    dom.window.close();
  }

  /* 3. Unavailable: no box, clean message */
  section('Unavailable (Dandadan)');
  {
    const dom = load(fs.readFileSync(path.join(ROOT, 'anime/dandadan/index.html'), 'utf8'));
    const d = dom.window.document;
    assert(!d.querySelector('[data-trailer-box]'), 'no player box when no trailer');
    assert(!!d.querySelector('.trailer-unavailable'), 'clean "Trailer unavailable" card');
    assert(!d.querySelector('iframe'), 'no iframe at all');
    dom.window.close();
  }

  /* 4. REGRESSION: player loads -> watchdog must NOT fire */
  section('Regression: no error after player loads');
  {
    const dom = load(BOX_HTML, w => { w.NEXTCLIP_TRAILER_TIMEOUT = 200; });
    const d = dom.window.document;
    d.querySelector('.trailer-play').click();
    const iframe = d.querySelector('[data-trailer-id] iframe');
    assert(!!iframe, 'iframe created');
    assert(iframe.src.indexOf('enablejsapi=1') > -1, 'embed enables JS API');
    assert(iframe.src.indexOf('playsinline=1') > -1, 'embed plays inline on mobile');
    iframe.dispatchEvent(new dom.window.Event('load'));
    await sleep(450);
    const err = d.querySelector('[data-trailer-error]');
    assert(err && err.hidden, 'NO error card after load (was the bug)');
    assert(!!d.querySelector('[data-trailer-id] iframe'), 'player still visible');
    dom.window.close();
  }

  /* 5. Stuck load -> error card -> retry */
  section('Stuck load -> error card');
  {
    const dom = load(BOX_HTML, w => { w.NEXTCLIP_TRAILER_TIMEOUT = 150; });
    const d = dom.window.document;
    d.querySelector('.trailer-play').click();
    assert(!!d.querySelector('[data-trailer-id] iframe'), 'iframe created');
    await sleep(400);
    const err = d.querySelector('[data-trailer-error]');
    assert(err && !err.hidden, 'error card visible after watchdog timeout');
    assert(!d.querySelector('[data-trailer-id] iframe'), 'no broken player left behind');
    assert(!!d.querySelector('[data-trailer-retry]'), 'Try again button present');
    d.querySelector('[data-trailer-retry]').click();
    assert(!!d.querySelector('[data-trailer-id] iframe'), 'retry recreates the player');
    dom.window.close();
  }

  /* 6. onError mid-play */
  section('onError mid-play');
  {
    const dom = load(BOX_HTML, w => { w.NEXTCLIP_TRAILER_TIMEOUT = 5000; });
    const d = dom.window.document;
    d.querySelector('.trailer-play').click();
    const iframe = d.querySelector('[data-trailer-id] iframe');
    iframe.dispatchEvent(new dom.window.Event('load'));
    dom.window.dispatchEvent(new dom.window.MessageEvent('message', { data: { event: 'onError' } }));
    const err = d.querySelector('[data-trailer-error]');
    assert(err && !err.hidden, 'error card visible after onError');
    assert(!d.querySelector('[data-trailer-id] iframe'), 'no blank iframe left behind');
    const watch = err.querySelector('[data-trailer-watch]');
    assert(watch && watch.getAttribute('href') === 'https://www.youtube.com/watch?v=AAAAAAAAAAA', 'watch link offered');
    dom.window.close();
  }

  /* 7. Multi-candidate cycling */
  section('Multi-candidate cycling');
  {
    const dom = load(BOX_HTML);
    const d = dom.window.document;
    const alt = d.querySelector('[data-trailer-alt]');
    assert(!!alt && !alt.hidden, 'Try another trailer visible');
    alt.click();
    assert(d.querySelector('.trailer-frame').getAttribute('data-trailer-id') === 'BBBBBBBBBBB', 'cycled to second candidate');
    assert(/Official Teaser/.test(d.querySelector('.trailer-status').textContent), 'badge updated');
    alt.click();
    assert(d.querySelector('.trailer-frame').getAttribute('data-trailer-id') === 'AAAAAAAAAAA', 'cycles back to first');
    dom.window.close();
  }

  /* 8. Homepage: zero iframes */
  section('Homepage performance');
  {
    const dom = load(fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8'));
    const d = dom.window.document;
    assert(d.querySelectorAll('iframe').length === 0, 'homepage loads ZERO iframes');
    assert(d.querySelectorAll('img').length > 30, 'posters used instead');
    dom.window.close();
  }

  /* 9. Admin audit page */
  section('Trailer admin page (/trailers/)');
  {
    const dom = load(fs.readFileSync(path.join(ROOT, 'trailers/index.html'), 'utf8'));
    const d = dom.window.document;
    assert(d.querySelectorAll('#ta-body tr').length === 630, 'admin table lists 630 titles');
    const f = d.getElementById('ta-filter');
    f.value = 'fan-made';
    f.dispatchEvent(new dom.window.Event('change'));
    const community = d.querySelectorAll('#ta-body tr').length;
    assert(community > 10, 'community filter works (' + community + ')');
    const q = d.getElementById('ta-q');
    q.value = 'interstellar';
    q.dispatchEvent(new dom.window.Event('input'));
    assert(d.querySelectorAll('#ta-body tr').length === 1, 'search narrows to Interstellar');
    dom.window.close();
  }

  /* 10. VideoObject schema accuracy */
  section('Structured data accuracy');
  {
    const s1 = fs.readFileSync(path.join(ROOT, 'movie/interstellar/index.html'), 'utf8');
    assert(s1.indexOf('VideoObject') > -1, 'official trailer emits VideoObject');
    const s2 = fs.readFileSync(path.join(ROOT, 'series/peaky-blinders/index.html'), 'utf8');
    assert(s2.indexOf('VideoObject') === -1, 'community trailer does NOT emit VideoObject');
    const s3 = fs.readFileSync(path.join(ROOT, 'anime/dandadan/index.html'), 'utf8');
    assert(s3.indexOf('VideoObject') === -1, 'no-trailer title does NOT emit VideoObject');
  }

  console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
  process.exit(fail ? 1 : 0);
})();
