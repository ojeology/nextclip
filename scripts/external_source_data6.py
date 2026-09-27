# -*- coding: utf-8 -*-
"""External source notes, part 6: BRYME Home & DIY desk, step 2 (68 pages).
Every URL curl-verified 200 at authoring time."""

NFPA = "https://www.nfpa.org/"
USFA = "https://www.usfa.fema.gov/"
EPA = "https://www.epa.gov/"
WHO = "https://www.who.int/"
EIA = "https://www.eia.gov/"
ENERGY = "https://www.energy.gov/"
NEMA = "https://www.nema.org/"
UL = "https://www.ul.com/"
ICC = "https://www.iccsafe.org/"
SON = "https://son.gov.ng/"
MEDLINE = "https://medlineplus.gov/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

EXTERNAL_SOURCES6 = {

"home/ac-outdoor-unit-care":
    "<p><b>The outdoor unit does the rejecting.</b> A condenser that cannot shed heat makes the whole system work harder, and the <a href=\"" + _w("air+conditioning") + "\" rel=\"noopener\">air-conditioning reference material on Wikipedia</a> explains the cycle. The <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the maintenance guidance behind the desk's cleaning interval.</p>",

"home/ants-in-the-kitchen":
    "<p><b>Trail behaviour explains why sprays fail.</b> Ants forage along pheromone trails back to a nest, and the <a href=\"" + _w("ant") + "\" rel=\"noopener\">ant reference material on Wikipedia</a> explains the colony behaviour that makes killing visible workers ineffective. The desk's protocol targets the source, which is why it is slower and works.</p>",

"home/appliances-that-use-the-most-electricity":
    "<p><b>Consumption data, from the statistical authority.</b> The <a href=\"" + EIA + "\" rel=\"noopener\">U.S. Energy Information Administration</a> publishes the household end-use consumption figures this ranking is built from, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the efficiency guidance. Heating and cooling dominate almost everywhere, which is why the desk's list starts there.</p>",

"home/autumn-home-preparation":
    "<p><b>One month decides the winter.</b> The checklist follows the published efficiency and moisture guidance from the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a>, and the mould and ventilation side from the <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a>. The desk's ordering is by consequence: a blocked gutter in October is a damp ceiling in February.</p>",

"home/basic-toolkit-checklist":
    "<p><b>A short list, chosen by failure frequency.</b> The desk's toolkit is the set that covers most household repairs, and the <a href=\"" + _w("hand+tool") + "\" rel=\"noopener\">hand-tool reference material on Wikipedia</a> describes the categories. Certified electrical products carry marks from bodies such as <a href=\"" + UL + "\" rel=\"noopener\">UL Solutions</a> and, in Nigeria, the <a href=\"" + SON + "\" rel=\"noopener\">Standards Organisation of Nigeria</a>.</p>",

"home/bathroom-fan-condensation":
    "<p><b>Condensation is a ventilation problem.</b> The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the indoor-moisture and mould guidance this page follows, and the <a href=\"" + _w("relative+humidity") + "\" rel=\"noopener\">relative-humidity reference material on Wikipedia</a> explains why a warm wet room deposits water on cold surfaces. The desk's fix order is airflow first, then surfaces.</p>",

"home/best-water-softener-for-your-home":
    "<p><b>Softening is an ion-exchange process.</b> What a softener removes and what it adds is described in the <a href=\"" + _w("water+softening") + "\" rel=\"noopener\">water-softening reference material on Wikipedia</a>, which is why the desk insists on a hardness test before any purchase. The honest cost is salt, maintenance and the sodium the process introduces.</p>",

"home/boiler-pressure-low-or-high":
    "<p><b>The gauge is telling you about the sealed system.</b> Pressure changes come from the expansion vessel, leaks or air, and the <a href=\"" + _w("boiler") + "\" rel=\"noopener\">boiler reference material on Wikipedia</a> describes the components. The desk's rule is the safety one: repressurise only within the manufacturer's stated range, and stop if the gauge climbs again on its own.</p>",

"home/ceiling-fan-direction-summer-winter":
    "<p><b>Direction changes what the fan is for.</b> Down-draught creates a cooling breeze on skin; up-draught redistributes warm air pooled at the ceiling, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the guidance on both. The <a href=\"" + _w("ceiling+fan") + "\" rel=\"noopener\">ceiling-fan reference material on Wikipedia</a> explains why the effect differs — a fan cools people, not rooms.</p>",

"home/ceiling-fan-vs-standing-fan":
    "<p><b>Different jobs, and a measurable difference in cost.</b> Fan energy use is published by the <a href=\"" + EIA + "\" rel=\"noopener\">Energy Information Administration</a> in its household consumption data, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> covers the cooling guidance. The desk's room-by-room answer turns on airflow reach, which is the variable nobody puts on the box.</p>",

"home/cost-to-charge-an-ev-at-home":
    "<p><b>Per-mile cost is arithmetic, not opinion.</b> Battery capacity, efficiency and your tariff produce the figure, and the <a href=\"" + EIA + "\" rel=\"noopener\">Energy Information Administration</a> publishes the electricity price series the desk uses. The <a href=\"" + _w("electric+vehicle") + "\" rel=\"noopener\">electric-vehicle reference material on Wikipedia</a> covers the consumption figures behind the calculation.</p>",

"home/cost-to-run-a-dehumidifier":
    "<p><b>Compare it against the problem it solves.</b> Running cost comes from wattage and hours, using the price data published by the <a href=\"" + EIA + "\" rel=\"noopener\">Energy Information Administration</a>, and the <a href=\"" + _w("dehumidifier") + "\" rel=\"noopener\">dehumidifier reference material on Wikipedia</a> explains the extraction rates. The <a href=\"" + EPA + "\" rel=\"noopener\">EPA's</a> moisture guidance is what decides whether you need one at all.</p>",

"home/cost-to-run-a-dishwasher":
    "<p><b>Per cycle, with the water and the power counted.</b> Appliance energy use is published by the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a>, and the <a href=\"" + _w("dishwasher") + "\" rel=\"noopener\">dishwasher reference material on Wikipedia</a> covers the cycle types that change the figure. The desk's comparison against washing up includes the heated water, which is the half most comparisons omit.</p>",

"home/cost-to-run-a-fan":
    "<p><b>The cheapest comfort there is.</b> A fan's draw is tens of watts, and the <a href=\"" + EIA + "\" rel=\"noopener\">Energy Information Administration</a>'s consumption and price data produce the yearly figure the desk prints. The honest caveat from the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a>: a fan cools people, so running one in an empty room buys nothing.</p>",

"home/cost-to-run-a-gaming-pc":
    "<p><b>Load matters more than the sticker.</b> A graphics card's draw varies enormously between idle and play, and the <a href=\"" + EIA + "\" rel=\"noopener\">Energy Information Administration</a>'s price data turns that into a monthly figure. The <a href=\"" + _w("power+supply+unit+(computer)") + "\" rel=\"noopener\">power-supply reference material on Wikipedia</a> explains why the rated wattage is not the consumption.</p>",

"home/cost-to-run-a-hot-tub":
    "<p><b>Heating water and holding it there.</b> The dominant cost is maintaining temperature, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the guidance on insulation and covers that reduces it. The <a href=\"" + _w("hot+tub") + "\" rel=\"noopener\">hot-tub reference material on Wikipedia</a> covers the volume and heating arithmetic behind the desk's monthly figure.</p>",

"home/cost-to-run-a-tumble-dryer":
    "<p><b>One of the hungriest appliances in the house.</b> Drying is thermal work, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the comparison between vented, condenser and heat-pump machines. The <a href=\"" + _w("clothes+dryer") + "\" rel=\"noopener\">clothes-dryer reference material on Wikipedia</a> explains why the heat-pump variant costs less to run and more to buy.</p>",

"home/door-lock-sticks-fix":
    "<p><b>Alignment before lubrication.</b> A sticking lock is usually a door that has moved, and the <a href=\"" + _w("lock+(security+device)") + "\" rel=\"noopener\">lock reference material on Wikipedia</a> describes the mechanism that binds when the strike plate is out of line. The desk's order — alignment, key condition, then lubricant — avoids the common mistake of oiling a misaligned lock.</p>",

"home/dryer-vent-cleaning-fire-risk":
    "<p><b>A documented and preventable fire cause.</b> The <a href=\"" + USFA + "\" rel=\"noopener\">U.S. Fire Administration</a> and the <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> both publish dryer-fire data and the cleaning guidance behind this page. The <a href=\"" + _w("clothes+dryer") + "\" rel=\"noopener\">clothes-dryer reference material on Wikipedia</a> explains why lint, which is fine fuel, accumulates exactly where the heat is.</p>",

"home/fridge-door-not-sealing":
    "<p><b>The seal is the whole efficiency story.</b> A leaking gasket makes the compressor run continuously, and the <a href=\"" + _w("refrigerator") + "\" rel=\"noopener\">refrigerator reference material on Wikipedia</a> describes the components. The desk's test is the paper test, and the fix is usually cleaning or replacing the gasket rather than any repair to the cooling system.</p>",

"home/fridge-not-cold-enough":
    "<p><b>Five checks before a technician.</b> Airflow, condenser cleanliness, door seal, thermostat setting and load are the usual causes, and the <a href=\"" + _w("refrigeration") + "\" rel=\"noopener\">refrigeration reference material on Wikipedia</a> explains the cycle each one disturbs. The desk's order is cheapest first, because the blocked air vent turns out to be the fault surprisingly often.</p>",

"home/fridge-temperature-setting":
    "<p><b>The number is a food-safety threshold.</b> Safe storage temperature is a documented figure, and the <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a>'s food-safety guidance is the desk's source for it. The <a href=\"" + _w("refrigerator") + "\" rel=\"noopener\">refrigerator reference material on Wikipedia</a> explains why the dial number means nothing until you measure with a thermometer.</p>",

"home/frozen-condensate-pipe-fix":
    "<p><b>A condensing boiler produces water that can freeze.</b> The condensate pipe carries acidic water out of the heat exchanger, and the <a href=\"" + _w("condensing+boiler") + "\" rel=\"noopener\">condensing-boiler reference material on Wikipedia</a> describes the mechanism. The desk's thawing order is gentle and external-first, and the page is explicit about what never to pour into the pipe.</p>",

"home/frozen-pipe-prevention":
    "<p><b>Water expands, and pipes lose.</b> The mechanism and the prevention methods are described in the <a href=\"" + _w("pipe+(fluid+conveyance)") + "\" rel=\"noopener\">piping reference material on Wikipedia</a>, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the insulation guidance behind the desk's checklist. Lagging is cheap; the burst it prevents is not.</p>",

"home/garage-door-spring-safety":
    "<p><b>The one repair to hand over.</b> Torsion springs store enough energy to cause serious injury, and the <a href=\"" + _w("garage+door+opener") + "\" rel=\"noopener\">garage-door reference material on Wikipedia</a> describes the mechanisms involved. The desk's position is unambiguous: everything else on the door is a DIY job, and the spring is not.</p>",

"home/gutter-guards-worth-it":
    "<p><b>Guards change the maintenance, they do not remove it.</b> How gutters fail and what blocks them is described in the <a href=\"" + _w("rain+gutter") + "\" rel=\"noopener\">rain-gutter reference material on Wikipedia</a>. The desk's answer follows the roofline: guards help under trees that drop leaves, and are wasted effort where the problem is pine needles or silt.</p>",

"home/home-office-setup":
    "<p><b>Ergonomics and power, both planned.</b> Screen height, seating and lighting have a documented evidence base summarised in the <a href=\"" + _w("ergonomics") + "\" rel=\"noopener\">ergonomics reference material on Wikipedia</a>, and <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the health guidance on screen use. The desk's setup assumes the power will fail and plans around it.</p>",

"home/how-to-clean-a-washing-machine":
    "<p><b>The parts that hold the smell.</b> Detergent residue, the door seal and the drain filter are the three places a machine keeps its grime, and the <a href=\"" + _w("washing+machine") + "\" rel=\"noopener\">washing-machine reference material on Wikipedia</a> describes the components. The desk's routine is monthly, because the buildup that causes odours is invisible until it is obvious.</p>",

"home/how-to-clean-and-care-for-a-mattress":
    "<p><b>Allergen control, not stain removal.</b> Dust-mite exposure is a documented health concern, and <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> publishes the allergy guidance behind the desk's advice, with the <a href=\"" + EPA + "\" rel=\"noopener\">EPA</a> covering indoor air quality. The <a href=\"" + _w("mattress") + "\" rel=\"noopener\">mattress reference material on Wikipedia</a> explains which constructions tolerate which cleaning methods.</p>",

"home/how-to-clear-a-slow-shower-drain":
    "<p><b>Effort, in ascending order.</b> Hair and soap residue collect in the trap, and the <a href=\"" + _w("trap+(plumbing)") + "\" rel=\"noopener\">plumbing-trap reference material on Wikipedia</a> explains the geometry that catches them. The desk's order — hair catcher, plunger, manual removal, then chemicals last — is arranged so the corrosive option is the last resort rather than the first.</p>",

"home/how-to-deep-clean-an-oven":
    "<p><b>Chemistry decides the method.</b> Baked-on grease responds to alkaline cleaners and time, and the <a href=\"" + _w("oven+cleaner") + "\" rel=\"noopener\">oven-cleaner reference material on Wikipedia</a> covers what each product type does. The desk's cautions are the practical ones: ventilation, no caustic on self-cleaning elements, and never mix products.</p>",

"home/how-to-defrost-a-freezer-properly":
    "<p><b>Ice is insulation you did not ask for.</b> Frost buildup reduces efficiency, and the <a href=\"" + _w("freezer") + "\" rel=\"noopener\">freezer reference material on Wikipedia</a> explains the mechanism and the frost-free alternative. The desk's method protects the food first and the appliance second, which is the order most guides get backwards.</p>",

"home/how-to-descale-a-kettle":
    "<p><b>Hard water leaves a predictable deposit.</b> Calcium carbonate precipitates on the heating element, and the <a href=\"" + _w("limescale") + "\" rel=\"noopener\">limescale reference material on Wikipedia</a> explains why it returns and how acid dissolves it. The desk's note on prevention matters as much as the fix: descaling frequency is a function of your water, not your habits.</p>",

"home/how-to-shut-off-water-main":
    "<p><b>Know it before the emergency.</b> The isolation valve is the first line of damage control, and the <a href=\"" + _w("valve") + "\" rel=\"noopener\">valve reference material on Wikipedia</a> describes the types you may meet. The desk's advice is to operate it once a year so it is not seized when it matters, and to label it for whoever else lives there.</p>",

"home/how-to-unblock-a-toilet":
    "<p><b>Technique, not force.</b> The mechanism is described in the <a href=\"" + _w("flush+toilet") + "\" rel=\"noopener\">flush-toilet reference material on Wikipedia</a>, and the desk's method uses water pressure rather than chemical or mechanical aggression. The page states plainly when to stop: repeated failure means the blockage is further down the system than a plunger can reach.</p>",

"home/hvac-filter-sizes-and-merv":
    "<p><b>The rating system is published, not invented.</b> MERV classifies filtration efficiency, and the <a href=\"" + _w("minimum+efficiency+reporting+value") + "\" rel=\"noopener\">MERV reference material on Wikipedia</a> explains the scale. The <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the maintenance guidance behind the desk's interval — and the trade-off between filtration and airflow restriction.</p>",

"home/ice-dam-prevention-checklist":
    "<p><b>A heat-loss problem wearing a roofing costume.</b> Ice dams form when a warm roof melts snow that refreezes at the eaves, and the <a href=\"" + _w("ice+dam") + "\" rel=\"noopener\">ice-dam reference material on Wikipedia</a> explains the mechanism. The desk's checklist attacks the cause — attic heat and ventilation — because removing the ice treats the symptom.</p>",

"home/inverter-sizing-calculator":
    "<p><b>Sizing is a load calculation.</b> Starting surge, continuous draw and battery capacity interact, and the <a href=\"" + _w("power+inverter") + "\" rel=\"noopener\">power-inverter reference material on Wikipedia</a> describes the specifications. This tool runs in your browser; product conformity in Nigeria is the remit of the <a href=\"" + SON + "\" rel=\"noopener\">Standards Organisation of Nigeria</a>.</p>",

"home/is-it-cheaper-to-heat-one-room":
    "<p><b>The answer depends on the heating system.</b> Zone heating and whole-home systems have different economics, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the space-heating guidance behind the desk's comparison. The <a href=\"" + EIA + "\" rel=\"noopener\">Energy Information Administration</a>'s price data supplies the cost figures on the page.</p>",

"home/mice-in-the-house-signs":
    "<p><b>Signs first, then exclusion.</b> Rodent activity carries documented health implications, and the <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the guidance on rodents and disease. The <a href=\"" + _w("house+mouse") + "\" rel=\"noopener\">house-mouse reference material on Wikipedia</a> explains the behaviour that makes sealing entry points more effective than traps alone.</p>",

"home/microwave-oven-care-and-safety":
    "<p><b>The door is the safety system.</b> Microwave leakage is prevented by the door's mesh and seals, and the <a href=\"" + _w("microwave+oven") + "\" rel=\"noopener\">microwave-oven reference material on Wikipedia</a> explains the mechanism. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the appliance fire-safety guidance behind the desk's warning about running it empty or with a damaged door.</p>",

"home/mistakes/drilling-without-checking":
    "<p><b>What is behind the wall is knowable.</b> Detection tools and building conventions are described in the <a href=\"" + _w("stud+finder") + "\" rel=\"noopener\">stud-finder reference material on Wikipedia</a>, and the <a href=\"" + ICC + "\" rel=\"noopener\">International Code Council</a> publishes the construction standards that determine where services usually run. The desk's rule is to assume every wall has something in it until a detector says otherwise.</p>",

"home/moving-week-by-week":
    "<p><b>A sequence, because order is the whole value.</b> The tasks a move actually contains are described in the <a href=\"" + _w("moving+company") + "\" rel=\"noopener\">moving-company reference material on Wikipedia</a>, and the desk's calendar adds the parts that get skipped: change of address, meter readings, and the box you will need on the first night.</p>",

"home/paint-calculator":
    "<p><b>Coverage is a published figure, and it is optimistic.</b> Spreading rate depends on surface and binder, and the <a href=\"" + _w("paint") + "\" rel=\"noopener\">paint reference material on Wikipedia</a> covers the factors. This calculator runs in your browser and the desk's advice rounds up, because buying a second litre mid-job costs more than the leftover.</p>",

"home/pipe-lagging-winter-guide":
    "<p><b>Insulation delays freezing; it does not prevent it.</b> The heat-transfer principles are described in the <a href=\"" + _w("pipe+insulation") + "\" rel=\"noopener\">pipe-insulation reference material on Wikipedia</a>, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the insulation guidance. The desk's honest framing: lagging buys hours, and the unheated cupboard still needs heat.</p>",

"home/pre-move-inspection":
    "<p><b>Documented before you sign.</b> What a property inspection covers is described in the <a href=\"" + _w("home+inspection") + "\" rel=\"noopener\">home-inspection reference material on Wikipedia</a>, and the <a href=\"" + ICC + "\" rel=\"noopener\">International Code Council</a> publishes the building standards a surveyor measures against. The desk's list is the version you can run yourself with a phone camera.</p>",

"home/radiators-cold-top-or-bottom":
    "<p><b>Each pattern means something different.</b> Cold at the top is air; cold at the bottom is sludge, and the <a href=\"" + _w("radiator+(heating)") + "\" rel=\"noopener\">radiator reference material on Wikipedia</a> describes how hydronic systems behave. The desk's diagnostic uses the pattern to pick the fix, which is cheaper than doing both.</p>",

"home/repair-or-replace-appliances":
    "<p><b>The comparison is lifetime cost.</b> Repair price against remaining life and running cost, using the consumption and price data published by the <a href=\"" + EIA + "\" rel=\"noopener\">Energy Information Administration</a> and the efficiency guidance from the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a>. The desk's threshold is a rule of thumb, stated as one.</p>",

"home/roof-gutter-leak-joint":
    "<p><b>Joints fail before the gutter does.</b> Thermal movement and sealant ageing are the usual causes, and the <a href=\"" + _w("rain+gutter") + "\" rel=\"noopener\">rain-gutter reference material on Wikipedia</a> covers the profiles and fixings. The desk's order is clean, then re-seat, then reseal — because sealing over debris guarantees a repeat visit.</p>",

"home/season-cast-iron-pan":
    "<p><b>Seasoning is polymerised oil, not a coating.</b> The chemistry is described in the <a href=\"" + _w("seasoning+(cookware)") + "\" rel=\"noopener\">cookware-seasoning reference material on Wikipedia</a>, which explains why thin layers beat thick ones. The desk's small version exists because most guidance oversells the effort: a used pan needs maintenance, not a ritual.</p>",

"home/sink-drain-slow-unclog":
    "<p><b>The trap is the first suspect.</b> Grease and debris collect in the U-bend, and the <a href=\"" + _w("trap+(plumbing)") + "\" rel=\"noopener\">plumbing-trap reference material on Wikipedia</a> explains the geometry. The desk's order is plughole, plunger, trap, then rod — with chemicals last, because they are the option that cannot be undone.</p>",

"home/spring-home-reset":
    "<p><b>An order, not a list.</b> Ventilation, moisture and efficiency tasks come from the <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a>'s indoor-air guidance and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a>'s seasonal checklist. The desk sequences them so each job does not undo the previous one, which is the failure mode of most seasonal cleaning.</p>",

"home/stop-pre-rinsing-dishes":
    "<p><b>Modern machines are designed for soiled dishes.</b> Detergent enzymes need food residue to act on, and the <a href=\"" + _w("dishwasher") + "\" rel=\"noopener\">dishwasher reference material on Wikipedia</a> explains the mechanism. The <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the water and energy figures behind the desk's argument that pre-rinsing costs more than it saves.</p>",

"home/storage-heaters-explained":
    "<p><b>Store heat cheaply, release it slowly.</b> The design and its controls are described in the <a href=\"" + _w("storage+heater") + "\" rel=\"noopener\">storage-heater reference material on Wikipedia</a>, and the <a href=\"" + EIA + "\" rel=\"noopener\">Energy Information Administration</a> publishes the tariff-structure data that decides whether the economics work. The desk's guidance covers the controls, which is where most of the savings actually are.</p>",

"home/summer-cooling-checklist":
    "<p><b>Block the heat before you cool the air.</b> Shading, ventilation and airflow are covered by the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a>'s cooling guidance, and the <a href=\"" + _w("air+conditioning") + "\" rel=\"noopener\">air-conditioning reference material on Wikipedia</a> explains the systems. The desk's order is deliberate: the free measures come first and cut the bill before anything is switched on.</p>",

"home/sump-pump-failure-signs":
    "<p><b>Test it, do not trust it.</b> A sump pump only matters once, and the <a href=\"" + _w("sump+pump") + "\" rel=\"noopener\">sump-pump reference material on Wikipedia</a> describes the float and switch mechanisms that fail silently. The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a>'s basement-water guidance covers the drainage side, and the desk's ten-second test is on the page.</p>",

"home/toilet-runs-after-flush":
    "<p><b>Three parts, one symptom.</b> Flapper, chain and float are the usual culprits, and the <a href=\"" + _w("flush+toilet") + "\" rel=\"noopener\">flush-toilet reference material on Wikipedia</a> describes the cistern mechanism. The desk's diagnostic starts with the dye test, because a silent leak is both the commonest fault and the most expensive one to ignore.</p>",

"home/vacuum-cleaner-care-guide":
    "<p><b>Lost suction is almost always a blockage or a filter.</b> The mechanisms are described in the <a href=\"" + _w("vacuum+cleaner") + "\" rel=\"noopener\">vacuum-cleaner reference material on Wikipedia</a>, and the desk's order follows the airflow path from the nozzle backwards. The filter is the part people replace last and should check first.</p>",

"home/vinegar-in-the-dishwasher":
    "<p><b>An acid in a machine designed for alkali.</b> Dishwasher detergents are alkaline by design, and the <a href=\"" + _w("vinegar") + "\" rel=\"noopener\">vinegar reference material on Wikipedia</a> covers what acetic acid does — including to seals and to the detergent's own action. The <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the appliance-care guidance the desk's alternative follows.</p>",

"home/washing-machine-hoses-replace":
    "<p><b>A cheap part with an expensive failure.</b> Rubber hoses degrade with age and pressure cycling, and the <a href=\"" + _w("washing+machine") + "\" rel=\"noopener\">washing-machine reference material on Wikipedia</a> describes the supply arrangement. The desk's interval is preventive rather than reactive, which is the entire point: the flood happens on a hose that looked fine.</p>",

"home/washing-machine-mould-door-seal":
    "<p><b>A damp, dark, warm fold.</b> Mould growth in that seal follows the conditions documented in the <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a>'s mould guidance, and the <a href=\"" + _w("washing+machine") + "\" rel=\"noopener\">washing-machine reference material on Wikipedia</a> describes the seal's function. The desk's habit — door open after every wash — costs nothing and prevents most of it.</p>",

"home/washing-machine-wont-drain":
    "<p><b>Check the filter before you call anyone.</b> Drain pumps are protected by a filter that collects coins and lint, and the <a href=\"" + _w("washing+machine") + "\" rel=\"noopener\">washing-machine reference material on Wikipedia</a> describes the drainage path. The desk's order is filter, hose, then pump, which is the reverse of how expensive the faults actually are.</p>",

"home/water-heater-explained":
    "<p><b>Know the machine before it fails.</b> Tank and tankless designs differ in failure mode and maintenance, and the <a href=\"" + _w("water+heating") + "\" rel=\"noopener\">water-heating reference material on Wikipedia</a> covers both. The <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the efficiency and temperature guidance behind the desk's settings advice.</p>",

"home/water-heater-flush-how-to":
    "<p><b>The rumbling is sediment boiling.</b> Mineral deposits insulate the element and overheat the tank floor, and the <a href=\"" + _w("water+heating") + "\" rel=\"noopener\">water-heating reference material on Wikipedia</a> explains the mechanism. The desk's flush procedure is the annual version, with the safety steps stated first because the water involved is hot and under pressure.</p>",

"home/why-does-my-circuit-breaker-keep-tripping":
    "<p><b>A trip is protection working.</b> Overload, short circuit and earth leakage each trip differently, and the <a href=\"" + _w("circuit+breaker") + "\" rel=\"noopener\">circuit-breaker reference material on Wikipedia</a> explains the mechanisms. The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the electrical fire-safety guidance behind the desk's rule: a breaker that trips repeatedly is a fault to find, not a switch to reset.</p>",

"home/why-is-my-home-doing-that":
    "<p><b>Symptoms map to causes, mostly.</b> Ten common household complaints have a small set of explanations, and the desk's finder routes each to the relevant guide — with the <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a>'s moisture and air-quality guidance behind the damp and smell entries. Where a symptom indicates a structural or gas issue, the page says to call a professional.</p>",

"home/window-film-for-heat":
    "<p><b>Solar gain is measurable, and so is the film's effect.</b> How films reject infrared and what they cost in light transmission is described in the <a href=\"" + _w("window+film") + "\" rel=\"noopener\">window-film reference material on Wikipedia</a>, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the window-efficiency guidance. The desk's verdict: real but partial, and no substitute for external shade.</p>",

"home/winter-home-preparation":
    "<p><b>The last pass before the cold.</b> The checklist follows the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a>'s heating and insulation guidance, with the moisture and ventilation items from the <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a>. The desk's ordering is by what fails first in a cold snap, which is rarely the thing people prepare for.</p>",

}
