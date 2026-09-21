# -*- coding: utf-8 -*-
"""BRYME Home & DIY desk — the Nigeria moat (Phase 1 T11, 21 Sep 2026).

Uncontested territory: harmattan, rainy season, borehole water, generator and
inverter maths, wiring red flags, mould after a flood — written for how homes
here actually behave. Tuple shape mirrors the other HOME_* modules:
(slug, kicker, title, dek, body-html). House rule: safety boundaries stated
without apology; no prices; anything that needs a licensed professional says so.
"""

HOME_LOCAL = [
 ("generator-vs-inverter-nigeria",
  "power",
  "Generator or inverter? The decision is a spreadsheet, not a brand",
  "Before you spend on either, run the arithmetic your salesperson skipped: your real watt-hours, your surge loads, and the one battery rule that decides whether the system survives year two.",
  """<p>Every power quote you receive is priced by kVA and Ah. What your house actually consumes is measured in watt-hours, and that arithmetic - five minutes with a notebook - decides whether your next power purchase feels like freedom or like a rented disappointment.</p>
<h2>Step one: write your real load</h2>
<p>For one honest week, list what you actually run during an outage and for how long: fridge (compressor cycles roughly a third of the hour, not full-time), fans, TV and decoder, router, lights, laptops, water pump. Nameplate watts are on each appliance's sticker; multiply by hours and add up - that's your watt-hour demand per outage. Most homes discover their "big generator instinct" is three times the actual need, and their "small inverter shortcut" is half the real one.</p>
<h2>Step two: surges, not averages</h2>
<p>Motors - fridge compressor, pumping jack, freezer, any borehole pump - pull two to three times their running watts for a few seconds on start. An inverter or generator sized to the sum of running watts will brown out on the evening the pump and fridge decide to wake up together. Sum the running watts, add the largest single motor's surge headroom, and buy against that number. This is the spec salespeople round down.</p>
<h2>Step three: the battery rule</h2>
<p>If you go inverter: usable capacity is roughly half your nominal kWh for lead-acid chemistry (deep cycling a car battery daily kills it in months - the "tubular" upgrade buys time, not immunity), and lithium tolerates much deeper cycles but still ages by heat. Nigerian roof-space heat is the silent budget-killer: a battery in a hot cupboard in year one is a replacement quote in year three. Ventilate the battery room, keep it off the floor, and ask for the installation's battery temperature story before you ask about warranty paper.</p>
<h2>Where each one genuinely wins</h2>
<ul><li><b>Generator:</b> cheap energy per hour while you burn fuel, tireless through long outages, tolerant of a full house running at once. Its true costs are fuel price volatility, service intervals you must actually keep, and noise your neighbours are pricing into their own patience.</li>
<li><b>Inverter + batteries:</b> silent, instant, phone-charging-friendly, and the only option that becomes <em>cheaper</em> over time once solar panels join it. Its true cost is capacity bought upfront: you cannot "borrow" extra stored sunlight on a harmattan week.</li>
<li><b>The hybrid answer almost everyone wants:</b> a small generator wired to charge a real battery bank (changeover done by a licensed electrician with a proper changeover switch and earthing - the death-avoidance part of the diagram), so the generator runs at its efficient steady load to fill batteries instead of babysitting every bulb.</li></ul>
<h2>The check before you buy anything</h2>
<p>Whatever the quote says, make it write: running watts covered, surge watts covered, battery chemistry and usable depth, and - if solar-ready - whether the inverter accepts panels today or needs a replacement later. A vendor who can answer those four questions in writing is selling a system. One who answers "trust me, it'll carry your house" is selling tomorrow's phone call.</p>"""),

 ("harmattan-and-your-electronics",
  "seasonal",
  "Harmattan is hard on screens, laptops and printers - the five-minute fixes that work",
  "Dry air and suspended dust are a chemistry set your devices were not shipped with. Nothing here needs a technician: it needs a calendar and a microfibre cloth.",
  """<p>For six to ten weeks a year, the air in your house is carrying fine mineral dust and holding almost no humidity, and your electronics pay for it in three currencies: heat, static and jammed moving parts. Every fix below is prevention; the cure, once dust has cooked onto a fan blade or paper has curled in a tray, is service fees.</p>
<h2>What actually happens to your devices</h2>
<ul><li><b>Fan intakes cake first.</b> Laptops on beds and sofas - where the intakes are blocked <em>and</em> the fabric is shedding - build a felt layer on the fan within one season. That layer is insulation with a motor attached.</li>
<li><b>Static stops chips slowly.</b> A dry room with synthetic carpet and a nylon chair is a charge generator. Sudden laptop death with no warning is usually not the dry air itself - it's the discharge that happened when someone reached across the desk to touch the open chassis.</li>
<li><b>Screens abrade.</b> Dust on a panel isn't dirt, it's grit; wiping a dry screen with a tissue is sandpaper with confidence.</li>
<li><b>Printers jam on paper mood.</b> Low humidity makes sheet edges curl and static-hold to each other; the top sheet of an old ream is where all the feed failures start.</li></ul>
<h2>The season kit (ten minutes a week)</h2>
<p>One: laptops onto hard trays or lap-desks, off textiles, intakes facing air they can steal - a cheap hard tray works. Two: open the printer cover, fan the stacked paper before loading, and keep the ream in its wrapper with a folded flap when idle. Three: wipe screens <em>after</em> blowing loose dust off (a camera blower or the keyboard trick: short bursts from the far edge), cloth barely damp, never sprayed on the panel. Four: before touching any open chassis - desktop case, TV back, console - touch a grounded metal part of it first, and keep the humidifier on the desk, not the floor. Five: once, mid-season, take the laptop to a shaded table and blow the vents out from the exhaust side while it runs off charge; a year's felt, in ten seconds.</p>
<h2>The humidifier trap nobody warns you about</h2>
<ul><li>Ultrasonic misters scatter whatever is in their water - including salt - onto everything within reach as a fine conductive film. Near electronics, use distilled or boiled-and-cooled water without exception, and point the mist away from desks. A "humidified" desk under a hard-water mister is a corrosion experiment you're funding.</li></ul>
<h2>When to call the professional</h2>
<p>Anything that involves opening a sealed power supply, a TV that clicks and won't light, or a laptop that runs hot <em>after</em> a dust clear - that's the desk's boundary, stated without apology: capacitor charge and glued panels are where YouTube lessons end and burnt mains begin. Fans, filters, paper and cloth are entirely yours.</p>"""),

 ("rainy-season-home-checklist",
  "seasonal",
  "The pre-rains home checklist that Lagos roofs actually need",
  "Gutters, sealant, ceiling pencil-marks, drainage fall and the weep holes nobody remembers: a Saturday of small inspections that turns a leaking ceiling into a paragraph in this checklist instead.",
  """<p>Water does not attack a house all at once; it queues. Every rainy-season emergency on a Nigerian roof has a dry-season version - a half-blocked gutter, a cracked seal, a downpipe pointed at the wall - and each one costs an hour before the rains to fix and a month of repainting after. This is that hour, ordered so the ladder work happens once.</p>
<h2>Roof and gutters (dry boots, two people, morning light)</h2>
<ul><li><b>The bucket test.</b> Clear every gutter and downpipe by hand, then pour two full buckets into the far end of each run. It should leave the downpipe at the ground in seconds, in a steady stream. Anything that backs up, drips at a joint or exits slower than the next bucket proves is a blockage or a fall problem - fix it before the first storm decides for you.</li>
<li><b>Sealant and screws.</b> Walk the parapet and flashings: sheet-to-wall junctions, vent pipes, the screw lines on every roof sheet. Sealant that crumbles to powder under a fingernail is gone, whatever the colour says. Re-bed it; missing screws get replaced with the same neoprene-washer type, not a smaller one.</li>
<li><b>The pencil habit.</b> Mark the corners of every ceiling stain with a dated pencil note on the floorboard behind furniture, not the wall. After the first heavy rain, a stain that grew or a new mark is an active leak with a postcode; a stain that sat unchanged for a season is history. This one pencil is the difference between "repaint" and "find the sheet first."</li></ul>
<h2>Windows and walls</h2>
<p>Slide-frame aluminium windows have weep holes in the outer track - small slots meant to let wind-blown rain out. Construction cement and years of neglect seal them shut, and then the frame becomes a fish tank for your wall. Clear every one with a cocktail stick and a damp rag before the rains. Outside: confirm the ground <em>falls away</em> from the foundation on all sides; a flat apron that puddles against the wall is rising damp on a payment plan. Check the paint at skirting height - chalky, bubbling or crumbling there means the ground, not the roof.</p>
<h2>Power and water, the parts people forget</h2>
<ul><li>Generator and inverter: outdoor units get a raised, drained, roofed position <em>and</em> an exhaust that points away from every window - the rain-storm habit of closing windows around a running generator is how carbon monoxide gets invited indoors; keep the intake side of the house clear and the machine outside, always. (This is the desk's hard line, not a suggestion.)</li>
<li>Water tanks: covers sealed gap-free - storm water pooling on top of an open tank is a mosquito nursery with a maintenance schedule; flush the sediment from the bottom tap before the rains dilute what you're storing.</li></ul>
<h2>The ten-minute wrap</h2>
<p>Photograph the cleared gutters, the pencil marks, the fresh sealant lines, and the dated note goes in the house file. Not for anyone else: when a leak appears next year, your photo set tells a roofer where to look first, and that sentence is worth more than the gutter itself.</p>"""),

 ("borehole-water-and-your-kettle",
  "water",
  "Borehole water, kettle scale and your filter: what actually needs solving",
  "Why white flakes are chemistry, not poison; which problems a boil fixes and which it makes worse; and the filter order that makes sense for a Nigerian borehole.",
  """<p>Nigerian borehole water arrives with three completely different problems that everyone solves as if they were one: hardness, sediment and the occasional biological surprise. A kettle tells you about the first, a white towel about the second, and - for the third - nothing visible does anything at all, which is why the boring test matters.</p>
<h2>Scale is not dirt</h2>
<p>White flakes in a boiled kettle, grey film on a stainless sink, laundry that needs more soap than the packet swears: that's dissolved calcium and magnesium - temporary hardness - precipitating when heated. It is a plumbing-and-appliance issue, not a health one, and boiling <em>concentrates</em> the visible part of it into your kettle element instead of removing it from your glass. What you do about it is engineering, not anxiety: a water softener (salt-dosed, regenerates, needs a drain point) for whole-house appliance protection, or nothing but descaling ritual for the kettle if scale is your only complaint. Magnetic "conditioners" are a cheap science-fair toy at best; don't fund one.</p>
<h2>Sediment, and the order filters go in</h2>
<p>If the towel test turns brown after a minute of cold tap water - fine silt, laterite cloud after rain, or a silty run after the pump kicks - you have suspended solids, and the solution is not expensive, it is ordered: <b>sediment first, carbon second, anything finer third.</b> A spun polypropylene sock (changed when flow visibly drops, not by calendar) eats the silt that would choke every downstream cartridge and scratch every tap valve. Carbon after it improves taste, chlorine where any exists, and the organics that make water "off" without making it dangerous. Skipping to an RO unit as your first move is how homes buy a machine that its own prefilter would have protected - and pay for the waste water RO rejects to fix a problem a cheap sediment sock solved.</p>
<h2>The test no filter can smell</h2>
<p>Boiling is a treatment, not a verdict: it kills germs if given a proper rolling minute, but it destroys nothing - it doesn't remove nitrate, salt, metals or the agricultural cocktail that shallow wells near soak-aways can carry. So once a year, for a small lab fee at a university or state water lab, hand them a bottle of your water <em>after</em> your filters and ask for the two-line answer that matters at home: bacterial contamination indicators, and the dissolved-solids/salt figure. That sheet, kept with the house file, is what "our water is fine" should mean - instead of an opinion about clarity.</p>
<h2>And the tank, always</h2>
<p>Everything above assumes the storage tank is honest: lid sealed against birds and leaves, vent meshed, no sunlit wall for algae, and drained-scrushed-flushed on a rhythm you actually keep (most homes: once a year, before the rains refill everything you stored). The treatment plant is the tank, first - every filter you buy is really insurance you didn't want to need.</p>"""),

 ("wiring-red-flags-in-your-home",
  "safety",
  "Eight wiring signs in a finished Nigerian home that mean call a professional",
  "Warm sockets, dimming lights, daisy-changed breakers, the missing earth - the visible symptoms of problems that become fires at 2 a.m., and the exact sentence to say to an electrician.",
  """<p>Most houses in this country carry wiring installed by the seat of someone's pants - competent in their habit, not in your standards. The reassuring part of electrical faults is that almost every serious one announces itself visibly and early. This page is a translation guide for those announcements, plus the boundary: what you may tighten, what you must hire.</p>
<h2>Call-a-professional signs, ranked by how fast they matter</h2>
<ul><li><b>A socket or plug that is warm, smells of hot plastic, or has brown ghost-marks around the pins.</b> That's resistance heating at a loose connection - a fire that has begun its paperwork. Stop using the socket today, and "today" is the entire warning.</li>
<li><b>Lights dim or bulbs surge when a large appliance starts.</b> Classic loose neutral or overloaded joint - the supply is being shared through a connection smaller than it should be. This one is not cosmetic and not "old houses do that."</li>
<li><b>No earth wire at three-pin sockets.</b> A strip of green-yellow is not decoration; without it an appliance fault makes the metal case - the fridge, the water heater - the live conductor through whoever touches it. Any socket cover you open to find bare copper ends and no earth is a rewiring conversation, not a repair.</li>
<li><b>Twisted tape joins inside walls or above ceilings.</b> Where a junction box should be, a "handled with tape and confidence" splice waits. Tape dries; joints oxidise; faults don't. Every hidden join should sit in an accessible box with a proper connector.</li>
<li><b>One breaker that won't stay in, or trips when the kettle <em>and</em> anything else run.</b> Either the circuit is overloaded past its cable's rating - breakers protect cables, so a breaker that's fighting its job means the cable is losing it - or the breaker itself is tired. Neither is a swap-shop job; both need an actual load check.</li>
<li><b>A board where circuits are shared by improvisation:</b> kitchen on the lights' breaker, AC on a "twin" slot crammed into a space for one device, the spare ways stacked double. Every legitimate panel spare that got two breakers where one sat is how this list begins.</li>
<li><b>Burnt, blackened or "melted-sweet" plastic at the meter tails or changeover.</b> Supply side: hands off, notify the service provider and get a licensed contractor with their paperwork for anything ahead of your main switch.</li>
<li><b>An RCD that has never been tested or never trips on test.</b> The little test button exists for one ritual: press it every quarter. No trip from a live safety device is no safety device.</li></ul>
<h2>What you may actually fix yourself</h2>
<p>With the breaker off and a confirmed dead with your own tester: re-clip a faceplate, replace a switch on the same terminals, swap a flex on a lamp. Anything that runs <em>inside</em> a wall, spans a joint, touches the board, or involves the meter - professional. This desk states its boundary without apology: water, aluminium mains and "small corrections at night" are the three words nearest every tragedy in the news.</p>
<h2>The sentence to say when you hire</h2>
<p>"Test first, quote second, certificate with the work." A real electrician can explain load and circuit for every breaker in your board, will never laugh at the warm-socket question, and expects you to ask for what the wiring in your house is actually made of. If the conversation starts with "how much for me to just add a socket here," the correct answer is a different electrician.</p>"""),

 ("mould-after-a-flooded-room",
  "safety",
  "Mould after a flood or a leaking roof: the 48-hour window and the cut line",
  "What can be saved, what belongs in a bin bag, why bleach on drywall is theatre, and the two moves in the first two days that decide the rest of the room's life.",
  """<p>Mould after a flood is not a cleaning job; it's a race - the first forty-eight hours belong to you, after that the wall chooses. Everything on this page is boring on purpose, because the proven wins here are dehumidifiers, plastic sheeting and judgement calls about what is porous.</p>
<h2>The two moves that come before scrubbing</h2>
<p>One: stop the source. A "cleaned" ceiling above an unsealed roof sheet is a cleaning subscription. Two: get the room <em>dry with force</em> - cross-draft fans, any dehumidifier you can borrow, nothing left damp for the weather to finish the job the flood started. Within 48 hours of wetting, most materials are recoverable; beyond it, porous ones are already colonised. Rush the drying; delay the cosmetics.</p>
<h2>Keep, bin, or cut: the honest rule</h2>
<ul><li><b>Bin list, no debate:</b> anything porous that was under floodwater - mattresses, upholstered furniture that absorbed it, carpet underlay, compressed-board furniture that swelled, any ceiling tile. Floodwater is not rain; what it carried into foam is why the bin is the answer. Seal each item in its own bag on the way out of the room - mould dry-scraped off a mattress is the spore cloud that becomes your lungs.</li>
<li><b>Keep list:</b> solid timber (scrub, then dry slowly out of sun), metal, glass, hard plastics, and concrete block - all cleanable once the water they met was clean-ish. Salvageable with work: rugs and clothing that met <em>rain</em> water, washed hot within the day.</li>
<li><b>The cut line for drywall/plasterboard:</b> board that wicked water above 300 mm from the floor, or that sounds hollow and soft, doesn't dry "back to new" - it dries as a sandwich with a damp core. The professional rule the pros actually follow: cut out affected board <em>up to a line about 300 mm above the highest tide mark</em>, bag from the room, and leave the cavity open and blowing air until everything behind your cut is measurably dry. Patching paint over wet board is how a clean-up becomes a re-build.</li></ul>
<h2>Bleach is theatre on the wrong surface</h2>
<p>On tile, glass and sealed metal: dilute household bleach, scrub, rinse, dry - fine. On plasterboard, wood or grout behind furniture, bleach mostly delivers water to a porous surface while the smell theatrically announces "done" - roots of mould below paint survive spraying. What actually works on surfaces is: HEPA-vacuum dry growth first, scrub with detergent solution, dry thoroughly, then and only then decide whether paint is the last step of dryness, not the first lie. Wear an N95 and gloves for all of it; seal the room off from the house with a taped plastic sheet in the doorway, and if the affected area is bigger than roughly a square metre of wall, that's the size where professional remediation pays for itself in not breathing your own repair.</p>
<h2>The week after: keep it from returning</h2>
<p>Furniture off walls, wardrobes angled to breathe (the corner of a built-in against an external wall is this country's favourite mould colony), bathroom door open after every bath, kitchen extraction while cooking, and the humidity gauge you can buy cheaply learning to read 60 percent in a tropical ground floor as "act now, not smell later." A flooded room that stays mould-free is won with airflow for the rest of its life, not with the one bottle of anti-mould wash. This desk's boundary, stated plainly: structural cracks, sewage water at any scale, and any room where your family includes an asthma attack or a compromised immune system - those start at the professional, not the checklist.</p>"""),
]
