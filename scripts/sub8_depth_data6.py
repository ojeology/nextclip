# -*- coding: utf-8 -*-
"""Editorial depth sections, part 6: fitness desk, first half of the 9.0-9.4 band.
Each page is 13-162 words short of the 750-word bar.
Every external URL curl-verified 200 at authoring time."""

WHO = "https://www.who.int/"
MEDLINE = "https://medlineplus.gov/"
NHS = "https://www.nhs.uk/"
NICE = "https://www.nice.org.uk/"
ACSM = "https://www.acsm.org/"
NIDDK = "https://www.niddk.nih.gov/"
BH = "https://www.betterhealth.vic.gov.au/"

def _w(q):
    return "https://en.wikipedia.org/wiki/Special:Search?search=" + q

DEPTH_SECTIONS6 = {

"fitness/weight":
    "<h2>How this section approaches body weight</h2>"
    "<p>Body weight is the most-measured and least-understood number in fitness, because it responds to water, glycogen, food volume and sleep as readily as to fat. This section treats the scale as a trend instrument rather than a verdict, which is the only way it produces useful information. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the guidance on healthy weight this desk follows. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>The reading rules</h2>"
    "<ul>"
    "<li><b>Weigh at the same point in the day.</b> Morning, before food and drink, removes most of the variation.</li>"
    "<li><b>Judge the week, not the day.</b> A single reading cannot distinguish fat change from water.</li>"
    "<li><b>Expect an early rise.</b> Starting training often increases weight in the first fortnight as muscle stores more glycogen and water.</li>"
    "<li><b>Use other measures alongside it.</b> Measurements, photographs and performance all move on different schedules from the scale.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/how-much-protein-do-you-need/\">how much protein you need</a>, <a href=\"/fitness/strength-training-while-losing-weight/\">strength training while losing weight</a> and <a href=\"/fitness/how-to-measure-fitness-progress-explained/\">how to measure progress</a>.</p>",

"fitness/progressive-overload-without-adding-weight-explained":
    "<h2>Load is one variable among several</h2>"
    "<p>Progressive overload means increasing the demand on the body over time, and load is only the most obvious way to do it. When weight cannot increase &mdash; through equipment limits, joint tolerance or a training break &mdash; the other variables still produce adaptation. <a href=\"" + ACSM + "\" rel=\"noopener\">The American College of Sports Medicine</a> publishes the resistance-training principles behind this page. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>The variables that are not load</h2>"
    "<ul>"
    "<li><b>Volume.</b> More repetitions or more sets at the same load is a genuine increase in demand.</li>"
    "<li><b>Density.</b> The same work in less rest is harder, and it trains a different capacity.</li>"
    "<li><b>Range of motion.</b> A deeper repetition at the same load does more mechanical work.</li>"
    "<li><b>Leverage.</b> Changing the position of a bodyweight movement changes the load without changing the equipment.</li>"
    "<li><b>Tempo.</b> Slower eccentric phases increase time under tension at identical load.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/how-progressive-overload-works/\">how progressive overload works</a>, <a href=\"/fitness/tempo-training-explained/\">tempo training</a> and <a href=\"/fitness/how-many-reps-for-muscle/\">how many reps for muscle</a>.</p>",

"fitness/rpe-and-rir-explained":
    "<h2>Two scales for the same judgement</h2>"
    "<p>RPE rates how hard a set felt; RPE's close relative, reps in reserve, estimates how many more repetitions were available. Both are subjective, and both are useful precisely because they adapt to how you are performing on the day rather than to a fixed number. <a href=\"" + ACSM + "\" rel=\"noopener\">The American College of Sports Medicine</a> publishes the intensity-guidance framework these scales sit within. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>Using them without fooling yourself</h2>"
    "<ul>"
    "<li><b>Calibrate against failure occasionally.</b> Without an occasional true limit, estimates drift optimistic.</li>"
    "<li><b>Keep most sets short of failure.</b> Training every set to zero reserve costs recovery that the adaptation does not repay.</li>"
    "<li><b>Apply them per set, not per session.</b> A session average hides the sets that were too easy.</li>"
    "<li><b>Record them.</b> An unrecorded RPE cannot be compared with last week's, which removes most of the value.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/how-many-reps-for-muscle/\">how many reps for muscle</a>, <a href=\"/fitness/deload-weeks-explained/\">deload weeks</a> and <a href=\"/fitness/rest-between-sets-explained/\">rest between sets</a>.</p>",

"fitness/30-day-walking-plan":
    "<h2>A plan built on consistency, not intensity</h2>"
    "<p>Walking plans succeed where harder programmes fail because the barrier to each session is low, and adherence over thirty days matters more than the intensity of any single walk. The structure here increases duration gradually and includes easier days deliberately. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the physical-activity guidelines on which the weekly volumes are based. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>Making the month work</h2>"
    "<ul>"
    "<li><b>Attach walks to existing routine.</b> A walk tied to a commute or a meal survives schedule pressure; one that needs a free hour does not.</li>"
    "<li><b>Take the easy days.</b> They are part of the plan and removing them is the commonest way to abandon it in week two.</li>"
    "<li><b>Count minutes, not steps.</b> Step totals vary with stride and terrain and make progress harder to see.</li>"
    "<li><b>Expect the third week to be hardest.</b> Novelty has worn off and results are not yet visible.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/beginner-running-plan/\">the beginner running plan</a>, <a href=\"/fitness/how-many-steps-a-day/\">how many steps a day</a> and <a href=\"/fitness/walking-vs-running/\">walking versus running</a>.</p>",

"fitness/kit":
    "<h2>Most equipment is optional, and that is the point</h2>"
    "<p>The useful question about kit is not what is available but what removes a barrier to training. Anything that makes a session less likely to happen is a cost regardless of price, and most home programmes need far less than the marketing implies. The <a href=\"" + NHS + "\" rel=\"noopener\">NHS</a> publishes guidance on getting active without a gym. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What is actually worth buying</h2>"
    "<ul>"
    "<li><b>Shoes suited to the activity.</b> The one item where the wrong choice causes problems rather than merely discomfort.</li>"
    "<li><b>Adjustable resistance.</b> A set of bands or adjustable dumbbells covers most home training in a small space.</li>"
    "<li><b>A mat.</b> Cheap, and it determines whether floor work happens at all.</li>"
    "<li><b>Something to track with.</b> A notebook is sufficient; the requirement is a record, not a device.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/home-gym-essentials-budget/\">home gym essentials on a budget</a>, <a href=\"/fitness/resistance-bands-guide/\">the resistance bands guide</a> and <a href=\"/fitness/how-to-choose-running-shoes/\">how to choose running shoes</a>.</p>",

"fitness/drop-sets-and-rest-pause-explained":
    "<h2>Intensity techniques buy fatigue, not necessarily growth</h2>"
    "<p>Drop sets and rest-pause extend a set beyond the point where it would otherwise stop, which increases fatigue substantially. Whether that extra fatigue produces extra adaptation is the question, and the honest answer is that these are tools for adding stimulus when volume and load cannot increase further &mdash; not a substitute for them. <a href=\"" + ACSM + "\" rel=\"noopener\">The American College of Sports Medicine</a> publishes the resistance-training guidance on advanced techniques. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>Using them sensibly</h2>"
    "<ul>"
    "<li><b>Apply to some sets, not all.</b> Every set taken past failure costs recovery out of proportion to the benefit.</li>"
    "<li><b>Prefer them on machines and isolation work.</b> Technical movements degrade badly under fatigue, which raises injury risk.</li>"
    "<li><b>Keep a record of the total work.</b> Without it, the technique becomes a way to feel tired rather than to progress.</li>"
    "<li><b>Deliberately deload after heavy use.</b> Accumulated fatigue from intensity work is easy to miss until performance drops.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/supersets-vs-circuits-explained/\">supersets versus circuits</a>, <a href=\"/fitness/deload-weeks-explained/\">deload weeks</a> and <a href=\"/fitness/rpe-and-rir-explained/\">RPE and RIR</a>.</p>",

"fitness/muscle-on-glp1-weight-loss-drugs":
    "<h2>Weight loss on these drugs is not only fat</h2>"
    "<p>Rapid weight loss of any cause includes lean tissue, and the proportion depends heavily on whether the person is doing resistance training and eating adequate protein during the loss. This is the part of treatment that is least often addressed and most consequential for what happens afterwards. <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the clinical reference material on these medicines. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What protects lean mass</h2>"
    "<ul>"
    "<li><b>Resistance training, consistently.</b> The strongest single factor in preserving muscle during a calorie deficit.</li>"
    "<li><b>Protein at the upper end.</b> Appetite suppression makes hitting a target harder, not less necessary.</li>"
    "<li><b>A moderate rather than maximal deficit.</b> Faster loss costs proportionally more lean tissue.</li>"
    "<li><b>A plan for after.</b> The behaviours that maintained muscle during the loss are the ones that prevent regain.</li>"
    "</ul>"
    "<p>These medicines are prescribed treatments; the desk's guidance does not replace the prescriber's. See <a href=\"/fitness/keeping-weight-off-after-glp1/\">keeping weight off after GLP-1</a>, <a href=\"/fitness/glp1-workout-plan-for-beginners/\">the GLP-1 workout plan</a> and <a href=\"/fitness/strength-training-while-losing-weight/\">strength training while losing weight</a>.</p>",

"fitness/gym-acronyms-explained":
    "<h2>The vocabulary is a barrier, and it is a low one</h2>"
    "<p>Gym abbreviations are shorthand rather than jargon with hidden meaning, and learning two dozen of them removes most of the confusion in a programme. They also compress information: a notation like 3x10 at RPE 8 specifies volume, reps and effort in a few characters. <a href=\"" + ACSM + "\" rel=\"noopener\">The American College of Sports Medicine</a> publishes the standard terminology used in exercise prescription. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>The ones worth knowing first</h2>"
    "<ul>"
    "<li><b>Sets and reps notation.</b> The first number is sets, the second repetitions per set.</li>"
    "<li><b>RPE and RIR.</b> Effort ratings, covered in full on their own page.</li>"
    "<li><b>RM.</b> The maximum load for a given number of repetitions.</li>"
    "<li><b>Tempo notation.</b> Four digits describing the phases of a repetition, read in seconds.</li>"
    "<li><b>AMRAP and EMOM.</b> Session structures used in conditioning work.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/what-does-3x10-mean-explained/\">what 3x10 means</a>, <a href=\"/fitness/rpe-and-rir-explained/\">RPE and RIR</a> and <a href=\"/fitness/tempo-training-explained/\">tempo training</a>.</p>",

"fitness/tempo-training-explained":
    "<h2>Tempo describes how long, not how much</h2>"
    "<p>Tempo training specifies the duration of each phase of a repetition, most often slowing the lowering phase. It is a way of increasing demand without increasing load, which makes it useful when joints will not tolerate more weight or when equipment is limited. <a href=\"" + ACSM + "\" rel=\"noopener\">The American College of Sports Medicine</a> publishes the guidance on repetition speed in resistance training. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>Reading and applying the notation</h2>"
    "<ul>"
    "<li><b>Four digits, in order.</b> Lowering, pause at the bottom, lifting, pause at the top, each in seconds.</li>"
    "<li><b>The eccentric is the part worth slowing.</b> It is where most of the mechanical tension occurs.</li>"
    "<li><b>Expect the load to fall.</b> A slower repetition at the same weight is harder, so the working load drops.</li>"
    "<li><b>Do not exaggerate the pause.</b> Very long pauses shift the stimulus toward starting strength rather than tension.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/time-under-tension-explained/\">time under tension</a>, <a href=\"/fitness/how-many-reps-for-muscle/\">how many reps for muscle</a> and <a href=\"/fitness/progressive-overload-without-adding-weight-explained/\">overload without adding weight</a>.</p>",

"fitness/heart-rate-zone-calculator":
    "<h2>Zones are a guide to intensity, not a rule</h2>"
    "<p>Heart-rate zones divide effort into bands derived from an estimated maximum. The estimate is where the weakness lies: the standard formula has a wide margin of error between individuals, so zones calculated from it are a starting point rather than a personal measurement. <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the reference material on target heart rate. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>Using the output well</h2>"
    "<ul>"
    "<li><b>Treat the zones as relative.</b> What matters is that harder work produces a higher reading, not the absolute boundary.</li>"
    "<li><b>Calibrate against perceived effort.</b> If a zone feels wrong, the estimate is wrong, not the sensation.</li>"
    "<li><b>Account for medication and caffeine.</b> Both shift heart rate at a given effort.</li>"
    "<li><b>Do not chase the number.</b> Training to a zone rather than to the session's purpose inverts the priority.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/heart-rate-zones-explained/\">heart rate zones explained</a>, <a href=\"/fitness/zone-2-cardio-explained/\">zone 2 cardio</a> and <a href=\"/fitness/vo2-max-explained/\">VO2 max explained</a>. This calculator runs in your browser and stores nothing.</p>",

"fitness/exercising-with-arthritis-explained":
    "<h2>Movement helps; the type and dose decide how much</h2>"
    "<p>Exercise is part of management rather than a risk in most forms of arthritis, and the evidence for it is stronger than for several other interventions. What varies is which movements suit which joints, and how the load is introduced. <a href=\"" + NHS + "\" rel=\"noopener\">The NHS</a> publishes the guidance on exercise with arthritis, and <a href=\"" + NICE + "\" rel=\"noopener\">NICE</a> publishes the clinical guideline. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>The principles that hold across types</h2>"
    "<ul>"
    "<li><b>Start low and progress slowly.</b> A flare after a large increase is a dosing problem rather than a sign to stop.</li>"
    "<li><b>Strength matters as much as mobility.</b> Muscle around a joint reduces the load the joint carries.</li>"
    "<li><b>Distinguish pain during from pain after.</b> Brief discomfort during movement differs from pain that persists and worsens.</li>"
    "<li><b>Keep moving on bad days, at lower intensity.</b> Complete rest tends to make the next session harder.</li>"
    "</ul>"
    "<p>This page is general information, not medical advice. See <a href=\"/fitness/mobility-after-40-explained/\">mobility after 40</a>, <a href=\"/fitness/strength-training-for-beginners/\">strength training for beginners</a> and <a href=\"/fitness/mobility-vs-flexibility/\">mobility versus flexibility</a>.</p>",

"fitness/bodybuilding-must-know":
    "<h2>The fundamentals survive every trend</h2>"
    "<p>Bodybuilding advice cycles constantly, and almost all of the disagreement is at the margins. The variables that determine results are few, well established, and unchanged for decades; most of what is new concerns optimisation of things that matter little. <a href=\"" + ACSM + "\" rel=\"noopener\">The American College of Sports Medicine</a> publishes the resistance-training principles this page is built on. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What actually determines the outcome</h2>"
    "<ul>"
    "<li><b>Progressive overload over months.</b> Not weeks, and not sessions &mdash; the trend across months is the signal.</li>"
    "<li><b>Volume within a recoverable range.</b> More is better up to a point, then it is worse.</li>"
    "<li><b>Protein and total intake.</b> Nutrition sets the ceiling on what training can produce.</li>"
    "<li><b>Sleep.</b> The largest recovery variable, and the one most often sacrificed for an extra session.</li>"
    "<li><b>Time.</b> Visible change takes longer than most programmes imply, which is why so many are abandoned early.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/bulking-and-cutting-explained/\">bulking and cutting</a>, <a href=\"/fitness/how-much-muscle-can-you-gain/\">how much muscle you can gain</a> and <a href=\"/fitness/workout-split-beginners/\">workout splits for beginners</a>.</p>",

"fitness/library":
    "<h2>An exercise library is a lookup, not a programme</h2>"
    "<p>The entries here describe how to perform each movement and what it targets. What they cannot do is assemble a programme, because that depends on your history, equipment and goals &mdash; and a library consulted without a plan produces a session with no progression behind it. <a href=\"" + ACSM + "\" rel=\"noopener\">The American College of Sports Medicine</a> publishes the exercise-classification framework used here. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>How to use it well</h2>"
    "<ul>"
    "<li><b>Pick by pattern, not by muscle.</b> Push, pull, hinge, squat and carry cover most of what a programme needs.</li>"
    "<li><b>Choose variants you can load progressively.</b> A movement you cannot add weight to has a limited useful life.</li>"
    "<li><b>Learn the brace before the load.</b> Technique at light weight transfers; technique at heavy weight does not.</li>"
    "<li><b>Keep the selection small.</b> Proficiency in eight movements beats familiarity with thirty.</li>"
    "</ul>"
    "<p>Start with <a href=\"/fitness/exercise-library/\">the full library</a>, then <a href=\"/fitness/exercise-library-push/\">push</a>, <a href=\"/fitness/exercise-library-pull/\">pull</a>, <a href=\"/fitness/exercise-library-legs/\">legs</a> and <a href=\"/fitness/exercise-library-core/\">core</a>.</p>",

"fitness/plans":
    "<h2>A plan is a schedule with a progression rule</h2>"
    "<p>Most published plans specify what to do and not how to advance, which is why they stop working after a few weeks. The plans here state both: the weekly structure and the rule for increasing demand when the current week becomes easy. <a href=\"" + ACSM + "\" rel=\"noopener\">The American College of Sports Medicine</a> publishes the programming principles behind them. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>Choosing one that fits</h2>"
    "<ul>"
    "<li><b>Match the frequency to your real week.</b> A four-day plan done twice is worse than a two-day plan done twice.</li>"
    "<li><b>Check the equipment requirement first.</b> Substitutions mid-session usually mean the wrong plan was chosen.</li>"
    "<li><b>Read the progression rule.</b> If there is none, the plan is a routine rather than a programme.</li>"
    "<li><b>Plan the deload.</b> Programmes without scheduled reductions accumulate fatigue until performance drops.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/workout-split-beginners/\">workout splits for beginners</a>, <a href=\"/fitness/strength-training-for-beginners/\">strength training for beginners</a>, <a href=\"/fitness/workout-builder/\">the workout builder</a> and <a href=\"/fitness/weekly-planner/\">the weekly planner</a>.</p>",

"fitness/push-up-progression":
    "<h2>Change the leverage, not the effort</h2>"
    "<p>A push-up progression works by altering how much body weight the arms support, which means every stage is a genuine push-up rather than a different exercise. That continuity is what makes the progression transferable: the movement pattern stays constant while the demand rises. <a href=\"" + NHS + "\" rel=\"noopener\">The NHS</a> publishes strength guidance for beginners that includes push-up variations. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>Moving through the stages</h2>"
    "<ul>"
    "<li><b>Incline before knees.</b> A raised-hand push-up keeps the body rigid and trains the same pattern as the full version.</li>"
    "<li><b>Advance on control, not on strain.</b> A stage is complete when the repetitions are clean, not when the last one is survived.</li>"
    "<li><b>Keep the hips with the shoulders.</b> A sagging position removes the work from the muscles being trained.</li>"
    "<li><b>Add load before adding endless repetitions.</b> Beyond roughly twenty, added resistance progresses strength better than volume.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/pull-up-progression-explained/\">the pull-up progression</a>, <a href=\"/fitness/bodyweight-moves-that-matter/\">bodyweight moves that matter</a> and <a href=\"/fitness/exercise-library-push/\">the push exercise library</a>.</p>",

"fitness/protein-foods-nigeria":
    "<h2>Local sources, with the numbers that matter</h2>"
    "<p>Protein targets are usually discussed in terms of imported foods, which makes them look expensive. Nigerian staples include substantial protein sources at low cost, and the practical question is how much each contributes per portion rather than whether it counts. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the dietary guidance on protein intake. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>Getting more from what is already available</h2>"
    "<ul>"
    "<li><b>Legumes are the cheapest source.</b> Beans, lentils and egusi contribute meaningful protein per portion at low cost.</li>"
    "<li><b>Fish, fresh or dried.</b> Dried fish is concentrated and keeps, which makes it practical where refrigeration is limited.</li>"
    "<li><b>Eggs remain the most versatile.</b> Inexpensive, complete, and usable in almost any meal.</li>"
    "<li><b>Combine across the day.</b> Total daily intake matters more than any single meal's composition.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/how-much-protein-do-you-need/\">how much protein you need</a>, <a href=\"/fitness/plant-based-protein-explained/\">plant-based protein</a> and <a href=\"/fitness/protein-powder-worth-it/\">whether protein powder is worth it</a>.</p>",

"fitness/what-water-does-to-your-body":
    "<h2>Hydration matters, and the extremes are overestimated</h2>"
    "<p>Water is involved in temperature regulation, joint lubrication and every metabolic process, so the deficiency effects are real. The exaggeration is usually in the volume: for most people in moderate conditions, thirst is an adequate guide, and the fixed eight-glasses figure has no physiological basis. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes guidance on water and health. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What the evidence supports</h2>"
    "<ul>"
    "<li><b>Dehydration impairs performance measurably.</b> The effect appears well before serious dehydration.</li>"
    "<li><b>Thirst is a usable signal.</b> Except during prolonged exercise in heat, where it lags behind need.</li>"
    "<li><b>Needs vary widely.</b> Climate, body size, activity and diet all shift the requirement.</li>"
    "<li><b>Over-drinking carries its own risk.</b> Excessive intake during endurance events can dilute blood sodium, which is a genuine danger.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/how-much-water-to-drink-a-day/\">how much water to drink a day</a>, <a href=\"/fitness/water-during-workout/\">water during a workout</a> and <a href=\"/fitness/electrolytes-do-you-need-them/\">whether you need electrolytes</a>.</p>",

"fitness/what-fruit-does-to-your-body":
    "<h2>Fruit is not a sugar problem</h2>"
    "<p>The argument that fruit should be limited because it contains sugar confuses the sugar in whole fruit with added sugar. Whole fruit carries fibre, water and micronutrients in a form that slows absorption and produces satiety, and the evidence does not support restricting it in the way the claim implies. <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the reference material on fruit and dietary fibre. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What the evidence actually shows</h2>"
    "<ul>"
    "<li><b>Fibre changes how the sugar behaves.</b> Whole fruit is not metabolically equivalent to a sugared drink with the same sugar content.</li>"
    "<li><b>Juice is the different case.</b> Removing the fibre removes most of the satiety and much of the benefit.</li>"
    "<li><b>Quantity within normal eating is not a concern.</b> The problems attributed to fruit sugar come from added sugar elsewhere in the diet.</li>"
    "<li><b>Variety matters more than volume.</b> Different fruits supply different compounds.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/superfoods-marketing-vs-evidence/\">superfoods: marketing versus evidence</a>, <a href=\"/fitness/is-fresh-always-better-than-frozen-explained/\">fresh versus frozen</a> and <a href=\"/fitness/is-breakfast-really-important-explained/\">whether breakfast matters</a>.</p>",

"fitness/intermittent-fasting-explained":
    "<h2>A timing pattern, not a metabolic shortcut</h2>"
    "<p>Intermittent fasting restricts when food is eaten rather than what or how much. That distinction is the whole thing: where it produces weight loss, the mechanism is usually reduced total intake because the eating window is smaller, not a change in how the body processes food. <a href=\"" + NIDDK + "\" rel=\"noopener\">The National Institute of Diabetes and Digestive and Kidney Diseases</a> publishes the research summary on fasting approaches. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What to weigh before trying it</h2>"
    "<ul>"
    "<li><b>It works when it reduces intake.</b> If the window is filled to the same total, the result is the same as any other schedule.</li>"
    "<li><b>It suits some schedules and not others.</b> People who train in the morning or work physical shifts often find it unworkable.</li>"
    "<li><b>Protein intake becomes harder.</b> Fewer meals means each one has to carry more, which matters during training.</li>"
    "<li><b>It is not appropriate for everyone.</b> Anyone with a history of disordered eating, or who is pregnant or managing certain conditions, should not adopt it without medical advice.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/intermittent-fasting-honest-guide/\">the honest guide</a>, <a href=\"/fitness/fasted-cardio-explained/\">fasted cardio</a> and <a href=\"/fitness/eating-late-at-night-myth-explained/\">eating late at night</a>.</p>",

"fitness/posture-exercises-what-evidence-says":
    "<h2>The evidence is weaker than the confidence</h2>"
    "<p>Posture correction is marketed with certainty that the research does not support. Postural alignment varies widely among people without pain, and the relationship between a measured posture and symptoms is much weaker than commonly claimed &mdash; which does not make the exercises useless, but it does change what they are for. <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the reference material on posture and back health. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What the exercises do achieve</h2>"
    "<ul>"
    "<li><b>Strength and endurance.</b> The muscles that hold a position get stronger, which is a real and measurable change.</li>"
    "<li><b>Comfort from movement.</b> Changing position regularly helps more than achieving a specific alignment.</li>"
    "<li><b>Range of motion.</b> Where stiffness limits movement, mobility work addresses it directly.</li>"
    "<li><b>Not a structural correction.</b> Skeletal alignment in adults is not reshaped by exercise, and claims that it is should be treated with suspicion.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/back-pain-and-exercise-what-evidence-says/\">back pain and exercise</a>, <a href=\"/fitness/desk-stretches-office-workers/\">desk stretches</a> and <a href=\"/fitness/mobility-vs-flexibility/\">mobility versus flexibility</a>.</p>",

"fitness/muscle-loss-after-40-explained":
    "<h2>The decline is real, and it is modifiable</h2>"
    "<p>Adults lose muscle mass progressively from around the fourth decade, and the rate accelerates later. What the research consistently shows is that the majority of what is attributed to ageing is attributable to reduced activity, which means resistance training changes the trajectory substantially. <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the reference material on age-related muscle loss. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What changes the trajectory</h2>"
    "<ul>"
    "<li><b>Resistance training, twice weekly at minimum.</b> The single most effective intervention, at any starting age.</li>"
    "<li><b>Higher protein than younger adults need.</b> The response to a given amount is blunted with age, so the requirement rises.</li>"
    "<li><b>Progressive load.</b> Maintenance work preserves less than progressive work builds, and the difference grows with age.</li>"
    "<li><b>Consistency across years.</b> Short programmes help, but the benefit compounds over decades rather than weeks, which is the argument for a routine you can hold indefinitely.</li>"
    "</ul>"
    "<p>It is also worth separating the two things people mean by muscle loss: the tissue itself, and the strength that goes with it. Both respond to training, and strength usually improves faster than size, which means capability returns before it looks different. See <a href=\"/fitness/strength-training-over-50/\">strength training over 50</a>, <a href=\"/fitness/mobility-after-40-explained/\">mobility after 40</a> and <a href=\"/fitness/recovery-changes-with-age-explained/\">how recovery changes with age</a>.</p>",

"fitness/apple-cider-vinegar-effects":
    "<h2>A small effect, heavily oversold</h2>"
    "<p>The claims attached to apple cider vinegar far exceed what the research supports. There is modest evidence for a small effect on post-meal blood glucose in some studies, and essentially none for the weight-loss, detoxification and disease claims made in marketing. <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the reference material on vinegar and health claims. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What is and is not supported</h2>"
    "<ul>"
    "<li><b>A modest glucose effect.</b> Small, inconsistent across studies, and not a substitute for any prescribed treatment.</li>"
    "<li><b>No meaningful weight loss.</b> The trials that showed any effect showed very little, and appetite suppression from acidity is not a sustainable mechanism.</li>"
    "<li><b>Real risks at undiluted strength.</b> Acidity damages tooth enamel and can irritate the oesophagus.</li>"
    "<li><b>Interactions worth checking.</b> Anyone on medication for diabetes or potassium should discuss it with a clinician.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/detox-diets-what-evidence-says/\">detox diets and the evidence</a>, <a href=\"/fitness/superfoods-marketing-vs-evidence/\">superfoods: marketing versus evidence</a> and <a href=\"/fitness/supplements-waste-of-money/\">which supplements are a waste of money</a>.</p>",

"fitness/creatine-explained":
    "<h2>The best-evidenced supplement in the category</h2>"
    "<p>Creatine monohydrate is unusual among supplements in having a large, consistent evidence base for improving performance in high-intensity effort and supporting gains during resistance training. It is also inexpensive, which removes the commercial incentive that distorts most supplement claims. <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the reference material on creatine. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What the evidence supports</h2>"
    "<ul>"
    "<li><b>Improved repeated high-intensity effort.</b> The effect is clearest in short, maximal efforts with recovery between.</li>"
    "<li><b>Greater gains alongside training.</b> It supports the work rather than replacing it, and does nothing without training.</li>"
    "<li><b>Initial weight gain is water.</b> Intracellular water retention accounts for the early change on the scale.</li>"
    "<li><b>Monohydrate is the form with the evidence.</b> The newer forms cost more and have not demonstrated an advantage.</li>"
    "</ul>"
    "<p>Anyone with kidney disease or taking medication affecting the kidneys should consult a clinician first. See <a href=\"/fitness/supplements-waste-of-money/\">which supplements are a waste of money</a>, <a href=\"/fitness/protein-powder-worth-it/\">whether protein powder is worth it</a> and <a href=\"/fitness/pre-workout-supplements-explained/\">pre-workout supplements</a>.</p>",

"fitness/time-under-tension-explained":
    "<h2>A description, not a target</h2>"
    "<p>Time under tension describes how long a muscle is loaded during a set. It is a useful way of thinking about why a slow set feels harder than a fast one, but treating it as a target to maximise leads to training decisions that the evidence does not support &mdash; very slow repetitions performed for their duration are not more effective than ordinary ones. <a href=\"" + ACSM + "\" rel=\"noopener\">The American College of Sports Medicine</a> publishes the guidance on repetition duration. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>The sensible reading</h2>"
    "<ul>"
    "<li><b>Tension matters, duration is a proxy.</b> What produces adaptation is mechanical tension, and time is only one route to it.</li>"
    "<li><b>Sets taken near failure matter more than their length.</b> Proximity to failure predicts the stimulus better than duration does.</li>"
    "<li><b>Moderate speed works.</b> Deliberately slow repetitions reduce the load that can be used, which can be counterproductive.</li>"
    "<li><b>Use it to vary stimulus.</b> Changing tempo is a legitimate way to progress when load cannot increase.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/tempo-training-explained/\">tempo training</a>, <a href=\"/fitness/how-many-reps-for-muscle/\">how many reps for muscle</a> and <a href=\"/fitness/progressive-overload-without-adding-weight-explained/\">overload without adding weight</a>.</p>",

"fitness/downside-of-stimulants":
    "<h2>What the stimulant is actually doing</h2>"
    "<p>Stimulants reduce perceived effort, which is why they feel effective &mdash; and the same mechanism is why they carry risk, because reduced perception of effort means the body's warning signals are also dulled. The performance effect is real; so are the costs, which are frequently underestimated at the doses used in pre-workout products. <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the reference material on caffeine and stimulant effects. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>The costs that accumulate</h2>"
    "<ul>"
    "<li><b>Tolerance.</b> The effect diminishes with regular use, which pushes doses up rather than results up.</li>"
    "<li><b>Sleep disruption.</b> Taken late, stimulants impair the recovery that training depends on, which can cancel the benefit.</li>"
    "<li><b>Cardiovascular load.</b> Raised heart rate and blood pressure during effort, which matters more in people with underlying conditions.</li>"
    "<li><b>Dependence and withdrawal.</b> Headaches and fatigue on stopping are common and are often misread as a need to continue.</li>"
    "</ul>"
    "<p>Anyone with a cardiovascular condition, or who is pregnant, should avoid stimulant pre-workouts. See <a href=\"/fitness/pre-workout-supplements-explained/\">pre-workout supplements</a>, <a href=\"/fitness/caffeine-side-effects/\">caffeine side effects</a> and <a href=\"/fitness/heart-pounding-during-workout/\">heart pounding during a workout</a>.</p>",

"fitness/exercise-when-sick-explained":
    "<h2>Symptom location is a rough but useful guide</h2>"
    "<p>The common clinical rule of thumb distinguishes symptoms above the neck from those below it: a runny nose usually permits light activity, while fever, chest symptoms or body aches do not. It is a heuristic rather than a diagnosis, and the conservative reading is the safer one. <a href=\"" + MEDLINE + "\" rel=\"noopener\">MedlinePlus</a> carries the reference material on exercise during illness. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>The decisions that matter</h2>"
    "<ul>"
    "<li><b>Fever means stop.</b> Exercising with a fever raises the risk of complications and delays recovery.</li>"
    "<li><b>Reduce intensity rather than maintain it.</b> A walk is a different proposition from a hard session when unwell.</li>"
    "<li><b>Return gradually.</b> Performance drops quickly during illness and recovers more slowly than people expect.</li>"
    "<li><b>Do not use exercise to sweat it out.</b> There is no mechanism by which that helps, and it costs recovery.</li>"
    "</ul>"
    "<p>This page is general information, not medical advice; persistent or worsening symptoms need clinical assessment. See <a href=\"/fitness/restarting-exercise-after-a-break/\">restarting after a break</a>, <a href=\"/fitness/recovery-changes-with-age-explained/\">how recovery changes with age</a> and <a href=\"/fitness/rest-days-and-recovery/\">rest days and recovery</a>.</p>",

"fitness/exercise-and-longevity-explained":
    "<h2>The most consistent finding in the field</h2>"
    "<p>Regular physical activity is among the strongest modifiable predictors of how long and how well people live, and the association holds across populations and study designs. The effect is not confined to intense exercise: the difference between doing nothing and doing something is larger than the difference between doing something and doing a lot. The <a href=\"" + WHO + "\" rel=\"noopener\">World Health Organization</a> publishes the physical-activity guidelines this page is based on. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What the evidence points to</h2>"
    "<ul>"
    "<li><b>Both types matter.</b> Aerobic activity and muscle-strengthening contribute differently, and the guidelines recommend both.</li>"
    "<li><b>Cardiorespiratory fitness is a strong marker.</b> It predicts outcomes independently of activity level, which is why it is worth training directly.</li>"
    "<li><b>Strength and grip correlate with later independence.</b> The practical outcome is less about lifespan than about capability in later years.</li>"
    "<li><b>Starting late still helps.</b> The benefit is not reserved for the lifelong exerciser.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/vo2-max-explained/\">VO2 max explained</a>, <a href=\"/fitness/grip-strength-why-it-matters/\">why grip strength matters</a> and <a href=\"/fitness/exercise-for-bone-density-explained/\">exercise for bone density</a>.</p>",

"fitness/couch-to-5k-explained":
    "<h2>Why the walk-run structure works</h2>"
    "<p>Couch to 5K alternates walking and running in a ratio that shifts across the programme, which allows total running volume to increase faster than continuous running would permit. The structure is the reason it succeeds with beginners: each session is achievable, and the progression is defined rather than improvised. <a href=\"" + NHS + "\" rel=\"noopener\">The NHS</a> publishes the Couch to 5K programme this page describes. By the Bryme Fitness desk. Reviewed 27 September 2026.</p>"
    "<h2>What makes it succeed or fail</h2>"
    "<ul>"
    "<li><b>Run the runs slowly.</b> The commonest error is running the intervals too fast, which makes the following week unmanageable.</li>"
    "<li><b>Keep the rest days.</b> The adaptations occur during recovery, and removing rest days is how injuries start in week three.</li>"
    "<li><b>Repeat a week if needed.</b> The schedule is a guide; finishing the programme matters more than finishing it on time.</li>"
    "<li><b>Expect the transition to continuous running to be the hard part.</b> Weeks five and six are where most people drop out.</li>"
    "</ul>"
    "<p>See <a href=\"/fitness/beginner-running-plan/\">the beginner running plan</a>, <a href=\"/fitness/how-to-choose-running-shoes/\">how to choose running shoes</a> and <a href=\"/fitness/running-form-explained/\">running form explained</a>.</p>",

}
