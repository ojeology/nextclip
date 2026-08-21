/* BRYME test suite — entertainment hero carousel + recommendation engine
   Run: NODE_PATH=/path/to/jsdom/node_modules node tests/homepage-tests.js */
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const app = fs.readFileSync(path.join(ROOT, 'assets/site-app.js'), 'utf8');

let pass = 0, fail = 0;
function assert(cond, msg) { if (cond) { pass++; } else { fail++; console.log('  ✗ FAIL:', msg); } }
function section(name) { console.log('\n== ' + name + ' =='); }
const sleep = ms => new Promise(r => setTimeout(r, ms));

function loadPage(file) {
  const dom = new JSDOM(fs.readFileSync(path.join(ROOT, file), 'utf8'), {
    runScripts: 'dangerously',
    url: 'https://bryme.onrender.com/',
    beforeParse(window) {
      window.fetch = function () {
        return Promise.resolve({ json: function () {
          return Promise.resolve(JSON.parse(fs.readFileSync(path.join(ROOT, 'data/rec-data.json'), 'utf8')));
        } });
      };
    }
  });
  dom.window.eval(app);
  return dom;
}
const loadEnt = () => loadPage('entertainment/index.html');
const loadHome = () => loadPage('index.html');

(async function () {
  /* 1. Hero structure — /entertainment/ */
  section('Hero carousel structure');
  {
    const dom = loadEnt();
    const d = dom.window.document;
    assert(d.querySelectorAll('[data-slide]').length === 3, 'exactly 3 hero slides');
    assert(d.querySelectorAll('.hero-slide.is-active').length === 1, 'exactly 1 active slide');
    assert(d.querySelectorAll('[data-hero-dot]').length === 3, '3 dots');
    assert(!!d.querySelector('[data-hero-prev]') && !!d.querySelector('[data-hero-next]'), 'prev/next buttons');
    assert(!!d.querySelector('[data-hero-pause]'), 'pause button present');
    assert(d.querySelectorAll('[data-hero-watch]').length === 3, 'Watch Now button per slide');
    assert(d.querySelectorAll('.hero-cta-ghost, a.cta-ghost').length >= 3, 'More Info links per slide');
    assert(!d.querySelector('.hero-video iframe'), 'no hero iframe initially');
    const h1 = d.querySelector('.hero-slide.is-active h1').textContent;
    assert(h1 === 'Project Hail Mary', 'active slide = Project Hail Mary (got ' + h1 + ')');
    assert(d.querySelector('.hero-slide.is-active').getAttribute('data-age') === 'U/A 13+', 'age badge U/A 13+');
    dom.window.close();
  }

  /* 2. Navigation: next/prev/dots */
  section('Carousel navigation');
  {
    const dom = loadEnt();
    const d = dom.window.document;
    const first = d.querySelector('.hero-slide.is-active h1').textContent;
    d.querySelector('[data-hero-next]').click();
    const second = d.querySelector('.hero-slide.is-active h1').textContent;
    assert(second !== first, 'next changes the active slide');
    d.querySelector('[data-hero-prev]').click();
    assert(d.querySelector('.hero-slide.is-active h1').textContent === first, 'prev returns to first');
    d.querySelectorAll('[data-hero-dot]')[2].click();
    assert(d.querySelectorAll('.hero-slide.is-active')[0].getAttribute('data-title') === 'The Shawshank Redemption', 'dot jump to slide 3 works');
    dom.window.close();
  }

  /* 3. Watch Now: embeds are added later — must be graceful without a video id */
  section('Watch Now behaviour');
  {
    const dom = loadEnt();
    const d = dom.window.document;
    d.querySelector('.hero-slide.is-active [data-hero-watch]').click();
    const vid = d.querySelector('.hero-slide.is-active').getAttribute('data-video');
    const iframes = d.querySelectorAll('.hero-video iframe');
    if (vid) {
      assert(iframes.length === 1, 'exactly one hero iframe after watch click');
      assert(iframes[0].src.indexOf('/embed/' + vid) > -1, 'iframe uses the active slide video id (' + vid + ')');
      assert(iframes[0].src.indexOf('autoplay=1') > -1, 'autoplay param present');
      assert(!d.querySelector('[data-hero-mute]').hidden, 'mute control visible while video plays');
      d.querySelector('[data-hero-next]').click();
      assert(d.querySelector('.hero-video').hidden === true || d.querySelectorAll('.hero-video iframe').length === 0, 'video stopped on slide change');
    } else {
      assert(iframes.length === 0, 'no iframe until an official embed is attached (graceful)');
    }
    dom.window.close();
  }

  /* 4. Recommendation — valid title (portal homepage) */
  section('Recommendation — valid title');
  {
    const dom = loadHome();
    const d = dom.window.document;
    const input = d.querySelector('[data-rec-input]');
    assert(!!input, 'recommendation input present on the portal homepage');
    input.value = 'alice in borderland';
    d.querySelector('[data-rec-form]').dispatchEvent(new dom.window.Event('submit', { cancelable: true }));
    setTimeout(() => {
      const tiles = d.querySelectorAll('.rec-grid .tile');
      assert(tiles.length >= 5 && tiles.length <= 8, '5-8 recommendations (got ' + tiles.length + ')');
      assert(/Because you liked/i.test(d.querySelector('.rec-results h3').textContent), 'header: "Because you liked..."');
      assert(d.querySelector('.rec-reason').textContent.indexOf('share') > -1, 'explanation based on shared metadata');
      const titles = Array.from(tiles).map(t => t.querySelector('h3').textContent);
      assert(titles.indexOf('Alice in Borderland') === -1, 'does not recommend the entered title itself');
      assert(new Set(titles).size === titles.length, 'no duplicate recommendations');
      const links = Array.from(d.querySelectorAll('.rec-grid a')).map(a => a.getAttribute('href'));
      assert(links.every(l => l.indexOf('/') === 0 || l.indexOf('https://') === 0), 'recommendation links well-formed');
      assert(links.length >= 10, 'each card has Watch Trailer + View Details (got ' + links.length + ')');
      finish1();
    }, 400);
  }
  function finish1() {
    /* 5. Recommendation: unknown title */
    section('Recommendation — unknown title');
    {
      const dom = loadHome();
      const d = dom.window.document;
      d.querySelector('[data-rec-input]').value = 'zzzz not a real title';
      d.querySelector('[data-rec-form]').dispatchEvent(new dom.window.Event('submit', { cancelable: true }));
      setTimeout(() => {
        const miss = d.querySelector('.rec-miss');
        assert(!!miss, 'friendly unknown-title card shown');
        dom.window.close();
        console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
        process.exit(fail ? 1 : 0);
      }, 400);
    }
  }
})();
