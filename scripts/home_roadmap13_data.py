# BRYME Home & DIY - roadmap batch 13: ground-zero tools + renter fixes + the
# symptom router. Batch 74, 14 Sep 2026. Tools are browser-only (.calc markup,
# assets/home-tools.js). General information, never professional advice; the
# electrical/gas boundaries stay absolute.

HOME_ROADMAP_13 = [
("paint-calculator", "guide",
"The paint calculator: how much paint a room actually needs",
 "Wall area, coats and can sizes in ten seconds - the honest arithmetic, the adjustments that matter, and when to fix the wall before you paint it.",
"""<p>Paint is bought in cans and cans come in litres, but rooms come in whatever shape the builder left. This calculator does the one piece of maths every painter needs: the wall area, the coats, and what to actually buy. All browser-side - nothing you type leaves the page.</p>
<div class="calc"><h2>The calculator</h2>
<label>Room length (m) <input id="pc-l" type="number" inputmode="decimal" min="1" max="30" step="0.1"></label>
<label>Room width (m) <input id="pc-w" type="number" inputmode="decimal" min="1" max="30" step="0.1"></label>
<label>Wall height (m) <input id="pc-h" type="number" inputmode="decimal" min="1.5" max="6" step="0.05"></label>
<label>Doors in the room <input id="pc-doors" type="number" inputmode="numeric" min="0" max="8" step="1" value="1"></label>
<label>Windows in the room <input id="pc-windows" type="number" inputmode="numeric" min="0" max="15" step="1" value="1"></label>
<label>Coats <select id="pc-coats"><option value="1">One</option><option value="2" selected="selected">Two (the usual answer)</option><option value="3">Three</option></select></label>
<button class="calc-go" data-calc="paint" data-html="1">Calculate my paint</button>
<p class="calc-out" id="pc-out" aria-live="polite" style="display:block"></p></div>
<h2>How the maths works</h2>
<p>Wall area is the perimeter times the height: 2 x (length + width) x height. Each door is reckoned at about 1.9 square metres and each window at about 1.4, and they come off the total. A litre of typical emulsion covers roughly 10 square metres per coat - that is the industry's usual figure, and it varies by brand, so the can's own number wins ties. The calculator adds 10 per cent for trays, roller skins and the bit that drips, then rounds up to the nearest half litre.</p>
<h2>The adjustments that actually matter</h2>
<p><b>Dark over light, or any big colour change:</b> add a coat - the calculator's three-option input is where honesty lives; two coats is the usual answer, three is common over reds and navies. <b>Bare new plaster:</b> it drinks - a diluted first coat (or a primer) before the counting even starts. <b>Textured or rough walls:</b> up to 20 per cent more paint; the surface area is bigger than it looks. <b>The ceiling:</b> not in this sum - it adds roughly the floor's area per coat, which for most rooms is one extra litre or so.</p>
<h2>Fix the wall first, always</h2>
<p>No calculator saves you from painting over a problem. Damp shows through every coat - diagnose it first (<a href="/home/condensation-vs-rising-vs-penetrating-damp/">which damp is it?</a>) and never seal it in with paint (<a href="/home/painting-over-damp/">painting over damp, explained</a>). Humid rooms need paint chosen for them (<a href="/home/humidity-and-paint/">humidity and paint</a>), and prep is the difference between one repaint and three (<a href="/home/interior-painting-mistakes/">the mistakes list</a>). The cost side of the job - paint, kit, your time - sits with <a href="/home/home-repair-costs-explained/">repair costs, estimated</a>.</p>
<p>Approximate by design: the calculator is a planning tool, not a quotation. Buy the second can returnable if your shop allows it, and note the colour and brand when a room comes out right - future you will need exactly that line.</p>
<script src="/assets/home-tools.js?v=1" defer></script>"""),
("renter-friendly-fixes", "guide",
"Renter-friendly fixes: improve the place without losing the deposit",
 "What a tenant may usually do, what needs the landlord's yes, and how to document everything - the difference between a nicer home and a deducted deposit.",
"""<p>Renting does not have to mean living in someone else's beige. There is a wide band of improvements that are reversible, harmless and usually yours to make - and a clear line past which everything belongs to the owner. This page maps the band, the line, and the paperwork habit that protects the deposit. Your tenancy agreement overrides everything here; read it first.</p>
<h2>Usually yours to do (reversible, no holes or harm)</h2>
<p><b>Hang things with removable strips and tension rods</b> - picture ledges, mirrors, curtains, shower caddies, without a single drill hole. <b>Swap lampshades and plug-in lamps</b> - lighting is the cheapest transformation in any home, and it reverses in a minute. <b>Refresh the sealant</b> around a bath or sink that has gone black at the edges - cleaning and re-sealing maintenance is expected care, not alteration (check the tenancy; take a photo before). <b>Rugs, furniture, plants, freestanding shelves</b> - everything that leaves with you, leaves with you. <b>Door drafts and thermal curtains</b> - reversible comfort that trims the bill (<a href="/home/draught-proofing-mistakes/">do it without the classic mistakes</a>).</p>
<h2>Ask first (sometimes yes, never assume)</h2>
<p><b>Painting</b> - some landlords welcome a neutral repaint; others deduct for it. Get the yes in writing, agree the colours, and keep the original paint tin names if they are in the cupboard. <b>Drilling and wall plugs</b> - TV brackets and shelving into masonry; some contracts allow "reasonable fixtures", and some ban holes outright. <b>Replacing fixtures</b> - shower heads, taps, cabinet handles: keep the originals labelled in a box, and put them back at move-out. <b>Anything touching the boiler, the fuse board or gas</b> - never a tenant job, full stop; report, do not touch (the boundaries are the same as the owner's own: <a href="/home/why-does-my-circuit-breaker-keep-tripping/">breaker problems get reported, not opened</a>).</p>
<h2>The documentation habit that wins disputes</h2>
<p>Photo of every wall and floor on move-in day, date-stamped. Photo before and after every fix or improvement you make. Keep receipts for sealant, blinds and any agreed paint. When the check-out inspection comes, the difference between "tenant damage" and "normal wear, tenant improved it" is exactly this folder. Damp and mould are the special case: report early and in writing, because the cause is usually the building's (<a href="/home/condensation-ventilation-that-works/">vent your side honestly</a>, and know the landlord's duties if you are in the UK: <a href="/home/uk-landlord-damp-mould-duties/">dated and explained</a>).</p>
<h2>Who fixes what</h2>
<p>The responsibility split - owner's repairs versus tenant's care - is mapped on <a href="/home/renter-vs-owner-repairs/">renter vs owner repairs</a>, and the security upgrades worth asking for are on <a href="/home/renter-security/">renter security</a>. A dripping tap is usually a two-pound washer - ask the landlord if they would rather you just fix it; many say yes (<a href="/home/how-to-fix-a-dripping-tap/">the honest fix</a>). Whatever you change, change it back cleanly: the deposit is won at move-out by whoever kept the receipts.</p>"""),
("why-is-my-home-doing-that", "guide",
"Why is my home doing that? A symptom finder for the ten common complaints",
 "Damp patch, dripping tap, tripping breaker, cold room, mystery smell: match the symptom, get the likely cause, and land on the page that fixes it.",
"""<p>Houses speak in symptoms. The trick - and this page is the trick - is matching what you are seeing to the page that actually explains it, instead of guessing from a forum at midnight. Find your symptom below; each one links the desk's full diagnosis. General information throughout: if anything smells of gas, or electrics are scorching or buzzing, stop and call a professional now.</p>
<h2>Find your symptom</h2>
<p><b>A damp patch low on the wall, worse in winter:</b> almost always condensation finding a cold corner - the three damp types and how to tell them apart are on <a href="/home/condensation-vs-rising-vs-penetrating-damp/">which damp is it?</a></p>
<p><b>A damp patch high on the wall, or one spot that never dries:</b> that pattern points to a leak or penetration, not lifestyle - <a href="/home/small-leak-ripple-effect/">how small leaks ripple</a> explains why the stain is bigger than the drip.</p>
<p><b>A tap that drips:</b> usually a worn washer or cartridge, and one of the cheapest honest fixes in the house - <a href="/home/how-to-fix-a-dripping-tap/">the dripping tap, fixed</a> (and the cost logic in <a href="/home/leaky-faucet-diy/">DIY or call someone</a>).</p>
<p><b>The sink drains slowly:</b> a forming blockage, not a mystery - clear it before it becomes a callout: <a href="/home/how-to-fix-a-slow-draining-sink/">the slow-draining sink</a>.</p>
<p><b>The breaker keeps tripping:</b> the circuit is protecting you; the page explains the three usual culprits and the point where you stop: <a href="/home/why-does-my-circuit-breaker-keep-tripping/">the tripping breaker</a>. Any scorch marks, buzzing or burning smell moves you to <a href="/home/electrical-fire-warning-signs/">the warning signs page</a> and a phone call.</p>
<p><b>A musty smell that cleaning never touches:</b> hidden moisture, usually ventilation - the pattern and the fixes: <a href="/home/condensation-ventilation-that-works/">ventilation that works</a>.</p>
<p><b>One room that never gets warm:</b> heat is leaving somewhere it should not - start with <a href="/home/draught-proofing-mistakes/">draught-proofing done right</a>, then the glass maths in <a href="/home/single-glazing-payback/">single glazing payback</a>.</p>
<p><b>Radiator hot at the bottom, cold at the top:</b> air in the system, and a bleed key's job - <a href="/home/how-to-bleed-a-radiator/">bleed a radiator</a>.</p>
<p><b>The fridge runs but food is warm:</b> usually the coils, the door seal, or the defrost - diagnose in order: <a href="/home/fridge-not-cold-enough/">fridge not cold</a>.</p>
<p><b>The washing machine will not drain:</b> almost always the filter or the pump path - <a href="/home/washing-machine-wont-drain/">washer won't drain</a>.</p>
<h2>When the symptom is bigger than the page</h2>
<p>Some signs end the DIY conversation immediately: gas smell, repeated breaker trips with nothing plugged in, a ceiling bulging with water, cracks through brickwork, anything inside the fuse board or boiler. Those are professional calls - and part of owning a home is having the money ready for them, which is what <a href="/home/emergency-repair-fund/">the emergency repair fund</a> is for. Everything else on this page is knowledge you can act on tonight.</p>"""),
]
