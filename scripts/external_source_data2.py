# -*- coding: utf-8 -*-
"""External source notes, part 2: the BRYME Home & DIY desk (42 pages).
Same rule as part 1 - every URL curl-verified 200 at authoring time."""

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
NIST = "https://www.nist.gov/"
MEDLINE = "https://medlineplus.gov/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

EXTERNAL_SOURCES2 = {

"home/air-cooler-vs-fan-care":
    "<p><b>How the cooling actually happens.</b> An evaporative cooler trades heat for humidity, and the <a href=\"" + _w("evaporative+cooler") + "\" rel=\"noopener\">evaporative-cooler reference material on Wikipedia</a> explains why that works in dry air and stops working in humid air — the single fact that decides whether the machine is worth its water in your climate.</p>",

"home/barred-windows-and-fire-escape":
    "<p><b>The escape route is regulated for a reason.</b> The <a href=\"" + USFA + "\" rel=\"noopener\">U.S. Fire Administration</a> publishes guidance on security bars and escape routes, including the release-mechanism requirement that turns a barred window back into an exit. The desk treats any bar without an operable release from inside as a defect, not a security upgrade.</p>",

"home/burning-plastic-smell-socket":
    "<p><b>Electrical fires start quietly.</b> The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the statistics and the safety guidance behind wiring faults, arcing and overheated outlets. The desk's five-minute triage exists because the smell is the early warning, and the correct response is to stop using the circuit rather than to investigate it live.</p>",

"home/changeover-switch-care":
    "<p><b>Transfer switching is standardised equipment.</b> The devices that select between grid and generator are covered by the <a href=\"" + _w("transfer+switch") + "\" rel=\"noopener\">transfer-switch reference material on Wikipedia</a>, including why back-feeding a generator into a live grid is dangerous to line workers. Product conformity in Nigeria is the remit of the <a href=\"" + SON + "\" rel=\"noopener\">Standards Organisation of Nigeria</a>.</p>",

"home/cockroach-fridge-motor-bay":
    "<p><b>Why they choose the compressor.</b> Cockroaches seek warmth, moisture and shelter, which is exactly what a fridge's motor bay offers — the <a href=\"" + _w("German+cockroach") + "\" rel=\"noopener\">reference material on the species</a> explains the habitat preferences that make kitchens the target. Hygiene and household-pest guidance from the <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> covers the health side.</p>",

"home/doors-sticking-rainy-season":
    "<p><b>Wood moves with moisture, predictably.</b> Timber swells across the grain as it absorbs humidity, and the <a href=\"" + _w("wood+moisture+content") + "\" rel=\"noopener\">wood-moisture reference material on Wikipedia</a> explains the mechanism — including why the swelling is worst across the width of the door and why planing in the rains is a mistake you repeat every dry season.</p>",

"home/dripping-tap-cartridge-fix":
    "<p><b>The mechanism, documented.</b> Modern mixer taps seal with a ceramic or rubber cartridge rather than a washer, and the <a href=\"" + _w("faucet") + "\" rel=\"noopener\">tap reference material on Wikipedia</a> sets out the valve types and their failure modes. Knowing which type you have is the whole job: the fix is a replacement part, not a repair.</p>",

"home/energy-bills":
    "<p><b>Prices and consumption data, from the source.</b> The <a href=\"" + EIA + "\" rel=\"noopener\">U.S. Energy Information Administration</a> publishes the energy price and consumption statistics that make running-cost comparisons possible, and the <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the efficiency guidance behind them. The desk's arithmetic uses measured consumption, not a label's best case.</p>",

"home/extension-cords-temporary-power":
    "<p><b>Tested equipment, and the rules around it.</b> <a href=\"" + UL + "\" rel=\"noopener\">UL Solutions</a> certifies the cord and socket products that carry its mark, and the <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the fire-safety guidance on extension-cord misuse. Product standards in Nigeria fall to the <a href=\"" + SON + "\" rel=\"noopener\">Standards Organisation of Nigeria</a>.</p>",

"home/flat-roof-ponding-and-leaks":
    "<p><b>Ponding is defined, not vague.</b> Water standing beyond the drainage period a roof was designed for is a measurable condition, and the <a href=\"" + _w("flat+roof") + "\" rel=\"noopener\">flat-roof reference material on Wikipedia</a> covers the drainage falls and membrane types behind it. The desk's rule follows the physics: fix the fall, then the membrane.</p>",

"home/floor-drain-backflow":
    "<p><b>Backflow has a standard fix.</b> A drain that returns water rather than taking it is a pressure or blockage problem, and the <a href=\"" + _w("backflow+prevention+device") + "\" rel=\"noopener\">backflow-prevention reference material on Wikipedia</a> explains the devices that stop it. Sewer and drainage guidance from the <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> covers the septic and stormwater side.</p>",

"home/fridge-food-safety-power-cut":
    "<p><b>The food-safety clock, from the health authority.</b> How long a closed refrigerator holds a safe temperature is a documented figure, and the <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a>'s food-safety guidance is the desk's source for the four-hour rule and the discard thresholds. The <a href=\"" + _w("food+safety") + "\" rel=\"noopener\">food-safety reference material on Wikipedia</a> sets out the temperature danger zone behind it.</p>",

"home/gas-cylinder-change-safely":
    "<p><b>LPG safety is written down.</b> Cylinder handling, leak testing and ventilation requirements are covered by the <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a>, and the <a href=\"" + _w("liquefied+petroleum+gas") + "\" rel=\"noopener\">LPG reference material on Wikipedia</a> explains why the gas behaves as it does when it leaks. Cylinder standards in Nigeria are set by the <a href=\"" + SON + "\" rel=\"noopener\">Standards Organisation of Nigeria</a>.</p>",

"home/gate-intercom-not-working":
    "<p><b>Four components, one failure chain.</b> A door entry system is a button, a controller, a lock release and a power supply, and the <a href=\"" + _w("intercom") + "\" rel=\"noopener\">intercom reference material on Wikipedia</a> describes the architectures. The desk's diagnostic order follows the voltage: power first, then the trigger, then the lock — because the lock is usually innocent.</p>",

"home/gate-motor-solar-light-care":
    "<p><b>Small systems fail on maintenance, not design.</b> A solar security light is a panel, a battery and a controller, and the <a href=\"" + _w("gate+operator") + "\" rel=\"noopener\">gate-operator reference material on Wikipedia</a> covers the motor side of the pairing. The battery is the consumable in both: the desk's service intervals are built around its expected life rather than the manufacturer's optimism.</p>",

"home/gate-motor-wont-move":
    "<p><b>A humming motor is telling you something specific.</b> The <a href=\"" + _w("gate+operator") + "\" rel=\"noopener\">gate-operator reference material on Wikipedia</a> describes the clutch, limit-sensor and obstruction-detection arrangements that decide why a motor energises but does not move. The desk's order is deliberate: check the mechanical release before the electrics, because that is where most faults actually are.</p>",

"home/generator-rainy-season-safety":
    "<p><b>Two hazards, both documented.</b> Water and electricity, and carbon monoxide from an exhaust in still air — the <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> and the <a href=\"" + USFA + "\" rel=\"noopener\">U.S. Fire Administration</a> both publish generator-safety guidance covering them. The six rules on this page are those two hazards reduced to a checklist; none of them is negotiable.</p>",

"home/generator-service-calendar":
    "<p><b>Service intervals are engineering, not folklore.</b> Oil, filters and fuel stability follow operating hours and calendar time, and the <a href=\"" + _w("diesel+generator") + "\" rel=\"noopener\">generator reference material on Wikipedia</a> covers the maintenance factors behind them. The desk's calendar is built for the machine that sits unused for months, which is the harder case and the more common one.</p>",

"home/grease-trap-yard-clean":
    "<p><b>What the trap is for, and what happens when it is not.</b> A grease trap separates fats before they reach the drain, and the <a href=\"" + _w("grease+trap") + "\" rel=\"noopener\">grease-trap reference material on Wikipedia</a> explains the mechanism and the consequences of skipping service. The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the fats-oils-grease guidance that most municipal rules are based on.</p>",

"home/home-repair-costs-explained":
    "<p><b>Costs compared against published data.</b> The desk's figures are grounded in the kind of consumption and price series the <a href=\"" + EIA + "\" rel=\"noopener\">U.S. Energy Information Administration</a> publishes for the energy side of running a home, and in the <a href=\"" + _w("home+improvement") + "\" rel=\"noopener\">home-improvement reference material on Wikipedia</a> for the trade side. Local labour rates vary widely, so every figure here is stated as a range with its check date.</p>",

"home/hot-top-floor-ceiling":
    "<p><b>Heat has a documented path.</b> Solar gain through a roof slab is a measurable transfer, and the <a href=\"" + _w("thermal+insulation") + "\" rel=\"noopener\">thermal-insulation reference material on Wikipedia</a> explains the mechanisms and the materials that interrupt them. The desk's ranking of fixes follows the physics: shade the surface first, insulate second, cool last.</p>",

"home/how-to-paint-a-room-right":
    "<p><b>The sequence matters more than the brand.</b> Preparation, primer and the number of coats are governed by the paint's chemistry, and the <a href=\"" + _w("paint") + "\" rel=\"noopener\">paint reference material on Wikipedia</a> covers binder types and what each needs from a surface. The desk's weekend plan is ordered so that each stage can dry properly — the step people compress and then regret.</p>",

"home/indoor-drying-rainy-season":
    "<p><b>Drying indoors is a humidity problem.</b> Wet clothes release litres of water into a room, and the <a href=\"" + _w("mold") + "\" rel=\"noopener\">mould reference material on Wikipedia</a> explains the humidity levels at which that water becomes a health issue rather than an inconvenience. The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the indoor-moisture guidance the desk's spacing and ventilation advice follows.</p>",

"home/moving-costs-explained":
    "<p><b>What movers charge for, itemised.</b> The cost structure — labour, vehicle, distance, stairs, packing materials — is described in the <a href=\"" + _w("moving+company") + "\" rel=\"noopener\">moving-company reference material on Wikipedia</a>, and the desk's breakdown follows it line by line. The negotiation leverage sits in the items you can do yourself, which is why the page lists them separately.</p>",

"home/pump-short-cycling-waterhammer":
    "<p><b>Two distinct problems with similar sounds.</b> Short cycling is usually a pressure-vessel or switch issue; the banging is a pressure surge, and the <a href=\"" + _w("water+hammer") + "\" rel=\"noopener\">water-hammer reference material on Wikipedia</a> explains the mechanism and why it damages joints over time. The desk treats them separately because fixing one does not fix the other.</p>",

"home/rainwater-harvest-drum":
    "<p><b>Harvested water needs handling rules.</b> Roof runoff carries what is on the roof, and the <a href=\"" + _w("rainwater+harvesting") + "\" rel=\"noopener\">rainwater-harvesting reference material on Wikipedia</a> covers first-flush diversion and storage. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a>'s drinking-water guidance is the desk's boundary on what harvested water may be used for without treatment.</p>",

"home/sink-trap-clean-smell":
    "<p><b>The trap is a water seal, and seals evaporate.</b> The U-bend under a sink holds water specifically to block sewer gas, and the <a href=\"" + _w("trap+%28plumbing%29") + "\" rel=\"noopener\">plumbing-trap reference material on Wikipedia</a> explains how it works and how it fails. The desk's advice is mechanical first: a smell is usually a dry or blocked trap, not a dirty drain.</p>",

"home/soakaway-filling-up-signs":
    "<p><b>Infiltration is a ground condition, not a tank level.</b> A soakaway depends on the surrounding soil accepting water, and the <a href=\"" + _w("soakaway") + "\" rel=\"noopener\">soakaway reference material on Wikipedia</a> describes the design and the failure modes. The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the on-site wastewater guidance that explains why silted systems stop working long before they fill.</p>",

"home/sofa-leather-vinyl-care":
    "<p><b>Two materials, two failure modes.</b> Leather dries and cracks when it loses oils; vinyl fails at the plasticiser, and the <a href=\"" + _w("leather") + "\" rel=\"noopener\">leather reference material on Wikipedia</a> explains the tannage and conditioning behind the difference. The desk's two-season routine exists because the harmattan and the rains damage upholstery in opposite ways.</p>",

"home/tiles-hollow-sounding-lifting":
    "<p><b>A hollow sound is a bond failure, not a tile defect.</b> Adhesive coverage and substrate preparation decide whether a tile stays put, and the <a href=\"" + _w("tile+adhesive") + "\" rel=\"noopener\">tile-adhesive reference material on Wikipedia</a> covers the bonding mechanisms. The desk's knock test is a diagnostic: the repair depends on whether the failure is at the tile or at the substrate.</p>",

"home/toilet-clog-how-to-plunge":
    "<p><b>Technique is the whole fix.</b> A plunger works by moving water, not air, and the <a href=\"" + _w("plunger") + "\" rel=\"noopener\">plunger reference material on Wikipedia</a> explains why the flange design suits a toilet and the cup design does not. The desk's method is the standard one: seal, then push and pull with the water doing the work.</p>",

"home/towels-smell-fresh":
    "<p><b>The smell is bacterial, and it survives the wash.</b> Damp fabric in warm air grows the organisms that produce the sour note, and the <a href=\"" + _w("laundry") + "\" rel=\"noopener\">laundry reference material on Wikipedia</a> covers wash temperature and drying — the two variables that actually decide the outcome. Detergent quantity matters less than either, which is the part that surprises people.</p>",

"home/tv-mount-on-block-wall":
    "<p><b>The anchor is the structural decision.</b> A block wall holds differently from a stud wall, and the <a href=\"" + _w("screw+anchor") + "\" rel=\"noopener\">screw-anchor reference material on Wikipedia</a> explains what each anchor type is rated for in masonry. The desk's rule follows the ratings: fix into the block, not the mortar joint, and use an anchor rated well above the load.</p>",

"home/us-diy-electrical-rules":
    "<p><b>The rules are published, and they are enforceable.</b> The <a href=\"" + NFPA + "\" rel=\"noopener\">National Fire Protection Association</a> publishes the National Electrical Code that most US jurisdictions adopt, and the <a href=\"" + ICC + "\" rel=\"noopener\">International Code Council</a> publishes the residential code alongside it. The desk's summary is orientation, not legal advice: the adopted local code and its permit requirements decide what you may do.</p>",

"home/wall-cracks-when-serious":
    "<p><b>Crack patterns mean different things.</b> Hairline plaster movement and structural displacement look different and behave differently, and the <a href=\"" + _w("subsidence") + "\" rel=\"noopener\">subsidence reference material on Wikipedia</a> explains the ground movement behind the serious cases. The desk's two-minute read is a triage, not a diagnosis — the page says clearly when to call a structural engineer.</p>",

"home/water-dispenser-jar-pump":
    "<p><b>The clean-looking part is the dirty one.</b> A dispenser's internal reservoir and pump stay wet between uses, and the <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a>'s drinking-water guidance is the desk's reference for why standing water needs regular cleaning. The <a href=\"" + _w("water+dispenser") + "\" rel=\"noopener\">water-dispenser reference material on Wikipedia</a> describes the mechanisms involved.</p>",

"home/water-heater-no-hot-water":
    "<p><b>Five checks, in the order that finds the fault.</b> Power, thermostat, heating element, pressure relief and sediment each fail differently, and the <a href=\"" + _w("water+heating") + "\" rel=\"noopener\">water-heating reference material on Wikipedia</a> covers the system types and their components. The desk's order starts with the supply because it is the cheapest thing to be wrong about.</p>",

"home/water-tank-annual-clean":
    "<p><b>Stored water is a health question.</b> A tank that is never cleaned grows a biofilm regardless of how good the supply was, and the <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a>'s drinking-water and household-water guidance is the desk's source for the cleaning and disinfection practice recommended here. The <a href=\"" + _w("water+storage+tank") + "\" rel=\"noopener\">storage-tank reference material on Wikipedia</a> covers the materials and their maintenance needs.</p>",

"home/weevils-in-rice-and-beans":
    "<p><b>They arrive with the grain.</b> Weevil eggs are laid before the rice is bagged, and the <a href=\"" + _w("weevil") + "\" rel=\"noopener\">weevil reference material on Wikipedia</a> explains the life cycle that makes an infestation look sudden. That is why the desk's advice targets storage and temperature rather than blame: the insects were already inside.</p>",

"home/wet-waste-bin-smell":
    "<p><b>Heat accelerates decomposition, measurably.</b> The <a href=\"" + EPA + "\" rel=\"noopener\">Environmental Protection Agency</a> publishes the composting and organic-waste guidance that explains why wet waste in a hot climate turns odorous within hours, and the <a href=\"" + _w("waste+management") + "\" rel=\"noopener\">waste-management reference material on Wikipedia</a> covers the separation habits that reduce it. The fix is drainage and frequency, not deodorant.</p>",

"home/window-ac-clatter-and-filter":
    "<p><b>Reduced cooling is usually airflow, not refrigerant.</b> A blocked filter raises the load and the noise together, and the <a href=\"" + _w("air+conditioning") + "\" rel=\"noopener\">air-conditioning reference material on Wikipedia</a> explains the cycle that makes airflow the dominant variable. The <a href=\"" + ENERGY + "\" rel=\"noopener\">Department of Energy</a> publishes the maintenance guidance behind the desk's filter interval.</p>",

"home/window-weep-holes":
    "<p><b>The holes are supposed to be there.</b> A window frame drains through small openings at the bottom of the track, and the <a href=\"" + _w("weep+hole") + "\" rel=\"noopener\">weep-hole reference material on Wikipedia</a> explains their function in both windows and masonry. Blocking them with paint or sealant is the common error, and it turns a drainage path into a leak.</p>",

}
