# BRYME Home & DIY — §16 interactive decision tools (25 September 2026).
# Two jurisdiction-honest tools, same architecture as the tech desk's:
# deterministic rules in external JS assets (site CSP blocks inline scripts),
# noscript decision tree in the page, reasoning rendered per answer,
# on-device only — no storage, no network calls.
#   /home/rent-or-buy-tool/     — six questions, answer shaped by MARKET:
#                                 UK / US / Canada / AU-NZ / EU / Nigeria / other.
#                                 Mechanics only (stamp duty, closing costs,
#                                 land transfer tax, upfront-rent norms, title
#                                 due diligence) — never price predictions,
#                                 never invented numbers (brief §11/§30).
#   /home/which-heating-system/ — gas / heat pump / modern electric /
#                                 keep-and-tune / cool-first, with the
#                                 fabric-first rule stated honestly.

RENT_BUY_SLUG = "rent-or-buy-tool"
HEATING_SLUG = "which-heating-system"

RENT_BUY_BODY = """<div class="prose">
<p class="byline">BRYME Home &amp; DIY desk &middot; published 25 September 2026 &middot; the tool runs entirely in your browser &mdash; no answers are stored or sent anywhere &middot; general information, never financial advice</p>
<p><b>The honest rent-or-buy answer depends on where you live, how long you&rsquo;ll stay, and what buying costs to enter and exit &mdash; not on headlines about prices.</b> This tool asks six questions, then gives you the call <em>for your market</em>: the transaction costs that decide the timescale, the schemes you might qualify for, and the due diligence that actually protects you. What it will never do is predict house prices &mdash; nobody can, and anyone who does is selling something.</p>
<style>
.rb-card{border:1px solid var(--line-strong);border-radius:12px;background:var(--sheet);padding:20px 22px;max-width:760px}
.rb-step{font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);margin:0 0 6px}
.rb-q{font-size:19px;font-weight:700;margin:0 0 14px;font-family:var(--serif)}
.rb-opts{display:flex;flex-direction:column;gap:8px}
.rb-opt{text-align:left;padding:11px 14px;border:1px solid var(--line-strong);border-radius:10px;background:var(--card);font:inherit;font-size:14.5px;cursor:pointer}
.rb-opt:hover,.rb-opt:focus-visible{border-color:var(--accent);background:var(--paper)}
.rb-opt small{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
.rb-nav{display:flex;gap:10px;margin-top:16px;align-items:center}
.rb-nav button{padding:8px 16px;border-radius:9px;border:1px solid var(--line-strong);background:var(--card);font:inherit;font-size:14px;cursor:pointer}
.rb-nav .rb-progress{font-size:12.5px;color:var(--dim);margin-left:auto}
.rb-result h3{margin:0 0 8px;font-family:var(--serif);font-size:22px}
.rb-why{margin:0 0 14px;padding-left:20px;font-size:14.5px}
.rb-why li{margin-bottom:6px}
.rb-dilig{font-size:14px;border-left:3px solid var(--accent);padding:8px 12px;background:var(--paper);margin:0 0 14px}
.rb-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.rb-links a{font-size:13.5px;border:1px solid var(--line-strong);border-radius:999px;padding:6px 13px}
.rb-links a:hover,.rb-links a:focus-visible{border-color:var(--accent)}
.rb-privacy{font-size:12.5px;color:var(--dim);margin-top:14px}
</style>
<div id="rent-or-buy-tool"></div>
<noscript>
<p><b>The tool needs JavaScript. Here is the honest framework, statically:</b></p>
<ul>
<li><b>The five-year test beats every headline.</b> Add up every cost of entering and exiting a purchase in your market &mdash; transfer taxes, legal fees, agent fees, mortgage setup. If you can&rsquo;t comfortably stay long enough for equity and stability to clear that pile, renting is buying flexibility, not &ldquo;throwing money away.&rdquo;</li>
<li><b>Staying under ~2 years:</b> rent, almost everywhere. Transaction costs alone rarely round-trip that fast.</li>
<li><b>2&ndash;5 years:</b> rent deliberately &mdash; and bank the difference on purpose. First-home schemes are worth checking now even if you buy later.</li>
<li><b>5&ndash;10 years with a deposit and stable income:</b> buying usually starts to win on cost predictability &mdash; not on price promises.</li>
<li><b>10+ years:</b> buying&rsquo;s strongest case: you set the rules of your own home, and the entry costs amortise over a decade.</li>
<li><b>Nigeria&rsquo;s twist:</b> rent is commonly demanded 1&ndash;2 years upfront, which changes the cash-flow maths entirely &mdash; and if buying, title verification (C of O, governor&rsquo;s consent, a real survey) is the step that protects you, not the fence.</li>
</ul>
</noscript>
<script src="/assets/rent-or-buy-tool.js" defer></script>

<h2 id="why-six">Why the market question comes first</h2>
<p>Every &ldquo;rent or buy&rdquo; calculator that ignores jurisdiction is doing arithmetic on fiction. The entry costs alone are different animals: <b>UK</b> stamp duty with first-time-buyer relief; <b>US</b> closing costs and an annual property-tax bill that never ends; <b>Canada</b> land transfer tax (with first-time rebates in some provinces) and mortgage insurance below 20% down; <b>Australia and New Zealand</b> state-by-state stamp duty and grants; the <b>EU</b> with notary fees and transfer taxes that swing hugely by country; and <b>Nigeria</b>, where the structural facts are different again &mdash; upfront rent norms, thinner mortgage availability, and title due diligence as the central risk. Same six questions; genuinely different answers.</p>

<h2 id="what-decides">What actually decides it (everywhere)</h2>
<table class="lg-table lg-scroll">
<thead><tr><th>Factor</th><th>Pulls toward buying</th><th>Pulls toward renting</th></tr></thead>
<tbody>
<tr><td>Time horizon</td><td>7+ years, roots down</td><td>Under 5 years, life still moving</td></tr>
<tr><td>Entry/exit costs</td><td>Low in your market or scheme-assisted</td><td>High stamp/transfer/agent costs</td></tr>
<tr><td>Income shape</td><td>Stable, mortgage-serviceable</td><td>Variable &mdash; flexibility has real value</td></tr>
<tr><td>Rent vs carrying cost</td><td>Rent &ge; monthly cost of owning</td><td>Rent well below owning costs</td></tr>
<tr><td>Repair reality</td><td>You&rsquo;ll maintain it (see <a href="/home/emergency-repair-fund/">the repair fund</a>)</td><td>Someone else&rsquo;s problem &mdash; <a href="/home/renter-vs-owner-repairs/">renter vs owner repairs</a></td></tr>
</tbody></table>
<p>The worked comparison behind the tool: <a href="/home/rent-vs-buy-explained/">rent vs buy, explained</a>. If buying is the call, the next pages are <a href="/home/mortgage-payments-explained/">what mortgage payments actually are</a>, <a href="/home/moving-costs-explained/">what moving really costs</a>, and <a href="/home/renter-vs-owner-repairs/">which repairs become yours</a>. The whole shelf: <a href="/home/owning-money/">Owning &amp; money</a>.</p>

<h2 id="limits">What this tool deliberately does not do</h2>
<ul>
<li><b>It never predicts prices.</b> &ldquo;Prices always go up&rdquo; is not a plan; history says they go up, down, and sideways depending on market and decade.</li>
<li><b>It doesn&rsquo;t quote your numbers.</b> Stamp-duty bands, tax rates and scheme thresholds change &mdash; the tool names the mechanic; the official calculator for your jurisdiction gives the figure.</li>
<li><b>It isn&rsquo;t financial advice.</b> It&rsquo;s a structured way to think &mdash; the desk&rsquo;s boundary, stated plainly.</li>
<li><b>It doesn&rsquo;t phone home.</b> No analytics on your answers, no storage, no network calls.</li>
</ul>
</div>"""

HEATING_BODY = """<div class="prose">
<p class="byline">BRYME Home &amp; DIY desk &middot; published 25 September 2026 &middot; the tool runs entirely in your browser &mdash; no answers are stored or sent anywhere &middot; general information, not professional advice &mdash; gas work belongs to qualified professionals</p>
<p><b>The honest heating question isn&rsquo;t &ldquo;which machine?&rdquo; &mdash; it&rsquo;s &ldquo;how much heat does this house leak?&rdquo;</b> A heat pump in a draughty house is an expensive way to heat the garden. So this tool puts the fabric first (insulation, draughts, glazing), then places you on the equipment ladder &mdash; keep-and-tune, modern gas, modern electric, or heat pump &mdash; and for hot climates it flips the question to cooling, which is what &ldquo;heating&rdquo; actually means in Lagos or a Mediterranean summer.</p>
<style>
.ht-card{border:1px solid var(--line-strong);border-radius:12px;background:var(--sheet);padding:20px 22px;max-width:760px}
.ht-step{font-size:12.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);margin:0 0 6px}
.ht-q{font-size:19px;font-weight:700;margin:0 0 14px;font-family:var(--serif)}
.ht-opts{display:flex;flex-direction:column;gap:8px}
.ht-opt{text-align:left;padding:11px 14px;border:1px solid var(--line-strong);border-radius:10px;background:var(--card);font:inherit;font-size:14.5px;cursor:pointer}
.ht-opt:hover,.ht-opt:focus-visible{border-color:var(--accent);background:var(--paper)}
.ht-opt small{display:block;color:var(--muted);font-size:12.5px;margin-top:2px}
.ht-nav{display:flex;gap:10px;margin-top:16px;align-items:center}
.ht-nav button{padding:8px 16px;border-radius:9px;border:1px solid var(--line-strong);background:var(--card);font:inherit;font-size:14px;cursor:pointer}
.ht-nav .ht-progress{font-size:12.5px;color:var(--dim);margin-left:auto}
.ht-result h3{margin:0 0 8px;font-family:var(--serif);font-size:22px}
.ht-why{margin:0 0 14px;padding-left:20px;font-size:14.5px}
.ht-why li{margin-bottom:6px}
.ht-cost{font-size:14px;border-left:3px solid var(--accent);padding:8px 12px;background:var(--paper);margin:0 0 14px}
.ht-links{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.ht-links a{font-size:13.5px;border:1px solid var(--line-strong);border-radius:999px;padding:6px 13px}
.ht-links a:hover,.ht-links a:focus-visible{border-color:var(--accent)}
.ht-privacy{font-size:12.5px;color:var(--dim);margin-top:14px}
</style>
<div id="which-heating-tool"></div>
<noscript>
<p><b>The tool needs JavaScript. Here is the whole ladder, statically:</b></p>
<ul>
<li><b>Rung 0 &mdash; keep and tune (often $0&ndash;low):</b> bleed radiators, correct boiler pressure, replace filters, set the thermostat deliberately, close the draughts. A surprising share of &ldquo;heating problems&rdquo; live here &mdash; <a href="/home/how-to-bleed-a-radiator/">bleed a radiator</a>, <a href="/home/boiler-pressure-low-or-high/">boiler pressure</a>, <a href="/home/thermostat-settings-that-save-money/">thermostat settings</a>.</li>
<li><b>Rung 1 &mdash; fabric first:</b> loft insulation, draught-proofing, then glazing. Every machine after this works cheaper &mdash; <a href="/home/attic-insulation-basics/">attic insulation</a>, <a href="/home/draught-proofing-mistakes/">draught-proofing</a>.</li>
<li><b>Rung 2 &mdash; heat pump:</b> the efficiency winner in a well-insulated home; a struggle in a leaky one &mdash; <a href="/home/heat-pump-vs-gas-furnace/">heat pump vs gas, honestly</a>.</li>
<li><b>Rung 3 &mdash; modern condensing gas boiler:</b> still the pragmatic call where the gas grid exists, the fabric is poor, and the budget is now &mdash; installed and certified by a qualified professional, always.</li>
<li><b>Rung 4 &mdash; modern electric:</b> where there&rsquo;s no gas grid: efficient panels or an air-source unit on a good tariff; old storage heaters are the expensive version of electric &mdash; <a href="/home/storage-heaters-explained/">storage heaters explained</a>, <a href="/home/off-peak-electricity-tariffs-explained/">off-peak tariffs</a>.</li>
<li><b>Hot climate &mdash; cooling is the heating question:</b> shade and airflow first, then a correctly sized AC, then the fan economics &mdash; <a href="/home/cost-to-run-air-conditioning/">AC running costs</a>, <a href="/home/ceiling-fan-direction-summer-winter/">fan direction</a>, <a href="/home/window-film-for-heat/">window film</a>.</li>
</ul>
</noscript>
<script src="/assets/which-heating-tool.js" defer></script>

<h2 id="why-ladder">Why a ladder and not a brand list</h2>
<p>Because the order of operations is the whole answer. Spending on machinery before fabric buys comfort at the highest possible per-unit price; spending on fabric first means every machine after it can be smaller, cheaper and more efficient. That&rsquo;s why the tool asks about insulation and draughts before it asks what&rsquo;s on the wall &mdash; and why &ldquo;keep and tune&rdquo; is a real recommendation, not a cop-out. The maths behind each rung: <a href="/home/is-it-cheaper-to-heat-one-room/">heating one room vs the house</a>, <a href="/home/epc-rating-explained/">what the EPC rating means</a>, and the whole <a href="/home/energy-bills/">energy &amp; bills cluster</a>.</p>

<h2 id="costs">The cost shapes (directional, never quotes)</h2>
<table class="lg-table lg-scroll">
<thead><tr><th>Rung</th><th>Upfront shape</th><th>Running shape</th><th>The catch</th></tr></thead>
<tbody>
<tr><td>Keep &amp; tune</td><td>~$0&ndash;low</td><td>Cuts bills immediately</td><td>Only fixes what&rsquo;s actually wrong &mdash; not a plan for a dead system</td></tr>
<tr><td>Fabric first</td><td>Moderate, room by room</td><td>Permanent reduction</td><td>Payback is years, not months &mdash; it&rsquo;s an asset, not a trick</td></tr>
<tr><td>Heat pump</td><td>High</td><td>Low per unit of heat</td><td>Wants good fabric; sizing and installer quality decide everything</td></tr>
<tr><td>Modern gas</td><td>Moderate</td><td>Follows gas prices</td><td>Fuel-price exposure; professional install and servicing non-negotiable</td></tr>
<tr><td>Modern electric</td><td>Low&ndash;moderate</td><td>Per-kWh is the pricey part</td><td>Tariff choice moves the bill more than the hardware does</td></tr>
</tbody></table>

<h2 id="limits">What this tool deliberately does not do</h2>
<ul>
<li><b>It doesn&rsquo;t size anything.</b> Real sizing is a survey &mdash; a tool that guesses kW from six answers is guessing.</li>
<li><b>It doesn&rsquo;t touch gas advice.</b> Boiler installs, moves and flue work belong to qualified professionals in every jurisdiction.</li>
<li><b>It doesn&rsquo;t quote prices.</b> The shapes above are directional; local installers and your tariff decide.</li>
<li><b>It doesn&rsquo;t phone home.</b> No analytics on your answers, no storage, no network calls.</li>
</ul>
</div>"""

INVERTER_SLUG = "inverter-sizing-calculator"

INVERTER_BODY = """<div class="prose">
<p class="byline">BRYME Home &amp; DIY desk &middot; published 25 September 2026 &middot; the tool runs entirely in your browser &mdash; no answers are stored or sent anywhere &middot; general information, never professional advice</p>
<p><b>The right inverter size is decided by your actual load &mdash; not by a sales counter.</b> Tick what actually runs in your home, add anything missing, and the tool sizes the inverter (with a surge margin), the battery bank (for your chemistry and autonomy) and the solar array that refills it &mdash; showing every line of the arithmetic. It pairs with the desk&rsquo;s <a href="/generator-vs-inverter-nigeria/">generator-or-inverter guide</a>: that page helps you choose; this one sizes what you chose.</p>
<style>
.iv-card{border:1px solid var(--line-strong);border-radius:12px;background:var(--sheet);padding:20px 22px;max-width:760px}
.iv-card fieldset{border:1px solid var(--line-strong);border-radius:10px;padding:10px 16px 14px;margin-bottom:14px}
.iv-card legend{font-weight:700;padding:0 8px}
.iv-row{display:flex;align-items:center;gap:10px;padding:7px 0;border-bottom:1px dashed var(--line);font-size:14.5px}
.iv-row small{margin-left:auto;color:var(--muted);font-size:12.5px}
.iv-note{font-size:13px;color:var(--muted);margin:10px 0 0}
.iv-flds{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}
.iv-flds label{display:flex;flex-direction:column;gap:6px;font-weight:600;font-size:14px}
.iv-flds select{padding:10px 12px;border:1px solid var(--line-strong);border-radius:8px;font-size:15px;background:var(--paper);color:var(--ink)}
.iv-out{margin-top:16px;border-left:3px solid var(--accent);background:var(--paper);padding:12px 16px;border-radius:8px}
.iv-out h3{margin:0 0 8px;font-family:var(--serif)}
.iv-out ul{margin:0;padding-left:20px}
.iv-out li{margin:6px 0;font-size:14.5px}
.iv-privacy{font-size:12.5px;color:var(--muted);margin-top:14px}
</style>
<div id="inverter-sizing-calculator"></div>
<noscript>
<p><b>The tool needs JavaScript. Here is the honest framework, statically:</b></p>
<ul>
<li><b>Daily energy:</b> add up (watts &times; hours per day) for everything that runs. That Wh/day number decides the battery and the solar; the peak decides the inverter.</li>
<li><b>Inverter:</b> take the watts that could run <em>at the same moment</em>, add ~25% surge margin (motors and compressors spike on start), then pick the next standard size above it.</li>
<li><b>Battery:</b> Wh/day &times; days of autonomy &divide; (system voltage &times; usable fraction). Lead-acid gives you ~50% of its label; lithium ~80%. Size the bank on usable, not label.</li>
<li><b>Solar:</b> Wh/day &divide; (peak sun hours &times; ~0.75 system efficiency). Nigeria typically sees 4&ndash;6 peak sun hours across the year &mdash; use the honest season, not the best month.</li>
<li><b>What this doesn&rsquo;t replace:</b> nameplate readings, a surge audit on fridges and pumps, cable sizing, and a qualified installer. Those are the steps that make a system safe.</li>
</ul>
</noscript>
<script src="/assets/inverter-sizing-tool.js" defer></script>

<h2 id="why-load">Why the load list decides everything</h2>
<p>Two homes can buy the &ldquo;same&rdquo; 1.5 kVA inverter and have opposite experiences, because one runs a fridge and a pump and the other runs lights and a TV. The load list is the only honest input: <b>watts from the nameplate</b> (not the marketing box), <b>hours it actually runs a day</b>, and the appliances that can start <em>at the same time</em>. Everything the tool outputs follows arithmetically from those three numbers.</p>
<p>The two classic mistakes it protects against: buying battery capacity in label amp-hours and getting half of it (deep-discharging lead-acid kills it), and sizing solar from the best month&rsquo;s sunshine and wondering why harmattan leaves the bank empty.</p>
</div>"""

HOME_DECISION_TOOLS = [
(RENT_BUY_SLUG,
 "Rent or buy where I live? \u2014 a jurisdiction-honest decision tool",
 "Six questions, one honest answer for YOUR market \u2014 UK, US, Canada, Australia, EU or Nigeria: entry costs, time horizon, schemes. No price predictions, ever.",
 RENT_BUY_BODY),
(HEATING_SLUG,
 "Which heating system fits my home? \u2014 gas, heat pump, electric or keep-and-tune",
 "Gas, heat pump, modern electric or keep-and-tune: six questions place your home on the honest heating ladder \u2014 fabric first, cost shapes shown, no quotes invented.",
 HEATING_BODY),(INVERTER_SLUG,
 "What size inverter and battery does my home need? \u2014 a load-first sizing tool",
 "Tick your actual appliances and the tool sizes the inverter (with surge margin), battery bank and solar array \u2014 every line of the working shown. Load first, labels second.",
 INVERTER_BODY),

]
