# -*- coding: utf-8 -*-
"""home_sources_data.py — external source system for BRYME Home & DIY (brief §12).

HOME_SOURCES: slug -> list of (url, publisher-label). Every URL was fetched and
status-checked on 2026-09-25 before shipping; the sweep re-verifies each batch.
Sources are authoritative bodies only — regulators, public-health agencies,
government guidance, standards institutes — never affiliate or commercial pages.
(403 from a CDN bot-guard counts as reachable; 404/410 are never shipped.)
"""

HOME_SOURCES = {
    # ---- energy & bills ----
    "why-is-my-electric-bill-so-high": [
        ("https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php", "U.S. EIA — electricity use in homes"),
        ("https://www.ofgem.gov.uk/", "Ofgem — the GB energy regulator"),
    ],
    "energy-bill-high-unchanged": [
        ("https://www.ofgem.gov.uk/", "Ofgem — the GB energy regulator"),
        ("https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php", "U.S. EIA — electricity use in homes"),
    ],
    "thermostat-settings-that-save-money": [
        ("https://energysavingtrust.org.uk/advice/heating-controls/", "Energy Saving Trust — heating controls"),
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
    ],
    "off-peak-electricity-tariffs-explained": [
        ("https://www.ofgem.gov.uk/", "Ofgem — the GB energy regulator"),
        ("https://energysavingtrust.org.uk/", "Energy Saving Trust"),
    ],
    "smart-thermostat-payback": [
        ("https://energysavingtrust.org.uk/advice/heating-controls/", "Energy Saving Trust — heating controls"),
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
    ],
    "solar-panels-worth-it-2026": [
        ("https://energysavingtrust.org.uk/advice/solar-panels/", "Energy Saving Trust — solar panels"),
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
    ],
    "uk-insulation-grants": [
        ("https://www.gov.uk/improve-energy-efficiency", "GOV.UK — improving your home's energy efficiency"),
        ("https://www.ofgem.gov.uk/", "Ofgem — the GB energy regulator"),
    ],
    "attic-insulation-basics": [
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
        ("https://energysavingtrust.org.uk/", "Energy Saving Trust"),
    ],
    "single-glazing-payback": [
        ("https://energysavingtrust.org.uk/advice/windows-and-doors/", "Energy Saving Trust — energy efficient windows and doors"),
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
    ],
    "draught-proofing-mistakes": [
        ("https://energysavingtrust.org.uk/advice/draught-proofing/", "Energy Saving Trust — draught-proofing"),
        ("https://energysavingtrust.org.uk/", "Energy Saving Trust"),
    ],
    "epc-rating-explained": [
        ("https://www.gov.uk/buy-sell-your-home/energy-performance-certificates", "GOV.UK — Energy Performance Certificates"),
    ],
    "cost-to-run-air-conditioning": [
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
        ("https://www.eia.gov/energyexplained/use-of-energy/", "U.S. EIA — energy use explained"),
    ],
    "second-fridge-freezer-cost": [
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
        ("https://www.energystar.gov/products/refrigerators", "ENERGY STAR — refrigerators"),
    ],
    "standby-power-real-numbers-your-meter": [
        ("https://www.eia.gov/energyexplained/use-of-energy/electricity-use-in-homes.php", "U.S. EIA — electricity use in homes"),
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
    ],
    "heat-pump-vs-gas-furnace": [
        ("https://energysavingtrust.org.uk/advice/heat-pumps/", "Energy Saving Trust — heat pumps"),
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
    ],
    "which-heating-system": [
        ("https://energysavingtrust.org.uk/advice/heat-pumps/", "Energy Saving Trust — heat pumps"),
        ("https://energysavingtrust.org.uk/advice/heating-controls/", "Energy Saving Trust — heating controls"),
        ("https://www.energy.gov/save/home-upgrades", "U.S. DOE — home energy upgrades"),
    ],
    "uk-boiler-servicing": [
        ("https://www.gassaferegister.co.uk/consumer-advice/", "Gas Safe Register — consumer advice"),
        ("https://www.hse.gov.uk/gas/", "HSE — gas safety"),
    ],
    "how-to-bleed-a-radiator": [
        ("https://energysavingtrust.org.uk/advice/heating-controls/", "Energy Saving Trust — heating controls"),
        ("https://www.hse.gov.uk/gas/domestic/index.htm", "HSE — domestic gas safety"),
    ],
    # ---- fire, gas, electrical safety ----
    "electrical-fire-warning-signs": [
        ("https://www.electricalsafetyfirst.org.uk/guides-and-advice/around-the-home/", "Electrical Safety First — guides and advice"),
        ("https://www.hse.gov.uk/electricity/", "HSE — electricity safety"),
    ],
    "outlet-overloading-danger": [
        ("https://www.electricalsafetyfirst.org.uk/guides-and-advice/around-the-home/", "Electrical Safety First — guides and advice"),
        ("https://www.hse.gov.uk/electricity/", "HSE — electricity safety"),
    ],
    "wiring-red-flags-in-your-home": [
        ("https://www.electricalsafetyfirst.org.uk/guides-and-advice/around-the-home/", "Electrical Safety First — guides and advice"),
        ("https://www.hse.gov.uk/electricity/", "HSE — electricity safety"),
    ],
    "electric-shock-first-response": [
        ("https://www.hse.gov.uk/electricity/", "HSE — electricity safety"),
    ],
    "co-smoke-alarm-expiry": [
        ("https://www.nfpa.org/news-blogs-and-articles/blogs/2023/03/06/what-kind-of-smoke-alarm-smoke-detector-should-i-buy", "NFPA — what kind of smoke alarm should I buy"),
        ("https://www.gov.uk/firekills", "GOV.UK — Fire Kills campaign"),
    ],
    "how-many-smoke-co-alarms": [
        ("https://www.gov.uk/firekills", "GOV.UK — Fire Kills campaign"),
        ("https://www.nfpa.org/news-blogs-and-articles/blogs/2023/03/06/what-kind-of-smoke-alarm-smoke-detector-should-i-buy", "NFPA — what kind of smoke alarm should I buy"),
    ],
    "test-alarms-monthly": [
        ("https://www.gov.uk/firekills", "GOV.UK — Fire Kills campaign"),
        ("https://www.nfpa.org/news-blogs-and-articles/blogs/2023/03/06/what-kind-of-smoke-alarm-smoke-detector-should-i-buy", "NFPA — what kind of smoke alarm should I buy"),
    ],
    "uk-carbon-monoxide-alarm-law": [
        ("https://www.nhs.uk/conditions/carbon-monoxide-poisoning/", "NHS — carbon monoxide poisoning"),
        ("https://www.hse.gov.uk/gas/", "HSE — gas safety"),
    ],
    "cooking-oil-fire-plan": [
        ("https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/cooking/", "USFA — cooking fire safety"),
        ("https://www.gov.uk/firekills", "GOV.UK — Fire Kills campaign"),
    ],
    "dryer-lint-every-load": [
        ("https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/", "USFA — home fire prevention"),
        ("https://www.gov.uk/firekills", "GOV.UK — Fire Kills campaign"),
    ],
    # ---- damp, mould, air ----
    "condensation-vs-rising-vs-penetrating-damp": [
        ("https://www.nhs.uk/common-health-questions/lifestyle/can-damp-and-mould-affect-my-health/", "NHS — can damp and mould affect my health?"),
        ("https://www.epa.gov/mold", "U.S. EPA — mold"),
    ],
    "bathroom-grout-mould": [
        ("https://www.epa.gov/mold", "U.S. EPA — mold"),
        ("https://www.nhs.uk/common-health-questions/lifestyle/can-damp-and-mould-affect-my-health/", "NHS — can damp and mould affect my health?"),
    ],
    "mould-after-a-flooded-room": [
        ("https://www.epa.gov/mold", "U.S. EPA — mold"),
        ("https://www.cdc.gov/mold/index.html", "CDC — mold"),
    ],
    "painting-over-damp": [
        ("https://www.epa.gov/mold", "U.S. EPA — mold"),
        ("https://www.nhs.uk/common-health-questions/lifestyle/can-damp-and-mould-affect-my-health/", "NHS — can damp and mould affect my health?"),
    ],
    "uk-landlord-damp-mould-duties": [
        ("https://www.gov.uk/government/publications/damp-and-mould-understanding-and-addressing-the-health-risks-for-rented-housing-providers", "GOV.UK — damp and mould: health risks guidance for rented housing providers"),
        ("https://www.nhs.uk/common-health-questions/lifestyle/can-damp-and-mould-affect-my-health/", "NHS — can damp and mould affect my health?"),
    ],
    "condensation-ventilation-that-works": [
        ("https://www.epa.gov/indoor-air-quality-iaq", "U.S. EPA — indoor air quality"),
        ("https://www.nhs.uk/common-health-questions/lifestyle/can-damp-and-mould-affect-my-health/", "NHS — can damp and mould affect my health?"),
    ],
    # ---- water ----
    "water-damage-insurance-coverage": [
        ("https://www.abi.org.uk/products-and-issues/choosing-the-right-insurance/home-insurance/", "ABI — home insurance"),
        ("https://consumer.ftc.gov/", "U.S. FTC — consumer advice"),
    ],
    "hidden-water-leak-meter-test": [
        ("https://www.epa.gov/watersense", "U.S. EPA WaterSense"),
    ],
    "water-storage-safety": [
        ("https://www.who.int/news-room/fact-sheets/detail/drinking-water", "WHO — drinking-water fact sheet"),
        ("https://www.cdc.gov/healthywater/drinking/index.html", "CDC — drinking water"),
    ],
    "borehole-water-and-your-kettle": [
        ("https://www.who.int/news-room/fact-sheets/detail/drinking-water", "WHO — drinking-water fact sheet"),
    ],
    # ---- pests ----
    "bedbugs-first-signs": [
        ("https://www.epa.gov/bedbugs", "U.S. EPA — bed bugs"),
        ("https://www.nhs.uk/conditions/bedbugs/", "NHS — bedbugs"),
    ],
    "rats-in-the-house": [
        ("https://www.pestworld.org/pest-guide/rodents/rats/", "NPMA — rats"),
    ],
    "wasp-nest-first-response": [
        ("https://www.pestworld.org/pest-guide/stinging-pests/wasps/", "NPMA — wasps"),
    ],
    "compound-mosquito-control-night": [
        ("https://www.cdc.gov/mosquitoes/prevent-bites/index.html", "CDC — prevent mosquito bites"),
        ("https://www.who.int/news-room/fact-sheets/detail/malaria", "WHO — malaria fact sheet"),
    ],
    # ---- money: rent, buy, insurance ----
    "rent-vs-buy-explained": [
        ("https://www.consumerfinance.gov/consumer-tools/buying-a-house/", "CFPB — buying a house"),
        ("https://www.gov.uk/stamp-duty-land-tax", "GOV.UK — Stamp Duty Land Tax"),
    ],
    "rent-or-buy-tool": [
        ("https://www.gov.uk/stamp-duty-land-tax", "GOV.UK — Stamp Duty Land Tax"),
        ("https://www.consumerfinance.gov/consumer-tools/buying-a-house/", "CFPB — buying a house"),
    ],
    "mortgage-payments-explained": [
        ("https://www.consumerfinance.gov/consumer-tools/mortgages/", "CFPB — mortgages"),
        ("https://www.gov.uk/support-for-mortgage-interest", "GOV.UK — Support for Mortgage Interest"),
    ],
    "fence-shed-insurance": [
        ("https://www.abi.org.uk/products-and-issues/choosing-the-right-insurance/home-insurance/", "ABI — home insurance"),
    ],
    "unpermitted-work-insurance": [
        ("https://www.gov.uk/building-regulations-approval", "GOV.UK — building regulations approval"),
    ],
    "hvac-diy-warranty-rules": [
        ("https://consumer.ftc.gov/consumer-alerts/2023/02/so-whats-deal-home-warranties", "U.S. FTC — so what's the deal with home warranties?"),
        ("https://consumer.ftc.gov/", "U.S. FTC — consumer advice"),
    ],
    # ---- smart home & security ----
    "smart-locks-cameras-worth-it": [
        ("https://www.ncsc.gov.uk/collection/device-security-guidance", "NCSC — device security guidance"),
        ("https://consumer.ftc.gov/", "U.S. FTC — consumer advice"),
    ],
    "smart-home-devices-worth-it": [
        ("https://www.ncsc.gov.uk/collection/device-security-guidance", "NCSC — device security guidance"),
    ],
    "renter-security": [
        ("https://www.met.police.uk/a/your-advice/crime-prevention/home-safety/", "Metropolitan Police — home safety advice"),
    ],
}
