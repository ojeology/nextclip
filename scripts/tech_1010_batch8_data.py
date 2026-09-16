# -*- coding: utf-8 -*-
"""Batch 8 — 10/10 brief Tier 2 item 19: Home insurance vs home warranty.

Written from primary documents only: a state insurance regulator's consumer
guide, a home warranty provider's own published sample contract, the NAIC's
state-by-state model-law chart, FEMA and the Congressional Research Service on
flood, the FTC on service contracts, and two insurers' and one cover provider's
own published product pages in the UK and Nigeria.

Every figure below is traceable to the source list at the end of the article.
Where a document is old (the AHS sample contract carries a 14 January 2021
revision date) or state-specific (the TDI guide), that is stated in the piece
rather than smoothed over.

Kept in /home/user/tools/ (persistent) and copied into the clone's scripts/ —
the clone lives in .cache, which does not survive between turns.
"""

BATCH_1010_B8 = [
    (
        "home-insurance-vs-home-warranty",
        "subscriptions",
        "guide",
        "Home insurance vs home warranty: the two contracts that cover opposite failures",
        "A home policy pays when a named peril damages your house. A home warranty is a service contract that pays when a machine wears out. Each one excludes the other's trigger — and which regulator hears your complaint depends on the state you live in.",
        """<p>These two get sold as complements, and they are complements, but almost nobody explains <em>why</em> they cannot substitute for each other. The reason is not marketing. It is that each contract excludes precisely the event the other one covers.</p>

<p>American Home Shield's published sample contract excludes breakdowns caused by "accidents, fire, freezing (except roof leaks), water damage, electrical failure or surge" and by "lightning, mud, earthquake, soil movement, storms, or acts of God". The Texas Department of Insurance's consumer guide lists "Wear and tear" among the things most home policies <strong>don't</strong> cover. Read the two sentences side by side and the shape of the market appears: the warranty takes the slow mechanical failure, the policy takes the sudden external event, and the overlap is close to empty.</p>

<p>Three further things decide this comparison before any price is mentioned, and all three are jurisdiction questions rather than product questions.</p>

<ul>
<li><strong>"Home warranty" is an American category.</strong> It is a service contract, which the FTC treats as a different object from a warranty, and which states classify differently — some as insurance, some explicitly not, some through a regulator that is not the insurance department at all.</li>
<li><strong>The UK equivalent is cover, not warranty.</strong> British Gas sells HomeCare for the boiler and heating system, and sells it <em>alongside</em> a boiler warranty that it describes as "basic cover". The two are priced separately and the warranty requires an annual service to stay valid.</li>
<li><strong>In Nigeria the published householder products are peril-based.</strong> Leadway's Householder plan and AIICO's Home Insurance plan both respond to fire, theft and burglary. Neither lists breakdown from wear and tear among its perils. The American question — insurance or warranty — does not have the same two options there.</li>
</ul>

<p>And one thing is not optional: if you still owe money on the home, your lender requires insurance. TDI is blunt about it — the law does not require home insurance, your lender does.</p>

<h2>Two different legal objects</h2>

<p>The FTC's warranty guidance has a section titled "Service Contracts Aren't Warranties". A service contract "costs extra and is sold separately from a product" and is therefore not the warranty that came with the thing you bought. That distinction is not pedantry; it determines who regulates the seller, what they must hold in reserve, and where you go when a claim is refused.</p>

<p>In the United States the classification is decided state by state, and the National Association of Insurance Commissioners publishes the map. Its model-law chart on service contracts, motor clubs and other extended warranties — state entries last reviewed between February and March 2023 — shows a genuine patchwork rather than a national rule.</p>

<div class="compare-scroll"><table class="compare-table"><caption class="sr-only">How US states classify home warranties, from the NAIC model-law chart PA-60</caption>
<thead><tr><th>Treatment</th><th>States, with the provision the NAIC chart cites</th></tr></thead>
<tbody>
<tr><td><strong>Regulated as insurance</strong></td><td>California calls it "Home Protection Insurance" (Ins. §§ 12740–12764). Connecticut: a home warranty contract "shall constitute contract of insurance", for structural components of dwellings of four units or fewer (§ 38a-320). Arizona regulates home warranty and home protection contracts through its insurance department (§§ 20-1095 to 20-1095.10). Florida requires licensing by the insurance department for home warranty business (§§ 634.301–634.348). North Dakota's administrative code includes home warranty in the definition of casualty insurance. Oklahoma's Service Warranty Insurance Act covers home warranties. Vermont's attorney general ruled in 1981 that home warranties are insurance; South Dakota's attorney general reached the same conclusion for prepaid home mechanical and electrical service agreements in 1978.</td></tr>
<tr><td><strong>Explicitly not insurance</strong></td><td>Ohio: "A home service contract is not insurance and is not governed by insurance law" (§ 3905.422). Pennsylvania exempts service contracts from regulation as insurance (40 P.S. § 477f) and has no home warranty provision at all. Tennessee (§ 56-2-126) and Colorado (§ 10-3-903(2)(g)) likewise. Delaware's statutes provide that service contracts and warranties are not regulated as insurance products.</td></tr>
<tr><td><strong>A regulator that is not the insurance department</strong></td><td>Texas licenses service contract providers through the Department of Licensing and Regulation (Occ. §§ 1304.001–1304.205) and handles home warranty through the Residential Service Company Act, regulated by the real estate commission (Occ. §§ 1303.001–1303.006). Virginia's Extended Service Contract Act sits with the commissioner of agriculture and consumer affairs, though a separate insurance-code chapter provides for home protection extended warranties (§§ 38.2-2600 to 38.2-2616). Oregon's service-contract framework is administered by the department of consumer and business services.</td></tr>
<tr><td><strong>Depends on scope, or on case law</strong></td><td>Alaska's statute turns on breadth: insurance statutes apply to a <em>comprehensive</em> home warranty covering the entire home, while contracts servicing household appliances and systems are not regulated under them (§ 21.03.021). West Virginia exempts service contracts from the insurance code (§ 33-4-2) — and then its supreme court held in <em>Riffe v. Home Finders Association</em> (1999) that a home warranty contract indemnifying a purchaser for repairs <em>was</em> insurance.</td></tr>
</tbody></table></div>

<p>That last row is the one to sit with. A single state can exempt the product by statute and still have a court call it insurance. The NAIC itself warns that its chart "does not constitute a formal legal opinion" and that the cited statutes should be consulted. So this article is not going to tell you what a home warranty <em>is</em> in general. It is going to tell you that the answer depends on where the house is, and that finding out takes one lookup of your own state's provision.</p>

<p>Why it matters practically: the remedy changes with the classification. American Home Shield's contract sends disputes to binding arbitration before a single arbitrator under the American Arbitration Association's Consumer Rules, with a decision that is "final, binding, and nonappealable", and it includes a class action waiver. An insurance claim dispute runs through a different door entirely — Texas, for instance, has a Consumer Bill of Rights for home and renters insurance that your company must give you when you buy or renew, and a state insurance department that takes complaints. Two products, two dispute systems, and you choose between them when you sign.</p>

<h2>What the insurance policy actually says</h2>

<p>Texas publishes a consumer guide to home insurance, and it is the clearest official statement of what these policies do. Most home policies there combine six coverages: dwelling, personal property, other structures, additional living expenses, personal liability, and medical payments. Note what is in that list and what is not — the structure, your belongings, the cost of living elsewhere while it is repaired, and your liability if you hurt someone. No machine is in it.</p>

<p>Then the perils. The guide's own table, which it prefaces with "coverages vary by company":</p>

<div class="compare-scroll"><table class="compare-table"><caption class="sr-only">Perils most Texas home policies cover and do not cover, per the TDI home insurance guide</caption>
<thead><tr><th>Most policies cover damage from</th><th>Most policies don't cover damage from</th></tr></thead>
<tbody>
<tr><td>Fire and lightning</td><td>Flooding</td></tr>
<tr><td>Sudden and accidental release of water or smoke</td><td>A continuous water leak; and no mold removal, except to repair damage caused by a covered risk</td></tr>
<tr><td>Explosion</td><td>Termites, insects, rats, or mice</td></tr>
<tr><td>Theft</td><td>Losses while the house is vacant for the number of days the policy specifies</td></tr>
<tr><td>Vandalism, malicious mischief, riot and civil commotion</td><td><strong>Wear and tear</strong></td></tr>
<tr><td>Aircraft and vehicles</td><td>Earthquakes or earth movement</td></tr>
<tr><td>Windstorm, hurricane and hail — but not if you live on the Gulf Coast</td><td>Wind or hail damage to trees and shrubs</td></tr>
</tbody></table></div>

<p>Two structural points hide in that table. The first is the asymmetry between "sudden and accidental release of water" and "a continuous water leak" — the same water, opposite outcomes, decided by how fast it arrived. The second is the Gulf Coast carve-out: Texas wind and hail damage on the coast is handled by the Texas Windstorm Insurance Association, a separate mechanism, and depending where you live you may need flood insurance before TWIA will sell you a policy.</p>

<p>The guide is equally useful on money. It works replacement cost against actual cash value with a roof: a ten-year-old roof costing $10,000 to replace today, with a $2,000 deductible, pays $8,000 under replacement cost coverage. Under actual cash value the same roof might be valued at $7,000, so the company pays $5,000 and your out-of-pocket is $5,000 rather than $2,000. Depreciation is defined as "a decrease in value because of wear and age" — the insurance policy, in other words, prices your house's wear and tear against you at claim time rather than covering it at failure time.</p>

<p>On limits: a deductible is subtracted from the claim, so a $1,000 claim with a $300 deductible pays $700, and you may have different deductibles for different coverages. Each coverage has a dollar limit, and most companies require you to insure the house for at least 80% of its replacement cost, with some requiring 100%. The declarations page — the first page of the policy — is where the coverages, limits and deductibles are summarised, which makes it the one page worth reading before a claim rather than after one.</p>

<p>Flood is the exclusion that surprises people, and it is federal rather than state. FEMA's own guidance states that most standard homeowners policies do not cover flood damage, and that cover is available through the National Flood Insurance Program where the community participates. The Congressional Research Service adds the mechanics: NFIP is the primary source of flood insurance for residential property in the US, no disaster declaration is needed to claim, renters can buy contents coverage even when the building owner buys nothing, and owners who skip required flood insurance may find themselves ineligible for certain disaster assistance afterwards. FEMA also publishes an Increased Cost of Compliance benefit of up to $30,000, payable on top of the flood claim, to elevate, floodproof, demolish or relocate the property. Premiums are moving: Risk Rating 2.0 was projected to increase premiums on roughly two-thirds of policies, against a statutory ceiling that bars increases above 18% a year for primary residences and 25% for other categories.</p>

<p>For what the standard policy is, the NAIC's homeowners report is the reference point: HO-3 provides all-risk coverage on buildings with broad named-peril coverage on personal property, and accounts for almost 80% of owner-occupied exposures, while HO-4 covers nearly 74% of tenant and condominium or co-op exposures and does not cover the building at all. That report's data is for 2018, collected from statistical agents in every state except Texas and California, which supply their own — old enough to read as structure rather than as current pricing.</p>

<h2>What the warranty contract actually says</h2>

<p>American Home Shield publishes a sample consumer home warranty contract, revision date 14 January 2021, with the customer's actual plan fee, term and trade service call fee set out on separate "Contract Agreement pages". Read as a specimen of the category, it is unusually explicit about the things that decide whether a warranty is worth its fee.</p>

<p><strong>What triggers it.</strong> Coverage is for "normal wear and tear malfunctions during the contract term". It also extends to malfunctions resulting from insufficient maintenance, rust, corrosion or sediment, improper installation or modification, mismatched indoor and outdoor HVAC units, and — the clause that matters most at claim time — "undetectable pre-existing conditions", defined as defects that could not have been found by a visual inspection or a "simple mechanical test", which the contract defines as turning the item on and off and checking that it operates without damage, irregular sounds, smoke or other abnormal outcomes.</p>

<p><strong>What it pays, and the ceilings.</strong> The caps are per malfunction and per contract term, and they are the numbers to compare rather than the monthly fee:</p>

<div class="compare-scroll"><table class="compare-table"><caption class="sr-only">Dollar limits in the AHS sample consumer home warranty contract</caption>
<thead><tr><th>Item</th><th>Limit stated in the sample contract</th></tr></thead>
<tbody>
<tr><td>Covered appliances, ShieldGold</td><td>Up to <strong>$3,000</strong> per covered item malfunction, for access, diagnosis and repair or replacement</td></tr>
<tr><td>Covered appliances, ShieldPlatinum</td><td>Up to <strong>$6,000</strong> per covered item malfunction</td></tr>
<tr><td>ShieldPlatinum coverage boost</td><td>Up to <strong>$1,000</strong> per contract term for duct, plenum, electrical and plumbing modifications, including relocating equipment and correcting code violations and permits</td></tr>
<tr><td>Roof leak repair</td><td>Up to <strong>$1,500</strong> total per agreement term; excluded are metal roofs, green roofs, anything penetrating the roof such as skylights, chimneys and vents, roof-mounted installations such as solar panels, and gutters and downspouts</td></tr>
<tr><td>Geothermal and water-source heat pumps, glycol, hot water or steam circulating systems</td><td>Up to <strong>$1,500</strong> per contract term</td></tr>
<tr><td>Access through a concrete floor, wall or ceiling — ductwork or plumbing</td><td>Up to <strong>$1,000</strong> per contract term, openings returned to a <em>rough finish</em>; you pay anything above it</td></tr>
<tr><td>Refrigerant, ShieldSilver and ShieldGold</td><td>Up to <strong>$10 per pound per occurrence</strong>; ShieldPlatinum covers refrigerant in full</td></tr>
<tr><td>Pool and inground spa equipment (optional)</td><td>Up to <strong>$3,000</strong> total per agreement term</td></tr>
<tr><td>Well pump (optional)</td><td>Up to <strong>$1,500</strong> per contract term</td></tr>
<tr><td>Rekey service</td><td>Up to 6 keyholes and 4 copied keys; trade service call fee is <strong>$100 regardless</strong> of the plan's fee. Lock picking and lock-out service are not covered</td></tr>
</tbody></table></div>

<p><strong>The clause most people miss.</strong> Section A.5.a: where the combined cost of diagnosis and repair or replacement "is estimated to exceed a stated contract dollar limit, AHS will not provide repair or replacement services but will instead pay an amount equal to the contract dollar limit minus the cost incurred to diagnose the malfunction." Do the arithmetic on a $4,200 appliance replacement against a $3,000 cap and the warranty does not fund the job — it hands you somewhat less than $3,000, less whatever the diagnosis cost, and the repair becomes yours to arrange. The cap is not a contribution towards a big repair. It converts a big repair into a smaller cash payment.</p>

<p>Related mechanics, all from the same document: AHS chooses the service contractor and will contact one within 48 hours of your request; the trade service call fee is owed per request, not per approved repair; if a repair or replacement fails within 30 days there is no second fee; if AHS tells you a malfunction is not covered you have 7 days to ask for a second opinion, and you pay another trade service call fee only if the second opinion agrees with the first. AHS holds the sole right to decide repair versus replacement, may install rebuilt parts, and replaces with equipment of "similar features, capacity, and efficiency, but not for matching dimensions, brand or color". It will not touch a malfunction already covered by a manufacturer, distributor, builder or extended warranty.</p>

<p><strong>What it will not pay for.</strong> The exclusions are worth reading in the provider's own order, because they describe the boundary with insurance almost exactly: misuse, abuse or mistreatment including damage by people, pests or pets; accidents, fire, freezing except roof leaks, water damage, electrical failure or surge, excessive or inadequate water pressure; lightning, mud, earthquake, soil movement, storms or acts of God; manufacturing defects; items determined defective by the Consumer Product Safety Commission or subject to a recall; mold, mildew, bio-organic growth, rot, fungus or pest damage, including its diagnosis and remediation; hazardous or toxic materials; routine maintenance, which stays yours; flues, venting, chimneys and exhaust lines; cosmetic defects; electronic, computerized or home management systems; radon monitoring, fire sprinkler and solar systems.</p>

<p>Then the consequential-loss clause, which is where the comparison with insurance becomes sharpest. AHS is "not responsible or liable for secondary, incidental, and/or consequential loss or damage" from a malfunction or from a contractor's neglect or delay, "including, but not limited to food spoilage, loss of income, utility bills, additional living expenses, personal and/or property damage." Additional living expenses is one of the six standard coverages in a home policy. The warranty excludes by name the thing the policy exists to provide.</p>

<p>In plumbing specifically, the covered list is long — leaks and breaks of water, drain, gas, waste and vent lines; toilets and their mechanisms; faucets, shower heads, valves and angle stops; permanently installed sump pumps for ground water; sewage ejector pumps; clearing of sink, tub, shower and toilet stoppages; mainline and lateral drain stoppages through an accessible cleanout up to 100 feet from the access point. The exclusions are just as specific: stoppages caused by collapsed, damaged or broken lines <em>outside the home's main foundation</em>, lines broken or infiltrated by roots or foreign objects even inside the foundation, bathtubs, sinks, showers, toilet lids and seats, caulking or grouting, septic tanks, water filtration systems, and the cost of locating or accessing cleanouts that cannot be found. A tree-rooted sewer lateral is not a warranty job, and it is not an insurance job either.</p>

<p><strong>Renewal and exit.</strong> The contract renews automatically unless you notify AHS before expiry, with renewal terms communicated within 60 days of expiration. You may cancel at any time for any reason. Inside the first 30 days: a full refund if no service was provided, otherwise the fees paid less the service costs AHS incurred — and if its costs exceed what you paid, you owe the lesser of the excess or the difference between the listed annual rate and the fees you paid. After day 30 the refund is pro rata for the unexpired term, on the same netting basis, plus an administrative fee equal to the lesser of one month's plan fee or the amount permitted by law.</p>

<h2>The same failure, two different answers</h2>

<p>This is the table that settles most real arguments. Each row is decided by a document cited above, not by convention.</p>

<div class="compare-scroll"><table class="compare-table"><caption class="sr-only">Which contract responds to common home failures</caption>
<thead><tr><th>What happened</th><th>Home policy</th><th>Home warranty</th></tr></thead>
<tbody>
<tr><td>A 15-year-old furnace fails its heat exchanger</td><td>No — wear and tear is excluded (TDI)</td><td><strong>Yes</strong> — wear and tear is the covered trigger, up to the plan's limit (AHS)</td></tr>
<tr><td>A pipe bursts in a freeze and floods the basement</td><td><strong>Yes</strong> — sudden and accidental release of water (TDI)</td><td>No — freezing and water damage are excluded breakdown causes (AHS)</td></tr>
<tr><td>A supply valve leaks slowly for months and ruins a vanity</td><td>No — a continuous water leak is excluded, and mold removal only where a covered risk caused the damage (TDI)</td><td>Partly — the valve is a covered plumbing item, but water damage is an excluded cause and restoration of cabinets, countertops and tiling is not payable (AHS)</td></tr>
<tr><td>A tree goes through the roof in a storm</td><td><strong>Yes</strong> — windstorm and hail, subject to Gulf Coast carve-outs (TDI)</td><td>No — storms and acts of God are excluded; roof leak repair is a separate, capped item (AHS)</td></tr>
<tr><td>A fridge compressor wears out, and $400 of food spoils</td><td>Contents may respond only if a covered peril caused the loss — not age</td><td>Appliance yes, up to the cap; <strong>food spoilage is expressly excluded</strong> as consequential loss (AHS)</td></tr>
<tr><td>Kitchen fire</td><td><strong>Yes</strong> — fire and lightning (TDI)</td><td>No — fire is an excluded breakdown cause (AHS)</td></tr>
<tr><td>River water comes into the ground floor</td><td>No — flooding is excluded; a separate NFIP policy is needed (TDI, FEMA, CRS)</td><td>No</td></tr>
<tr><td>Sewer lateral collapses outside the foundation</td><td>Generally no — not a listed peril; check the policy</td><td>No — expressly excluded (AHS)</td></tr>
<tr><td>A guest is injured on your property and sues</td><td><strong>Yes</strong> — personal liability and medical payments (TDI)</td><td>No such coverage exists in the contract</td></tr>
<tr><td>The house is uninhabitable for a month</td><td><strong>Yes</strong> — additional living expenses (TDI)</td><td>Expressly excluded (AHS)</td></tr>
</tbody></table></div>

<p>The pattern in the middle rows is the one that costs people money. Both contracts can decline a slow leak, and they decline it for opposite reasons: the policy because it was not sudden, the warranty because water damage is an excluded cause and finishes are not restored. Slow damage is the gap in the middle of the two products, and no amount of stacking closes it. The response to a slow leak is the same in both worlds — find it early.</p>

<h2>What it costs where you live</h2>

<h3>United States</h3>

<p>Three numbers define a home warranty's real annual cost, and only the first is advertised: the plan fee, the trade service call fee per request, and the per-item cap. AHS's fee is owed per trade service request, so three requests in a year at $125 add $375 whether or not any of them ends in an approved repair — the contract's second-opinion clause, which charges another fee only if the second opinion agrees with the first, is the clearest evidence that the first fee stands either way.</p>

<p>Set that against the cap. A plan paying at most $3,000 per appliance malfunction, and handing over <em>less</em> than that when the job exceeds the limit, is a device for smoothing mid-sized repairs. It is not protection against a $9,000 HVAC replacement, and it does not behave like a deductible: an insurance deductible is a fixed amount you absorb before the policy pays the rest up to a large limit, whereas a warranty cap is a ceiling on what the provider pays at all.</p>

<h3>United Kingdom</h3>

<p>The UK market does not sell "home warranty" as a category. It sells cover, and British Gas's published pages are a useful specimen because the provider itself distinguishes cover from warranty.</p>

<ul>
<li><strong>Boiler warranty</strong> — "basic cover in case something goes wrong with your new boiler", and it requires an annual boiler service after the first year to stay valid, which is <em>not</em> included. All boilers installed by British Gas require an annual service to remain under warranty.</li>
<li><strong>HomeCare for a new boiler</strong> — from £7 a month in year one with a £60 excess, rising to from £14.50 a month in year two including an annual boiler service "worth £99". With a £0 excess: £13 a month in year one, from £19 in year two. The offer is available only within six months of the installation date; after that you pay from £14.50 or £19 depending on excess.</li>
<li><strong>HomeCare beyond the boiler</strong> — cover for just the boiler and heating is quoted from £22 a month with a £60 excess, including an annual boiler service, unlimited repairs, and all parts and labour. For landlords, HomeCare Three covering boiler, central heating, plumbing and drains is quoted from £15.74 a month, or from £20.00 a month with a Gas Safety Certificate, and includes up to £1,000 per repair to gain access and make good.</li>
</ul>

<p>Two things are worth noticing. The excess is per claim, so a £60 excess is the UK analogue of the American trade service call fee. And the access-and-make-good limit of up to £1,000 per repair mirrors the American contract's $1,000 concrete-access limit — gaining access to a hidden pipe is a cost both markets cap separately from the repair. British Gas also sells a separate Kitchen Appliance Cover, which is the closest thing in its range to an American appliance warranty, and it is a different product again.</p>

<h3>Nigeria</h3>

<p>Nigerian householders' products are peril-based, and the published pages are specific enough to be useful.</p>

<ul>
<li><strong>Leadway Householder Insurance</strong> covers the building, household items and public liability against insured perils including fire, theft, burglary and flood. The page states the premium as "as low as ₦20,000 per year" in its benefits list and "as low as ₦10,000/per year" in its FAQ — the two figures are both on the page, which is itself the argument for getting a quote rather than trusting a headline number. Jewellery, laptops and phones are excluded unless added as extensions at extra premium; furniture and household appliances are covered, as contents against those perils. The plan is available to tenants and landlords, includes alternative accommodation after an incident, and Leadway's own guidance is to insure at a realistic valuation rather than opt for the minimum premium.</li>
<li><strong>AIICO Home Insurance</strong> is structured on a flat premium of ₦10,000 per annum, designed for people in rented apartments covering contents against burglary, fire and special perils: ₦2 million for fire damage to contents only, ₦1 million for burglary, rent for alternative accommodation up to ₦250,000, and personal accident cover for the insured and spouse. Multiple entries are not allowed on the policy.</li>
</ul>

<p>Neither plan lists mechanical breakdown from wear and tear among its perils. That is the honest answer to the American question in a Nigerian context: there is no second contract to compare against, so a worn-out refrigerator is not an insured event. The practical instruments are a manufacturer or retailer service plan on the appliance itself, or self-insurance — a standing repair fund — and the more valuable decision is whether the householder policy's sums insured reflect what the household actually owns, since contents limits of ₦1–2 million will not rebuild a furnished home. Note too that the appliances you would want a warranty for are excluded items on a contents policy unless added: laptops and phones need extensions.</p>

<h2>Which one you actually need</h2>

<p>In decision order, and the order matters more than the answers:</p>

<ol>
<li><strong>Is there a mortgage?</strong> Then insurance is not a choice. TDI: the law does not require it, the lender does.</li>
<li><strong>Is the policy adequate?</strong> Read the declarations page. Check that it is replacement cost rather than actual cash value, that the dwelling limit meets your insurer's requirement — most require at least 80% of replacement cost, some 100% — and that the deductible is one you could actually pay on the worst week of the year.</li>
<li><strong>Is the peril gap filled?</strong> Flood needs a separate NFIP policy in the US and is excluded from standard policies; on the Texas coast wind and hail need TWIA. Neither is a warranty question.</li>
<li><strong>Only then: are the machines old, and would a single failure hurt?</strong> A warranty is a budgeting instrument for aging systems. It earns its fee when the house has original mechanicals, when the failures are mid-sized, and when you would actually call it in rather than pay a local tradesperson.</li>
<li><strong>Can you self-insure the cap?</strong> If a $3,000 repair is absorbable from savings, the plan fee plus per-request fees is a poor trade, and the cap-minus-diagnosis clause means the warranty performs worst exactly when the job is biggest.</li>
<li><strong>Can you meet the maintenance conditions?</strong> Routine maintenance stays yours in the contract, misuse and pest damage are excluded, and mold remediation is excluded. A warranty bought by someone who will not service the equipment is a fee with a dispute attached.</li>
</ol>

<p>Where you live changes step four's shape. In the US, look up your state's provision in the NAIC chart or your own regulator's site before you sign, because it tells you whether a refused claim goes to the insurance department, to a licensing board, or to private arbitration. In the UK the comparison is not warranty-versus-insurance but cover-versus-warranty: price HomeCare against a £99 annual service plus the risk you keep yourself, and check whether your boiler warranty is already conditional on that service. In Nigeria the useful decision is the sum insured on a householder policy, not whether to add a second contract.</p>

<h3>What to check before you sign either one</h3>

<ul>
<li>The <strong>per-item cap</strong> and the <strong>aggregate cap</strong>, and what happens when a job exceeds the per-item cap — AHS pays the limit minus diagnosis and does not do the work.</li>
<li>Whether the fee is <strong>per request or per repair</strong>, and whether it is refunded if the claim is declined.</li>
<li><strong>Access and make-good limits</strong> as separate numbers: $1,000 per term for concrete access in the AHS contract, up to £1,000 per repair in HomeCare Three.</li>
<li>The <strong>re-failure window</strong> — 30 days in the AHS contract — and who chooses the contractor.</li>
<li><strong>Auto-renewal</strong>, and the cancellation refund arithmetic including any administrative fee.</li>
<li>The <strong>dispute clause</strong>: binding arbitration and a class action waiver, or a regulator and the courts.</li>
<li>Whether the item is still under a <strong>manufacturer, builder or extended warranty</strong>, since AHS will not service those.</li>
<li>On the policy side: replacement cost versus actual cash value, the deductible per coverage, the 80% rule, and whether flood or earthquake need separate policies.</li>
</ul>

<h2>One tool that earns its place here</h2>

<p>Contracts are won by word count. Paste the coverage schedule into the <a href="/tech/tool/word-counter/">word counter</a>, then paste the limitations and exclusions section, and compare the two numbers. In the AHS specimen the exclusions are longer than any single coverage list, which is the whole argument in one measurement: the document spends more words on what it will not do than on what it will.</p>

<p>A word count is not a verdict — a short clause can be the one that refuses your claim, and the cap-minus-diagnosis sentence above is only forty words long. It tells you where to read carefully first, and it makes the shape of a contract visible before you have read a line of it. For the recurring-charge half of the problem, the <a href="/tech/subscription-creep-audit/">subscription audit</a> applies unchanged: an auto-renewing plan fee is a subscription with a claims process attached, and <a href="/tech/free-trial-traps/">cancellation windows</a> are where those subscriptions are won or lost.</p>

<h2>What this article does not claim</h2>

<p>No universal statement is being made about home warranties or home insurance, because neither product has universal terms. Specifically: the AHS figures come from a published sample contract carrying a revision date of 14 January 2021, and a customer's actual plan fee, term and trade service call fee are set on their own Contract Agreement pages, which vary by plan and state; current figures come from the provider's quote. The NAIC chart's state entries were last reviewed between February and March 2023, and the NAIC states that the chart is not a legal opinion and that the cited statutes should be consulted. The TDI guide describes Texas policies and says itself that coverages vary by company; other states' guides differ. FEMA and CRS material is about the US National Flood Insurance Program and says nothing about flood cover elsewhere. British Gas prices are "from" prices published on its own pages at the time of checking in September 2026 and vary by property, boiler and excess. The Nigerian figures are the premiums and sums insured published on Leadway's and AIICO's own product pages, and they describe those two plans, not the Nigerian market. Nothing here is legal or financial advice, and no claim is made about any jurisdiction not named.</p>""",
        [("Texas Department of Insurance — Home insurance guide (consumer publication cb025)", "https://tdi.texas.gov/pubs/consumer/cb025.html"),
         ("American Home Shield — Consumer Home Warranty sample contract (revision date 14 January 2021)", "https://cdn.frontdoorhome.com/ahs/ahs-ecom/prod-1b3db460/static/document/DTC_Sample_Contract_Final.pdf"),
         ("NAIC — Model Law Chart PA-60: Service Contracts, Motor Clubs and Other Extended Warranties (state entries reviewed 2/23–3/23)", "https://content.naic.org/sites/default/files/model-law-chart-pa-60-service-contracts-motor-clubs-and-other-extended-warranties.pdf"),
         ("NAIC — Dwelling Fire, Homeowners Owner-Occupied, and Homeowners Tenant and Condominium/Cooperative Unit Owner's Insurance Report (data for 2018)", "https://content.naic.org/article/news-release-naic-releases-homeowners-insurance-report"),
         ("Federal Trade Commission — Warranties, including \"Service Contracts Aren't Warranties\"", "https://consumer.ftc.gov/articles/warranties"),
         ("FEMA — FEMA 511-12, Chapter 11: Flood Insurance", "https://www.fema.gov/pdf/fima/FEMA511-12-Chapter11.pdf"),
         ("Congressional Research Service — A Brief Introduction to the National Flood Insurance Program (IF10988)", "https://www.congress.gov/crs-product/IF10988"),
         ("British Gas — New boiler cover options: HomeCare pricing and how warranty differs from HomeCare", "https://www.britishgas.co.uk/cover/warranty-faqs.html"),
         ("British Gas — Boiler service and maintenance (HomeCare from £22 a month, £60 excess)", "https://www.britishgas.co.uk/heating/boiler-service.html"),
         ("British Gas — HomeCare Three for Landlords (from £15.74 a month; up to £1,000 to gain access and make good)", "https://www.britishgas.co.uk/home-services/landlords/landlord-home-and-boiler-cover/HC3CP12/"),
         ("Leadway Assurance — Householder Insurance", "https://www.leadway.com/householder/"),
         ("AIICO — Home Insurance plan", "https://www.aiicoplc.com/home/home-insurance-plan")],
        [("subscription-creep-audit", "How to actually audit every subscription you're paying for"),
         ("free-trial-traps", "Free trial traps: the cancellation mistakes that cost real money"),
         ("web-hosting-costs-explained", "Web hosting costs explained: the true 3-year price"),
         ("smart-home-worth-it", "Smart home devices that are worth it vs. the gimmicks"),
         ("refurbished-vs-new-tech", "Refurbished vs new: when refurbished is the smarter buy")],
    ),
]
