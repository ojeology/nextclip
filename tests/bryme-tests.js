/* BRYME test suite — branding, verticals, hero fixes, suggestions
   Run: NODE_PATH=/path/to/jsdom/node_modules node tests/bryme-tests.js */
const { JSDOM } = require('jsdom');
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const app = fs.readFileSync(path.join(ROOT, 'assets/site-app.js'), 'utf8');

let pass = 0, fail = 0;
function assert(cond, msg) { if (cond) { pass++; } else { fail++; console.log('  ✗ FAIL:', msg); } }
function section(name) { console.log('\n== ' + name + ' =='); }
const read = p => fs.readFileSync(path.join(ROOT, p), 'utf8');

/* 1. Branding */
section('BRYME branding');
{
  const home = read('index.html');
  assert(/<a class="brand"[^>]*>BRY<b>ME<\/b><\/a>/.test(home), 'brand mark = BRYME');
  assert(home.indexOf("Discover what you love. Learn what you need. Find what's next.") > -1, 'slogan on homepage');
  assert(home.indexOf('| BRYME') > -1, 'title suffix = BRYME');
  assert(/property="og:site_name" content="BRYME"/.test(home), 'og:site_name = BRYME');
  assert(home.indexOf(('NEXT' + 'CLIP')) === -1, 'no obsolete brand literal anywhere on homepage');
  assert(home.indexOf('BRYME_BASE') > -1, 'JS base constant = BRYME_BASE');
  // footer
  assert(home.indexOf('/entertainment/') > -1 && home.indexOf('/sports/') > -1 && home.indexOf('/memes/') > -1 &&
         home.indexOf('/make-money/') > -1 && home.indexOf('/tech/') > -1, 'footer links all 5 verticals');
}

/* 2. Vertical hubs */
section('Vertical hubs');
{
  const hubs = {
    'sports/index.html': 'BRYME Sports',
    'memes/index.html': 'BRYME Memes',
    'make-money/index.html': 'BRYME Make Money',
    'tech/index.html': 'BRYME Tech',
    'entertainment/index.html': 'BRYME Entertainment'
  };
  for (const [f, expect] of Object.entries(hubs)) {
    const s = read(f);
    assert(/<h1>/.test(s), f + ' has h1');
    assert(s.indexOf(('NEXT' + 'CLIP')) === -1, f + ' has no obsolete brand literal');
    assert(/rel="canonical" href="https:\/\/bryme\.onrender\.com\//.test(s), f + ' canonical on production domain');
    assert(/<link rel="canonical"/.test(s) && /property="og:title"/.test(s), f + ' SEO meta present');
  }
  assert(read('sports/index.html').indexOf('class="vcat"') > 0, 'sports hub lists categories');
  assert(read('make-money/index.html').indexOf('No fake income claims') > -1, 'make-money honest-note present');
  assert(read('memes/index.html').indexOf('do not scrape random copyrighted images') > -1, 'memes copyright note present');
}

/* 3. Vertical category pages */
section('Vertical category pages');
{
  for (const f of ['sports/champions-league/index.html', 'memes/whatsapp-stickers/index.html',
                   'make-money/freelancing/index.html', 'make-money/platform-reviews/index.html', 'tech/ai-tools/index.html',
                   'tech/ai-tutorials/index.html', 'sports/international/index.html']) {
    const s = read(f);
    assert(/<h1>/.test(s), f + ' has h1');
    assert(s.indexOf('foundation ready') > -1, f + ' shows honest placeholder state');
    assert(s.indexOf(('NEXT' + 'CLIP')) === -1, f + ' no obsolete brand literal');
  }
}

/* 4. Sitemap includes verticals */
section('Sitemap');
{
  const sm = read('sitemap.xml');
  for (const p of ['/sports/', '/memes/', '/make-money/', '/tech/', '/entertainment/', '/sports/premier-league/', '/tech/ai-tools/', '/memes/whatsapp-stickers/']) {
    assert(sm.indexOf('bryme.onrender.com' + p) > -1, 'sitemap includes ' + p);
  }
}

/* 5. Search index has verticals */
section('Search index');
{
  const idx = JSON.parse(read('data/search-index.json'));
  assert(idx.verticals && idx.verticals.length >= 54, 'search index has vertical entries (' + (idx.verticals || []).length + ')');
  const sports = idx.verticals.find(v => v.slug === 'sports');
  assert(sports && sports.title === 'BRYME Sports', 'sports vertical entry present');
  assert(idx.movies.length === 632, 'entertainment catalogue intact in search index');
}

/* 6. Hero: muted autoplay + single video + suggestions (DOM test) */
section('Homepage fixes (DOM)');
{
  const { VirtualConsole } = require('jsdom');
  let navTarget = null;
  const vc = new VirtualConsole();
  vc.on('jsdomError', function (e) {
    if (/navigation/.test(String(e.message || ''))) navTarget = 'NAVIGATION_ATTEMPTED';
  });
  const dom = new JSDOM(read('index.html'), {
    runScripts: 'dangerously',
    virtualConsole: vc,
    url: 'https://bryme.onrender.com/',
    beforeParse(window) {
      window.fetch = function () {
        return Promise.resolve({ json: function () {
          return Promise.resolve(JSON.parse(read('data/rec-data.json')));
        } });
      };
    }
  });
  dom.window.eval(app);
  const d = dom.window.document;
  // watch click -> iframe, muted by default
  d.querySelector('.hero-slide.is-active [data-hero-watch]').click();
  const ifr = d.querySelector('.hero-video iframe');
  assert(!!ifr, 'hero iframe created on watch click');
  assert(ifr.src.indexOf('mute=1') > -1, 'hero video loads MUTED by default (no forced audio)');
  assert(ifr.src.indexOf('autoplay=1') > -1, 'autoplay attempted');
  assert(d.querySelectorAll('.hero-video iframe').length === 1, 'only one hero video at a time');
  assert(!d.querySelector('[data-hero-mute]').hidden, 'unmute control visible');
  // suggestions: type "alice"
  const input = d.querySelector('[data-rec-input]');
  input.value = 'alice';
  input.dispatchEvent(new dom.window.Event('input'));
  setTimeout(() => {
    const items = d.querySelectorAll('.rec-sug-item');
    assert(items.length >= 1, 'suggestion dropdown appears while typing (got ' + items.length + ')');
    const first = items[0];
    const href = first.getAttribute('data-sug');
    assert(!!href, 'suggestion has a slug');
    first.click();
    setTimeout(() => {
      // jsdom cannot complete navigation, but the click MUST trigger a location change attempt
      assert(navTarget === 'NAVIGATION_ATTEMPTED', 'clicking a suggestion navigates to the title page (navigation attempt detected)');
      dom.window.close();
      console.log('\nRESULTS: ' + pass + ' passed, ' + fail + ' failed');
      process.exit(fail ? 1 : 0);
    }, 200);
  }, 500);
}
