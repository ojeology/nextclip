/* Logic harness for the two HOME decision tools (§16). Fake DOM; drives the real render loop. */
const fs = require('fs');

function makeNode(tag) {
  const n = {
    tag, children: [], handlers: {}, attrs: {}, className: '', type: '', href: '', _html: ''
  };
  Object.defineProperty(n, 'innerHTML', {
    get() { return n._html; },
    set(v) { n._html = v; n.children.length = 0; }
  });
  n.appendChild = (c) => { n.children.push(c); return c; };
  n.setAttribute = (k, v) => { n.attrs[k] = v; };
  n.addEventListener = (ev, fn) => { n.handlers[ev] = fn; };
  return n;
}

function load(file, mountId) {
  const mount = makeNode('div');
  const doc = {
    getElementById: (id) => (id === mountId ? mount : null),
    createElement: makeNode
  };
  new Function('document', fs.readFileSync(file, 'utf8'))(doc);
  return mount;
}

function allText(node) {
  let t = node._html || '';
  for (const c of node.children) t += ' ' + allText(c);
  return t;
}
function findByClass(node, cls) {
  if ((node.className || '').split(' ').includes(cls)) return node;
  for (const c of node.children) { const r = findByClass(c, cls); if (r) return r; }
  return null;
}
function clickThrough(mount, indices, optCls) {
  for (const idx of indices) {
    const opts = findByClass(mount, optCls);
    if (!opts) throw new Error('no options row at step');
    const btns = opts.children;
    if (!btns[idx] || !btns[idx].handlers.click) throw new Error('no clickable option ' + idx);
    btns[idx].handlers.click();
  }
}

let pass = 0, fail = 0;
function ok(cond, label) { if (cond) { pass++; } else { fail++; console.log('FAIL:', label); } }

/* ---------- rent-or-buy ---------- */
const RB = 'assets/rent-or-buy-tool.js';
function rb(indices) {
  const mount = load(RB, 'rent-or-buy-tool');
  clickThrough(mount, indices, 'rb-opts');
  const card = mount.children[0];
  const res = findByClass(card, 'rb-result');
  return {
    text: allText(card),
    h3: res ? res.children.find(c => c.tag === 'h3')._html : '',
    aria: card.attrs['aria-live'],
    links: (findByClass(card, 'rb-links') || { children: [] }).children.map(a => a.href),
    startover: allText(card).includes('Start over')
  };
}
let r;
r = rb([0,0,2,0,1,0]);                       // uk, lt2 -> rent-flexibility
ok(r.h3.includes('without the guilt'), 'uk short horizon -> rent, no guilt');
ok(r.text.includes('flexibility') , 'flexibility framing present');
r = rb([0,1,2,0,1,1]);                       // uk, y2_5 -> rent-save
ok(r.h3.includes('bank the difference'), 'uk 2-5y -> rent-save');
r = rb([1,2,0,0,1,2]);                       // us, y5_10, deposit none -> rent-save
ok(r.h3.includes('bank the difference'), 'us no deposit -> rent-save');
ok(r.text.includes('emergency fund comes first'), 'emergency-fund-first ordering stated');
r = rb([2,3,1,0,1,2]);                       // ca, y10p, small+stable -> buy-schemes
ok(r.h3.includes('scheme support'), 'ca small deposit stable -> buy-schemes');
ok(r.text.includes('FHSA'), 'ca diligence names FHSA');
r = rb([5,3,3,0,2,3]);                       // ng, y10p, large+stable -> buy-ready + NG diligence
ok(r.h3.includes('realistic call'), 'ng strong -> buy-ready');
ok(r.text.includes('Certificate of Occupancy'), 'NG diligence: title verification named');
ok(r.text.includes('YEARS upfront'), 'NG diligence: upfront-rent norm named');
r = rb([3,2,2,1,3,2]);                       // anz, y5_10, standard+variable+unknown -> rent-save (income gate) + caveats
ok(r.h3.includes('bank the difference'), 'variable income never reaches a buy outcome -> rent-save');
ok(r.text.includes('income shape'), 'rent-save reason names income shape');
ok(r.text.includes('homework'), 'unknown rentcost -> homework note');
r = rb([4,1,3,0,2,0]);                       // eu, y2_5, renthigh -> rent-save + re-run note
ok(r.h3.includes('bank the difference'), 'eu 2-5y -> rent-save even with high rent');
ok(r.text.includes('re-run this maths yearly'), 'high-rent re-run warning');
r = rb([0,2,1,2,0,3]);                       // uk, small+growing+rentcheap+control -> rent-save + ownership note
ok(r.h3.includes('bank the difference'), 'rentcheap blocks schemes path -> rent-save');
ok(r.text.includes('ranked ownership itself highly'), 'control priority acknowledged');
/* privacy + a11y + start over */
ok(r.aria === 'polite', 'result card aria-live=polite');
ok(r.startover, 'start-over control present');
ok(r.links.every(h => h.startsWith('/home/')), 'all outcome links are internal /home/ links');

/* ---------- which-heating ---------- */
const HT = 'assets/which-heating-tool.js';
function ht(indices) {
  const mount = load(HT, 'which-heating-tool');
  clickThrough(mount, indices, 'ht-opts');
  const card = mount.children[0];
  const res = findByClass(card, 'ht-result');
  return {
    text: allText(card),
    h3: res ? res.children.find(c => c.tag === 'h3')._html : '',
    aria: card.attrs['aria-live'],
    links: (findByClass(card, 'ht-links') || { children: [] }).children.map(a => a.href)
  };
}
let h;
h = ht([3,0,0,0,0,0]);                       // hot -> cool-first
ok(h.h3.toLowerCase().includes('cool'), 'hot climate -> cool-first');
h = ht([0,2,0,2,0,0]);                       // coldgas, modern electric -> keep-tune
ok(h.text.includes('modern hardware'), 'modern hardware -> keep-tune');
h = ht([0,0,2,0,0,1]);                       // poor fabric, minimal budget -> keep-tune (fixes)
ok(h.text.includes('honest ladder starts at fixes'), 'minimal budget -> fixes-first');
h = ht([0,0,2,1,0,1]);                       // poor fabric, moderate budget -> fabric-first
ok(h.text.includes('worth more on the envelope'), 'leaky+moderate -> fabric-first');
h = ht([0,0,0,1,0,1]);                       // good fabric, gas, bills driver -> keep-tune
ok(h.text.includes('tune before you spend'), 'tight house + gas + bills -> tune');
h = ht([1,3,0,1,2,1]);                       // coldnogas, none, good, moderate, emissions -> heatpump
ok(h.text.includes('coherent answer'), 'no-gas + good fabric + emissions -> heat pump');
h = ht([1,1,1,2,0,0]);                       // coldnogas, old electric -> modern-electric + storage note
ok(h.text.includes('expensive version of electric'), 'old storage heaters flagged');
h = ht([0,0,2,2,1,1]);                       // gas broken, poor fabric, replacement -> modern-gas
ok(h.text.includes('expensive mistake this tool exists to prevent'), 'fabric-first rule: no HP into leaky house');
h = ht([0,0,0,2,2,1]);                       // gas, good fabric, replacement, emissions -> heatpump
ok(h.text.includes('textbook heat-pump case'), 'textbook HP case');
h = ht([2,0,1,2,3,1]);                       // mild, gas, medium, replacement, comfort -> modern-gas
ok(h.text.includes('pragmatic call'), 'mild + medium fabric -> modern gas pragmatic');
ok(h.aria === 'polite', 'heating result aria-live=polite');
ok(h.links.every(x => x.startsWith('/home/')), 'heating links internal');

console.log(pass + ' passed, ' + fail + ' failed');
process.exit(fail ? 1 : 0);
