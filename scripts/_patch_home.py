"""Phase 4 patch: BRYME Home & DIY goes from foundation to a real publication."""
import ast
from pathlib import Path

p = Path("scripts/build-ecosystem.py")
t = p.read_text()

HOME_CODE = '''
# ------------------------------------------------------------------ 6. HOME & DIY
HOME_CHECK = [
    ("Water & drainage", "Run water in every unused sink, shower and floor drain",
     "Traps dry out and let sewer smells back in. A jug of water a month keeps the seal."),
    ("Water & drainage", "Look inside the cabinets under your sinks",
     "Damp rings, swollen board or a slow drip caught early is a five-minute fix, not a flood."),
    ("Safety devices", "Press the test button on your RCD / GFCI outlets",
     "The button exists so you can prove the protection works. If it does not trip, get it checked."),
    ("Safety devices", "Test your smoke alarms",
     "Fire services recommend testing monthly. Press the button; replace batteries on the schedule the maker states."),
    ("Safety devices", "Check the torch you keep for power cuts",
     "Batteries die quietly. Give it thirty seconds of light now, not darkness later."),
    ("Appliances", "Clean the coils behind or under your refrigerator",
     "Dust on coils makes the compressor work harder and run hotter. Unplug first, brush gently."),
    ("Appliances", "Inspect the washing machine hoses",
     "Bulges, cracks or weeping fittings on rubber hoses are how laundry rooms flood. Makers commonly advise replacing ageing hoses before they fail."),
    ("Appliances", "Descale the kettle and coffee machine",
     "Wherever water is hard, scale shortens appliance life and ruins the taste. Your maker\\u2019s descaling guide beats any hack."),
    ("Seals & airflow", "Walk the windows and doors",
     "Daylight around a closed door or cracked sealant means lost heat/cooling and moisture where you do not want it."),
    ("Seals & airflow", "Vacuum vents, radiators and the dryer\\u2019s full lint path",
     "Dryer lint beyond the filter is a known fire risk; blocked vents make everything work harder."),
]

HOME_SOURCES = [
    ("NFPA \\u2014 smoke alarm safety (testing guidance)", "https://www.nfpa.org/education-and-research/home-fire-safety/smoke-alarms"),
    ("U.S. Fire Administration \\u2014 dryer fire safety", "https://www.usfa.fema.gov/prevention/home-fires/prevent-hfires/dryers/"),
]

HOME_ARTICLES = [
    ("how-to-fix-a-slow-draining-sink",
     "How to fix a slow-draining sink, honestly",
     "What actually clears a slow sink (in order of effort), what is mostly theatre, and the point at which a plumber earns their fee.",
     """<p>A slow sink is almost always a partial blockage in the trap or the first metre of pipe: hair, soap, fat, or the slow accretion of all three. You rarely need chemicals and you never need panic. Work down this list and stop when the water runs.</p>
<h2>First: the honest physics</h2>
<p>Drain cleaners and home remedies get marketed hard. The honest order of effectiveness for a slow (not fully blocked) sink is mechanical: physically removing the gunk beats dissolving it, and dissolving beats hoping. Hot water alone is theatre for a genuine soap-fat clog, though it helps flush a cleared pipe.</p>
<h2>Step 1: the plunger, properly</h2>
<p>Block the overflow opening with a wet cloth (a basin has a small hole near the top; cover it or the plunger\\u2019s pressure escapes there). Add enough water to cover the plunger\\u2019s cup. Push and pull sharply for twenty to thirty seconds. Most slow sinks end here.</p>
<h2>Step 2: open the trap</h2>
<p>Under the sink is the U-bend (P-trap). Put a bucket under it, hand-loosen the slip nuts, and lift the trap off. Empty it. What you find inside is usually the entire story \\u2014 a compacted plug of hair and soap. Rinse both directions, refit hand-tight, run hot water and check for drips before closing the cabinet. If the pipe from the wall also holds gunk, a plastic hand-crank drain snake costs little and reaches where fingers cannot.</p>
<h2>What about baking soda and vinegar?</h2>
<p>The famous fizz is mostly theatre for real blockages \\u2014 it is a mild reaction, not a solvent. It will not harm anything, and it can freshen a smelly (rather than slow) drain, but do not let it replace the plunger and the trap.</p>
<h2>Chemicals: the safety boundary</h2>
<p>If you do use a caustic drain cleaner, follow the label exactly, ventilate, and never mix products \\u2014 especially anything containing bleach with anything containing ammonia or acid; the reaction gases are genuinely dangerous. Chemicals also sit in the pipe, waiting for whoever opens the trap next. That is why this guide puts chemicals last, if at all.</p>
<h2>Call a plumber when</h2>
<p>Several fixtures drain slowly at once (the blockage is downstream, often in the main drain), water comes up in a different fixture when another drains, or the trap will not come apart because fittings are corroded or glued. Also call if there is sewage smell that a water top-up does not fix \\u2014 a dried trap is a jug of water; a broken vent or seal is a professional.</p>
<h2>Prevention</h2>
<p>A mesh screen over the plug hole, fat into a jar rather than the sink, and a monthly kettle\\u2019s worth of hot water down each drain. Three habits; zero emergencies. The <a href="/seasonal-home-maintenance-checklist/">once-a-season home checklist</a> includes the drain top-up.</p>"""),
    ("how-to-fix-a-dripping-tap",
     "A dripping tap (faucet), and what you can honestly fix yourself",
     "Why taps drip, the washer-and-cartridge reality behind most of them, and the ten-minute test that tells you whether it is your job or a plumber\\u2019s.",
     """<p>A tap that drips once a second wastes more water over a month than most people expect, and the sound has driven stronger people than you to madness. The good news: the majority of dripping taps are a small, cheap, mechanical fix \\u2014 provided you can turn the water off and tell the difference between the two most common tap insides.</p>
<h2>Before anything: the isolation test</h2>
<p>Find the shut-off valve for that tap (under the sink in most homes) and close it, or close the main if there is none. Open the tap to confirm the flow has stopped. No isolation valve and no main you can find? That is the professional\\u2019s first visit, not yours.</p>
<h2>What kind of tap is it?</h2>
<p>Two families dominate. Traditional taps with a spindle you turn several times usually seal with a rubber washer and a seat \\u2014 dripping when off, usually the washer. Modern single-lever or quarter-turn taps usually seal with a ceramic cartridge \\u2014 dripping or failing to shut smoothly, usually the cartridge. Brand matters for parts: open nothing until you know the make, or plan to take the old part to a hardware shop as the specimen.</p>
<h2>The washer job, in one honest paragraph</h2>
<p>With water off: prise the decorative cap, unscrew the handle, unscrew the spindle with an adjustable spanner, and look at the end \\u2014 a squashed, grooved or torn rubber washer is your culprit. Replace it with an identical size (take the old one shopping), check the seat it presses against is not scored, reassemble in reverse, reopen the water slowly. Ten to twenty minutes the first time.</p>
<h2>The cartridge job</h2>
<p>Same isolation, then the retaining clip or nut holds the cartridge. Cartridges are brand-specific parts \\u2014 photograph the tap and its brand before buying. They swap in minutes once you hold the right part, and they are usually the only part that ever needs replacing on those taps.</p>
<h2>When it is not your job</h2>
<p>Water weeping from the tap body itself, corrosion that will not let fittings separate, no way to isolate the supply, or anything involving the pipes inside the wall: that is a plumber\\u2019s territory. Paying for an hour of plumbing is cheaper than a flooded cabinet \\u2014 see <a href="/how-to-fix-a-slow-draining-sink/">what lives inside sink cabinets</a> when they stay damp.</p>
<h2>Prevention, such as it is</h2>
<p>Taps wear from use, not neglect. What you can prevent is the collateral: close taps firmly but never forced \\u2014 over-tightening chews washers faster. And once a season, glance at every tap\\u2019s isolation valve; a valve that has not moved in years is the one that will seize. It is on the <a href="/seasonal-home-maintenance-checklist/">seasonal checklist</a>.</p>"""),
    ("why-does-my-circuit-breaker-keep-tripping",
     "Why your circuit breaker keeps tripping \\u2014 and where DIY must stop",
     "What breakers actually protect you from, the safe way to narrow down the cause, and the hard boundary that separates a homeowner from an electrician.",
     """<p>A tripping breaker is not a malfunction. It is your electrical panel doing exactly its job: cutting power when the circuit is asked to carry more current than is safe, or when it detects a leak of current to earth. The nuisance is the clue. Read it correctly and it is one of the most useful signals in your home.</p>
<h2>The three usual causes</h2>
<p>Overload: too many things drawing power on one circuit \\u2014 the kettle, heater and iron sharing one socket circuit, say. Short circuit: live and neutral touching somewhere they should not, often a damaged appliance, cable or plug \\u2014 the trip is instant. Earth leak (the RCD/GFCI part of the protection): current escaping along a path it should not, often moisture or a failing appliance \\u2014 these trips feel random and are the ones you must never ignore, because that protection exists to stop shocks.</p>
<h2>The safe way to narrow it down</h2>
<p>Unplug everything on the dead circuit. Reset the breaker firmly. If it holds: plug items back in one at a time, with a pause between each \\u2014 the item that trips it again has named itself; retire or repair it. If it trips immediately with nothing plugged in, or trips repeatedly with everything unplugged, stop there. That is wiring, not appliances, and it is not a homeowner diagnosis.</p>
<h2>The reset, done properly</h2>
<p>Breakers trip to OFF or to a middle position. Push fully to OFF first, then to ON \\u2014 resetting from the middle position is the classic reason a breaker \\u201cwill not reset\\u201d. One or two resets to diagnose is normal. A breaker you find yourself resetting weekly is telling you something is wrong; solving that by resetting harder is how problems escalate.</p>
<h2>The hard boundary</h2>
<p>Resetting a breaker and unplugging appliances: homeowner territory, do it today. Everything else \\u2014 panel work, adding circuits, repeated trips with no load, burning smells, warm outlets, any work behind sockets \\u2014 belongs to a qualified electrician. This page is general information, not electrical advice, and it deliberately stops at the panel cover. Electricity does not give second chances.</p>
<h2>Where this fits the house</h2>
<p>The <a href="/seasonal-home-maintenance-checklist/">once-a-season checklist</a> includes testing RCD/GFCI outlets and smoke alarms \\u2014 the thirty seconds that prove the protective parts of your home still work.</p>"""),
    ("how-to-clean-a-washing-machine",
     "How to clean a washing machine (including the parts that actually cause the smell)",
     "Why machines smell and mark laundry, the gasket-and-filter truth behind it, and a maintenance rhythm that prevents both.",
     """<p>A washing machine that smells damp, or marks clean clothes with grey streaks, is not broken. It is dirty in the three specific places detergent residue and water sit long enough to grow things: the door gasket, the detergent drawer, and the filter. Cleaning those beats every scented product marketed to mask the problem.</p>
<h2>The gasket is the crime scene</h2>
<p>On front loaders, fold back the rubber door gasket and look: black speckles, slime, the odd lost sock. Wipe it out with a cloth and warm soapy water, getting into the folds. Leave the door and drawer ajar between washes so the inside dries \\u2014 sealed-in moisture is what grows the smell in the first place.</p>
<h2>The detergent drawer slides out</h2>
<p>Most drawers release fully with a press of a recessed clip (your manual shows where, or the internet knows your model). Wash it under the tap with an old toothbrush; check the jet holes above where it sits and clear the residue that blocks rinse water.</p>
<h2>The filter you have been avoiding</h2>
<p>Behind a small hatch near the floor lives the drain filter \\u2014 the place coins, hair clips and lint go to retire. Put a shallow tray or towel down, open it slowly (water will come), remove and rinse the filter, and screw it back snugly. Once a season is the honest rhythm; more if you have pets or small humans.</p>
<h2>Hot wash, occasionally</h2>
<p>Cold-wash habits let grease and residue accumulate. A monthly hot cycle \\u2014 empty, with a maker-approved cleaner or plain washing soda per its instructions \\u2014 flushes the tub and the pipes behind it. Skip the folk chemistry; heat does the work.</p>
<h2>Prevention rhythm</h2>
<p>Door ajar after washes; drawer ajar; filter each season; a monthly hot cycle; and measure detergent honestly \\u2014 most people use far more than the machine needs, and the surplus is what rots. All of this except the hot cycle is on the <a href="/seasonal-home-maintenance-checklist/">once-a-season checklist</a>.</p>"""),
    ("fridge-not-cold-enough",
     "Fridge not cold enough? Five checks before you pay for a repair",
     "The settings, airflow and coil checks that fix most \\u201cwarm fridge\\u201d calls, and the signs that say it really is a technician\\u2019s problem.",
     """<p>A fridge that runs but does not quite cool is one of the most common \\u201crepair\\u201d calls \\u2014 and a decent share of them are fixed in ten minutes with no parts. Work these checks in order; stop and call a technician the moment the path says so.</p>
<h2>1. The thermostat, honestly</h2>
<p>Dials marked 1\\u20135 say nothing absolute; the manual says which end is colder. Confirm the setting first \\u2014 dials get nudged by grocery bags. A fridge thermometer (cheap, honest) beats any built-in dial: you want roughly at or below 4\\u00b0C / 40\\u00b0F on the shelf, freezer around \\u201318\\u00b0C / 0\\u00b0F.</p>
<h2>2. Airflow inside</h2>
<p>Cold air travels through vents between freezer and fridge. Boxes jammed against the back wall and vents blocked by a bag of peas mimic a failing fridge. Create space; let air move.</p>
<h2>3. The door seal test</h2>
<p>Close the door on a piece of paper; if it slides out with no resistance at several points, the gasket is not sealing and cold air leaks out. Clean sticky residue off the gasket; a perished or torn one is a replaceable part on most models \\u2014 cheaper than a new fridge.</p>
<h2>4. The coils you never see</h2>
<p>Unplug the fridge, find the coils (behind the kick plate or on the back), and brush/vacuum the dust blanket off. Coils choked with dust shed heat poorly and the cabinet warms. This is the single most common neglected maintenance on kitchen appliances \\u2014 it is on the <a href="/seasonal-home-maintenance-checklist/">seasonal checklist</a> for that reason.</p>
<h2>5. Give it time, then listen</h2>
<p>After any change, give the fridge several hours with the door kept closed. Then listen: a compressor that clicks on and off every few minutes, or hums constantly without cooling, is failing \\u2014 and that, along with frost patterns that suggest a defrost-system fault, is genuinely a technician\\u2019s job. Refrigerant and sealed systems are not DIY, full stop.</p>
<h2>When you call, say this</h2>
<p>\\u201cCompressor runs continuously, cabinet at 10\\u00b0C, coils cleaned, seal tested\\u201d gets a better visit than \\u201cit\\u2019s warm\\u201d \\u2014 and sometimes a better answer: knowing the checks were done may save you the call-out entirely.</p>"""),
]

def home_pages():
    import json as _j
    def src_html(sources):
        if not sources:
            return ""
        return ('<h2>Sources</h2><ul class="list">'
                + "".join('<li><a href="' + u + '" rel="noopener">' + n + "</a></li>" for n, u in sources)
                + "</ul>")

    def band(text):
        return ('<section class="section alt" style="border-left:4px solid var(--brand)"><div class="wrap"><p class="lede">'
                + text + "</p></div></section>")

    SAFETY_BAND = band("<b>Safety boundary.</b> Electrical panel work, gas, structural changes and anything at height belong to qualified professionals. Every guide here stops where that line starts.")
    DISCLAIMER = band("<b>General information, not professional advice.</b> Homes differ \\u2014 if a job is beyond your confidence or the guide\\u2019s boundary, that is what tradespeople are for.")

    def art(slug, title, dek, body_html, sources, related):
        rel_html = "".join('<li><a href="/' + s + '/">' + rt + "</a></li>" for s, rt in related)
        schema = {"@context": "https://schema.org", "@type": "Article",
                  "headline": title,
                  "author": {"@type": "Organization", "name": "BRYME Home & DIY desk"},
                  "publisher": {"@type": "Organization", "name": "THE BRYME"},
                  "datePublished": TODAY, "dateModified": TODAY,
                  "mainEntityOfPage": ORIGIN + "/home/" + slug + "/",
                  "description": dek}
        abody = (head("home", "Practical help for fixing, maintaining and understanding your home.")
            + '<main id="main"><div class="wrap">'
            + '<nav class="crumb"><a href="/home/">Home & DIY</a> / ' + html.escape(title) + "</nav>"
            + '<section class="cover"><p class="kicker">Low-risk help \\u00b7 boundaries stated \\u00b7 no theatre</p>'
            + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">' + html.escape(title) + "</h1>"
            + '<p class="byline">BRYME Home & DIY desk \\u00b7 reviewed ' + TODAY + " \\u00b7 general information, not professional advice</p></section>"
            + '<section class="section alt"><div class="wrap"><p class="lede"><b>In one line:</b> ' + html.escape(dek) + "</p></div></section>"
            + '<section class="section"><div class="prose">' + body_html + src_html(sources) + "</div></section>"
            + '<section class="section alt"><div class="section-head"><p class="kicker">Next</p><h2>Related on this desk.</h2></div>'
            + '<ul class="list">' + rel_html + "</ul>"
            + '<div class="actions"><a class="btn secondary" href="/home/">All of BRYME Home & DIY</a></div></section>'
            + DISCLAIMER
            + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
            + "</div></main>" + foot("home"))
        return (("/" + slug + "/"), title + " | BRYME Home & DIY", dek[:155], abody)

    related_map = {
        "how-to-fix-a-slow-draining-sink": [("how-to-fix-a-dripping-tap", "A dripping tap, fixed honestly"),
                                            ("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                            ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "how-to-fix-a-dripping-tap": [("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                                      ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker"),
                                      ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "why-does-my-circuit-breaker-keep-tripping": [("seasonal-home-maintenance-checklist", "The once-a-season checklist"),
                                                      ("fridge-not-cold-enough", "Fridge not cold enough"),
                                                      ("how-to-fix-a-dripping-tap", "A dripping tap, fixed honestly")],
        "how-to-clean-a-washing-machine": [("fridge-not-cold-enough", "Fridge not cold enough"),
                                           ("how-to-fix-a-slow-draining-sink", "The slow-draining sink"),
                                           ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
        "fridge-not-cold-enough": [("how-to-clean-a-washing-machine", "Why the washing machine smells"),
                                   ("why-does-my-circuit-breaker-keep-tripping", "The tripping breaker"),
                                   ("seasonal-home-maintenance-checklist", "The once-a-season checklist")],
    }

    # ---- the seasonal checklist (the product) ----
    groups = []
    seen = []
    for g, task, why in HOME_CHECK:
        if g not in seen:
            seen.append(g)
    cur = ""
    items = ""
    n = 0
    for g, task, why in HOME_CHECK:
        if g != cur:
            if items:
                groups.append((cur, items))
            cur = g
            items = ""
        n += 1
        items += ('<li class="fp-day" data-item="' + html.escape(task[:40]) + '">'
                  '<span class="fp-num">' + str(n) + "</span>"
                  "<span><b>" + html.escape(task) + "</b><small>" + html.escape(why) + "</small></span>"
                  '<button type="button" class="btn secondary fp-done" aria-pressed="false">Done</button></li>')
    if items:
        groups.append((cur, items))
    weeks_html = "".join(
        '<section class="section"><div class="section-head"><p class="kicker">The checks</p><h2>' + html.escape(g) + '</h2></div>'
        + '<ul class="list fp-week">' + rows + "</ul></section>" for g, rows in groups)
    import json as _j
    schema = {"@context": "https://schema.org", "@type": "Article",
              "headline": "The Once-a-Season Home Checklist",
              "author": {"@type": "Organization", "name": "BRYME Home & DIY desk"},
              "publisher": {"@type": "Organization", "name": "THE BRYME"},
              "datePublished": TODAY, "dateModified": TODAY,
              "mainEntityOfPage": ORIGIN + "/home/seasonal-home-maintenance-checklist/",
              "description": "A short, season-proof home maintenance checklist \\u2014 water, safety devices, appliances, seals and airflow \\u2014 with progress saved in your browser."}
    plan_body = (head("home", "Practical help for fixing, maintaining and understanding your home.")
        + '<main id="main"><div class="wrap">'
        + '<nav class="crumb"><a href="/home/">Home & DIY</a> / The Once-a-Season Checklist</nav>'
        + '<section class="cover"><p class="kicker">Preventive maintenance \\u00b7 season-proof \\u00b7 no hemisphere assumptions</p>'
        + '<h1 class="cover-title" style="font-size:clamp(30px,4.6vw,48px)">The Once-a-Season Home Checklist</h1>'
        + '<p class="byline">BRYME Home & DIY desk \\u00b7 reviewed ' + TODAY + " \\u00b7 general information, not professional advice</p></section>"
        + '<section class="section alt"><div class="wrap"><p class="lede"><b>One honest idea:</b> homes fail slowly, then suddenly. A short list of checks every season \\u2014 whatever \\u201cseason\\u201d means where you live \\u2014 catches the slow failures while they are still cheap. Progress is saved in your browser: no account, nothing sent anywhere.</p></div></section>'
        + '<section class="section"><div class="wrap"><div class="fp-progressbar" role="img" aria-label="Checklist progress"><div class="fp-fill" id="fp-fill"></div></div>'
        + '<p class="lede" id="fp-status">Nothing ticked yet. Tick items as you do them \\u2014 your browser will remember.</p></div></section>'
        + weeks_html
        + '<section class="section"><div class="section-head"><p class="kicker">Boundaries</p><h2>What is deliberately not on this list.</h2></div>'
        + '<div class="prose"><p>Nothing on this checklist asks you near an electrical panel, a gas supply, a roof or a structure. Those are the qualified professional\\u2019s territory \\u2014 the checklist proves your protective devices work, and their visit proves the rest does. If any check reveals damage you cannot see the edge of, stop and get it assessed.</p></div></section>'
        + '<section class="section alt">' + src_html(HOME_SOURCES) + "</section>"
        + '<script type="application/json" id="fit-plan-data">{"total": ' + str(len(HOME_CHECK)) + "}</script>"
        + '<script src="/assets/home-checklist.js" defer></script>'
        + '<script type="application/ld+json">' + _j.dumps(schema) + "</script>"
        + "</div></main>" + foot("home"))
    plan_page = [("/seasonal-home-maintenance-checklist/", "The Once-a-Season Home Checklist | BRYME Home & DIY",
                  "A short, season-proof home maintenance checklist \\u2014 water, safety devices, appliances, seals, airflow \\u2014 with progress saved in your browser.", plan_body)]

    arts = [art(s, ti, dek, b, [], related_map[s])
            for (s, ti, dek, b) in HOME_ARTICLES]

    fix_rows = ('<li><a href="/how-to-fix-a-slow-draining-sink/"><span><b>How to fix a slow-draining sink</b>'
                "<small>Plunger, trap, and the honest ranking of everything else \\u2014 chemicals last, if at all.</small></span>"
                '<span class="meta">Fix it</span></a></li>'
                '<li><a href="/how-to-fix-a-dripping-tap/"><span><b>A dripping tap (faucet)</b>'
                "<small>Washer or cartridge \\u2014 the ten-minute test that tells you which, and when to stop.</small></span>"
                '<span class="meta">Fix it</span></a></li>')
    understand_rows = ('<li><a href="/why-does-my-circuit-breaker-keep-tripping/"><span><b>Why the breaker keeps tripping</b>'
                       "<small>Overload, short or earth leak \\u2014 read the clue safely, and know the hard boundary.</small></span>"
                       '<span class="meta">Understand it</span></a></li>'
                       '<li><a href="/fridge-not-cold-enough/"><span><b>Fridge not cold enough</b>'
                       "<small>Five checks before you pay for a repair \\u2014 and the words that make the technician\\u2019s visit count.</small></span>"
                       '<span class="meta">Understand it</span></a></li>'
                       '<li><a href="/how-to-clean-a-washing-machine/"><span><b>Why the washing machine smells</b>'
                       "<small>Gasket, drawer, filter \\u2014 the three places smell actually lives, and the rhythm that prevents it.</small></span>"
                       '<span class="meta">Clean & maintain</span></a></li>')
    index_body = (head("home", "Practical help for fixing, maintaining and understanding your home.")
        + '<main id="main"><div class="wrap">'
        + '<section class="cover"><p class="kicker">BRYME Home & DIY</p>'
        + '<h1 class="cover-title">Fix it. Clean it. Maintain it. Understand it.</h1>'
        + '<p class="cover-dek">Practical help for the problems every household hits \\u2014 written for low-risk work, with the boundaries stated plainly: electrical panels, gas, structure and height belong to qualified professionals, and every guide here says exactly where that line is.</p></section>'
        + '<section class="section"><div class="section-head"><p class="kicker">The product</p><h2>The once-a-season checklist.</h2></div>'
        + '<div class="prose"><p><a href="/seasonal-home-maintenance-checklist/"><b>The once-a-season home checklist</b></a> \\u2014 eleven checks across water, safety devices, appliances and airflow, with progress your browser remembers. Homes fail slowly, then suddenly; this catches the slow part.</p></div></section>'
        + '<section class="section alt"><div class="section-head"><p class="kicker">Fix it</p><h2>Problems you can honestly fix yourself.</h2></div>'
        + '<ul class="list">' + fix_rows + "</ul></section>"
        + '<section class="section"><div class="section-head"><p class="kicker">Understand & maintain</p><h2>What the symptoms mean.</h2></div>'
        + '<ul class="list">' + understand_rows + "</ul></section>"
        + SAFETY_BAND.replace('<section class="section alt"', '<section class="section"').replace('border-left:4px solid var(--brand)', '')
        + "</div></main>" + foot("home"))
    pages = [("/", "BRYME Home & DIY \\u2014 fix, clean, maintain, understand",
              "Low-risk home repairs and maintenance, honestly explained: the slow sink, the dripping tap, the tripping breaker, and the once-a-season checklist with in-browser progress.", index_body)]
    pages.extend(plan_page)
    pages.extend(arts)
    return pages + legal_pages("home", "BRYME Home & DIY", "Practical help for fixing, maintaining, improving and understanding your home \\u2014 safe, low-risk guidance with clear professional boundaries.")


'''

# 1. insert before main()
i = t.index("\ndef main()")
t = t[:i] + "\n" + HOME_CODE + t[i:]

# 2. swap placeholder for service
o = '''    write_placeholder("home", "BRYME Home & DIY",
        "Practical help for fixing, maintaining, improving and understanding your home.",
        "BRYME Home & DIY will answer the questions every household hits: why is this not working, how do I maintain it, and can I fix it myself? Low-risk practical problems first \\u2014 and clear, non-negotiable safety boundaries: electrical, gas and structural work belongs to qualified professionals.",
        ["Fix it \\u2014 household problems and beginner repairs",
         "Clean it \\u2014 cleaning and maintenance that actually works",
         "Maintain it \\u2014 preventive home maintenance, season by season",
         "Understand it \\u2014 appliance symbols, noises and questions",
         "Improve it \\u2014 organisation and safe DIY projects"])
'''
assert t.count(o) == 1
t = t.replace(o, '    write_service("home", home_pages())\n')

# 3. PREFIX gains home
o = 'PREFIX = {"sports": "/sports", "entertainment": "/entertainment", "tech": "/tech", "fitness": "/fitness"}'
assert t.count(o) == 1
t = t.replace(o, 'PREFIX = {"sports": "/sports", "entertainment": "/entertainment", "tech": "/tech", "fitness": "/fitness", "home": "/home"}')

# 4. (placeholder call removed wholesale; its body goes with it)

# 4. hub: five live publications
o = '("home", "BRYME Home & DIY", "Foundation laid.", "Practical help for fixing, maintaining, improving and understanding your home \\u2014 fix it, clean it, maintain it, understand it. Safe, low-risk guidance first; dangerous work belongs to qualified professionals. The first guides are being built now.", "foundation"),'
assert t.count(o) == 1
t = t.replace(o, '("home", "BRYME Home & DIY", "Now open.", "Practical help for fixing, maintaining and understanding your home \\u2014 low-risk repairs explained honestly, an in-browser seasonal checklist, and safety boundaries stated without apology.", "live"),')
o = 'Four publications. One house standard.'
assert t.count(o) == 1
t = t.replace(o, 'Five publications. One house standard.')
o = "One standard, four voices."
assert t.count(o) == 1
t = t.replace(o, "One standard, five voices.")

ast.parse(t)
p.write_text(t)
print("build-ecosystem.py: home build patched")
