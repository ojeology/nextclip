# Fitness desk — curated external source map (batch 2, 2026-09-25 sweep).
# Every URL below was fetched and verified on 2026-09-25: status 200, or
# 403/429 bot-gates that return the page to normal browsers (CDC, Mayo,
# Examine). Pages that keep the default WHO + CDC pair are deliberately
# not listed here. Primary/public-health bodies first; no commercial
# symptom-checker or SEO-farm links.

WHO_PA = ("WHO — Physical activity (fact sheet)",
          "https://www.who.int/news-room/fact-sheets/detail/physical-activity")
WHO_DIET = ("WHO — Healthy diet (fact sheet)",
            "https://www.who.int/news-room/fact-sheets/detail/healthy-diet")
CDC_PA = ("CDC — Physical Activity Basics",
          "https://www.cdc.gov/physical-activity-basics/")
CDC_ST = ("CDC — Adding Strength Training",
          "https://www.cdc.gov/physical-activity-basics/adding-strength-training/index.html")
CDC_SLEEP = ("CDC — About Sleep",
             "https://www.cdc.gov/sleep/about/index.html")
NHS_EX = ("NHS — Exercise (Live Well)",
          "https://www.nhs.uk/live-well/exercise/")
NHS_SLEEP = ("NHS — How to get to sleep",
             "https://www.nhs.uk/live-well/sleep-and-tiredness/how-to-get-to-sleep/")
MAYO_ST = ("Mayo Clinic — Strength training: Get stronger, leaner, healthier",
           "https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/strength-training/art-20046670")
FDA_CAFF = ("US FDA — Spilling the Beans: How Much Caffeine Is Too Much?",
            "https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much")
FDA_GLP1 = ("US FDA — Update on FDA's ongoing evaluation of GLP-1 receptor agonists (incl. approved-medicines table)",
            "https://www.fda.gov/drugs/drug-safety-communications/update-fdas-ongoing-evaluation-reports-suicidal-thoughts-or-actions-patients-taking-certain-type")
NIDDK_WM = ("NIH NIDDK — Weight Management",
            "https://www.niddk.nih.gov/health-information/weight-management")
NIDDK_PROG = ("NIH NIDDK — Choosing a Safe and Successful Weight-Loss Program",
              "https://www.niddk.nih.gov/health-information/weight-management/choosing-a-safe-successful-weight-loss-program")
ODS_EX = ("NIH ODS — Dietary Supplements for Exercise and Athletic Performance (health professional fact sheet)",
          "https://ods.od.nih.gov/factsheets/ExerciseAndAthleticPerformance-HealthProfessional/")
HARV_PROT = ("Harvard T.H. Chan School of Public Health — Protein",
             "https://nutritionsource.hsph.harvard.edu/what-should-you-eat/protein/")
HARV_SUPP = ("Harvard T.H. Chan School of Public Health — Workout Supplements",
             "https://nutritionsource.hsph.harvard.edu/workout-supplements/")
EXAMINE_PROT = ("Examine — Protein intake guide (Morton et al. meta-analysis breakpoint)",
                "https://examine.com/guides/protein-intake/")

FIT_PAGE_SOURCES = {
    # --- protein & nutrition (YMYL: highest source priority) ---
    "how-much-protein-do-you-need": [HARV_PROT, EXAMINE_PROT],
    "protein-timing-anabolic-window": [HARV_PROT, ODS_EX],
    "protein-before-bed": [HARV_PROT, ODS_EX],
    "protein-foods-nigeria": [WHO_DIET, HARV_PROT],
    "what-to-eat-after-a-workout": [ODS_EX, WHO_DIET],
    "what-to-eat-before-a-workout": [CDC_PA, WHO_DIET],
    "benefits-of-walking-after-meals": [CDC_PA, WHO_DIET],
    "how-much-water-to-drink-a-day": [CDC_PA, WHO_PA],
    # --- supplements (YMYL) ---
    "creatine-explained": [ODS_EX, HARV_SUPP],
    "caffeine-side-effects": [FDA_CAFF, ODS_EX],
    "downside-of-stimulants": [FDA_CAFF, ODS_EX, HARV_SUPP],
    "supplements-waste-of-money": [ODS_EX, HARV_SUPP],
    "testosterone-booster-truth": [ODS_EX, HARV_SUPP],
    # --- sleep & recovery (YMYL) ---
    "sleep-and-exercise-performance": [CDC_SLEEP, NHS_SLEEP, WHO_PA],
    "benefits-of-sleeping-well": [NHS_SLEEP, CDC_SLEEP],
    # --- strength & training ---
    "how-much-muscle-can-you-gain": [MAYO_ST, CDC_ST, WHO_PA],
    "how-many-reps-for-muscle": [MAYO_ST, CDC_ST],
    "squat-form-beginners": [MAYO_ST, CDC_ST, NHS_EX],
    "push-up-progression": [MAYO_ST, NHS_EX],
    "bodyweight-moves-that-matter": [MAYO_ST, NHS_EX],
    "workout-split-beginners": [MAYO_ST, CDC_ST, NHS_EX],
    "deload-weeks-explained": [CDC_ST, MAYO_ST],
    "cardio-or-weights-first": [WHO_PA, CDC_ST],
    "beginner-running-plan": [NHS_EX, CDC_PA],
    # --- gym onboarding ---
    "how-to-start-going-to-the-gym": [NHS_EX, CDC_PA],
    "gym-anxiety-beginners": [NHS_EX, CDC_PA],
    # --- weight (YMYL) ---
    "30-day-weight-loss-programme": [NIDDK_PROG, CDC_PA],
    "intermittent-fasting-honest-guide": [NIDDK_WM, WHO_DIET],
}
