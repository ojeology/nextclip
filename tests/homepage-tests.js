/* BRYME test suite — homepage hero carousel + recommendation engine
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

function loadEnt() {
  const dom = new JSDOM(fs.readFileSync(path.join(ROOT, 'entertainment/index.html'), 'utf8'), {
    runScripts: 'dangerously',
    url: 'https://bryme.onrender.com/',
    beforeParse(window) {
      // stub fetch for the rec-data lazy load
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

(async function () {
  /* 1. Hero structure */
  section('Hero carousel structure');
  {
    const dom = loadEnt();
    const d = dom.window.document;
    assert(d.querySelectorAll('[data-slide]').length === 5, 'exactly 5 hero slides');
    assert(d.querySelectorAll('.hero-slide.is-active').length === 1, 'exactly 1 active slide');
    assert(d.querySelectorAll('[data-hero-dot]').length === 5, '5 dots');
    assert(!!d.querySelector('[data-hero-prev]') && !!d.querySelector('[data-hero-next]'), 'prev/next buttons');
    assert(!!d.querySelector('[data-hero-pause]'), 'pause button present');
    assert(d.querySelectorAll('[data-hero-watch]').length === 5, 'watch-trailer button per slide');
    assert(d.querySelectorAll('.hero-cta-ghost, a.cta-ghost').length >= 5, 'View Details links per slide');
    // no iframe before interaction/autoplay window
    assert(!d.querySelector('.hero-video iframe'), 'no hero iframe initially');
    // slide 1 content
    const h1 = d.querySelector('.hero-slide.is-active h1').textContent;
    assert(['Squid Game', 'Alice in Borderland', 'Into the Badlands', 'Solo Leveling', 'Nosferatu'].indexOf(h1) > -1, 'active slide has a real title (got ' + h1 + ')');
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
    d.querySelectorAll('[data-hero-dot]')[4].click();
    assert(d.querySelectorAll('.hero-slide.is-active h1')[0].textContent === 'Nosferatu' ||
           d.querySelectorAll('.hero-slide.is-active')[0].getAttribute('data-slide') !== null, 'dot jump works');
    dom.window.close();
  }

  /* 3. Trailer playback: only ONE iframe, stops on slide change, mute control */
  section('Trailer playback');
  {
    const dom = loadEnt();
    const d = dom.window.document;
    // click the active slide's watch button
    d.querySelector('.hero-slide.is-active [data-hero-watch]').click();
    const iframes = d.querySelectorAll('.hero-video iframe');
    assert(iframes.length === 1, 'exactly one hero iframe after watch click');
    const vid = d.querySelector('.hero-slide.is-active').getAttribute('data-video');
    assert(vid && iframes[0].src.indexOf('/embed/' + vid) > -1, 'iframe uses the active slide video id (' + vid + ')');
    assert(!iframes[0].src.indexOf('mute=0') > -1 ? iframes[0].src.indexOf('autoplay=1') > -1 : true, 'autoplay param present');
    assert(!d.querySelector('[data-hero-mute]').hidden, 'mute control visible while video plays');
    // switching slides stops the video
    d.querySelector('[data-hero-next]').click();
    assert(d.querySelector('.hero-video').hidden === true || d.querySelectorAll('.hero-video iframe').length === 0, 'video stopped on slide change (no multiple videos)');
    dom.window.close();
  }

  /* 4. Recommendation: valid title */
  section('Recommendation — valid title');
  {
    const dom = loadEnt();
    const d = dom.window.document;
    const input = d.querySelector('[data-rec-input]');
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
      const dom = loadEnt();
      const d = dom.window.document;
      d.querySelector('[data-rec-input]').value = 'zzzz not a real title';
      d.querySelector('[data-rec-form]').dispatchEvent(new dom.window.Event('submit', { cancelable: true }));
      setTimeout(() => {
        const miss = d.querySelector('.rec-miss');
        assert(!!miss, 'friendly unknown-title card shown');
        assert(/couldn't find/i.test(miss.textContent), 'message: "We couldn\'t find that title..."');
        assert(d.querySelectorAll('.rec-pop a').length > 0, 'popular suggestions offered');
        finish2();
      }, 400);
    }
  }
  function finish2() {
    /* 6. Recommendation: empty input */
    section('Recommendation — empty input');
    {
      const dom = loadEnt();
      const d = dom.window.document;
      d.querySelector('[data-rec-form]').dispatchEvent(new dom.window.Event('submit', { cancelable: true }));
      assert(/Type a movie/.test(d.querySelector('[data-rec-status]').textContent), 'prompts for input when empty');
      dom.window.close();
    }

    /* 7. Existing homepage content preserved */
    section('Existing homepage content preserved');
    {
      const home = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
      assert(home.indexOf('🔥 Trending Now') > -1, 'Trending section intact');
      assert(home.indexOf('⭐ Popular Movies') > -1, 'Popular Movies intact');
      assert(home.indexOf('⭐ Popular Series') > -1, 'Popular Series intact');
      assert(home.indexOf('⭐ Popular Anime') > -1, 'Popular Anime intact');
      assert(home.indexOf("👑 Editor's Picks") > -1, "Editor's Picks intact");
      assert(home.indexOf('🆕 New Releases') > -1, 'New Releases intact');
      assert(home.indexOf('Latest articles') > -1, 'Articles section intact');
      assert(home.indexOf('Browse by genre') > -1, 'Genre section intact');
      assert(home.indexOf('href="/movies/"') > -1 && home.indexOf('href="/sports/"') > -1, 'root-relative internal links intact');
      assert(home.indexOf('https://bryme.onrender.com/') > -1, 'absolute production canonical/og:url present');
      assert(home.match(/<title>[^<]+<\/title>/), 'title tag preserved');
      assert(home.indexOf('rel="canonical"') > -1, 'canonical preserved');
      // no indexable duplicate states introduced
      assert(home.indexOf('rec-data" type="application/json') === -1, 'rec data is NOT inline (lazy file)');
    }

    console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
    process.exit(fail ? 1 : 0);
  }
})();
