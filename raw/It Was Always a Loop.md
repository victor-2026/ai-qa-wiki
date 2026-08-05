

[https://medium.com/@kdineshkvkl/it-was-always-a-loop-1a216f3eeb3c

](https://medium.com/@kdineshkvkl?source=post_page---byline--1a216f3eeb3c---------------------------------------)

[Dinesh Karakambaka](https://medium.com/@kdineshkvkl?source=post_page---byline--1a216f3eeb3c---------------------------------------)

Follow

7 min read

·

Jul 11, 2026

5

[

](https://medium.com/plans?dimension=post_audio_button&postId=1a216f3eeb3c&source=upgrade_membership---post_audio_button-----------------------------------------)

## “Loop engineering” is the phrase of the year. The idea underneath is older than most of the people naming it — and seeing that clearly is worth more than the hype around it.

Our field has a rhythm. A practice that working engineers have quietly relied on for years gets a clean name, the name arrives attached to someone with a large audience, and within a month the thing is discussed as though it were discovered rather than merely described. “Loop engineering” is the latest turn of that wheel, and the honest version of it is more useful than the exciting one.

An agent does not have a loop added to it the way you bolt a turbo onto an engine. Being a loop is what makes it an agent. Read the situation, act, check what changed, correct, and go again toward a goal you were given once — that is not a technique someone dreamed up in 2026. It is the shape of nearly every self-correcting system we have trusted for decades, from the thermostat holding a room at temperature to the pipeline that refuses to merge a broken build.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*OpRBy0zpoHLcnczn91VNMA.png)

## The mechanism, and why it’s old

Three parts carry the whole weight of a loop, and the fastest way to see they aren’t new is to notice a household thermostat has all three. There’s a **verifier** — a check that can genuinely fail the work; in the thermostat it’s the thermometer, in software it’s the test that passes or fails, the metric that moves the right way or the wrong way. Without it, repetition stops being progress and becomes the model nodding along with its own last answer forever. There’s **state** — memory of what’s already been tried, so the loop learns instead of repeating its fourth-pass mistake from the first pass. And there’s a **stop condition** — the goal is met, or a hard limit says stop after N attempts and report — without which a loop runs until it wins, breaks, or quietly empties your account overnight.

State those three together and the point makes itself. Control theorists have built loops with exactly this structure since long before language models existed. What is genuinely different now is only the substrate: for the first time, the thing inside the loop proposing the next move and judging the last one can be a model reasoning in open-ended code and prose, rather than a fixed rule tuning a fixed dial. That is a real change. It is worth being precise that it is the _only_ change.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*GRc5BQWaAPca09mCryMdqw.png)

## The naming problem is ours, not theirs

Here is the part the excitement skips. The last few years handed us a procession of terms — prompt engineering, then context engineering, then harnesses, then skills, and now loop engineering — each arriving as though a frontier had just been crossed. Each names something real. But prompt engineering was, at bottom, learning to ask for what you want with precision. Context engineering was deciding what to put in front of the system before asking it to reason. A “skill” written down as reusable conventions and steps is something a great many engineers were maintaining, under their own private names, long before the word travelled.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*bNJtyFGM57fN6HHuBgxHPA.png)

This is not a complaint about the people who coined the terms; naming is a genuine service, because a good name lets a scattered practice be taught and shared. The problem is us, the audience, when we mistake the moment a thing is _named_for the moment it was _invented_, and let an idea’s reach be set by the size of the platform it launched from rather than its merit. Plenty of practitioners were running loop-shaped automations and maintaining skill-shaped documents years ago and simply got on with the work. The concepts didn’t become true when a famous person described them — they became popular. Those are not the same event, and confusing them is how you end up chasing vocabulary instead of understanding mechanisms. Understand the mechanism and the next rename can’t sell you anything; learn only the word and you’re at the mercy of whoever coins the next one.

A loop only earns its cost, by the way, under four conditions together: the task recurs, verification can be automated, your budget can absorb the wasted tokens, and the agent has real tools to run and check its own work. Miss one and a single good prompt beats a loop.

[](https://medium.com/plans?source=promotion_paragraph---post_body_banner_dot_calm_clouds--1a216f3eeb3c---------------------------------------)

When all four hold, the cleanest specimen to study is the one Andrej Karpathy published in March 2026 — valuable not because it invented anything, but because it’s small and legible enough to read in an afternoon. His AutoResearch is about six hundred lines across three files: `train.py`, the model, the only file the agent may edit; `prepare.py`, the scorer, which the agent is forbidden to touch (an agent allowed to edit its own exam makes the exam easier, not the model better); and `program.md`, a plain-English file where the human writes what to explore. The loop reads the code, proposes a change, trains for five minutes, keeps it if the score improved and rolls it back if it didn't, and repeats without asking permission. Pointed at a model Karpathy had already hand-tuned for years and left running two days, it ran roughly seven hundred experiments and surfaced about twenty improvements he'd missed — including a missing scaler in the attention mechanism a careful person could have found and simply didn't, because attention flags around experiment twelve and the machine's doesn't. The remarkable thing isn't that a loop can improve a model; that's close to expected. It's that the whole apparatus fits in six hundred readable lines, which makes it a teaching artifact more than a breakthrough.

## The one genuinely new turn

If most of what gets announced is old ideas in new clothes, it’s fair to point at where something does move forward. Qu and Lu’s March 2026 paper, “Bilevel Autoresearch,” is disarmingly literal: if the loop is a way of doing research, point a loop at the loop. The inner loop does the familiar work — propose, train, evaluate, keep or discard. The outer loop watches it, reads its traces, finds where the _search itself_ keeps getting stuck, and writes new code that changes how the inner loop searches. On Karpathy’s own benchmark the two-loop version beat the single loop fivefold, and the telling detail is that both loops used the same model — the gain came from the arrangement, not a bigger brain. It works because a model keeps reaching for the same optimisations even after they stop paying off, wearing familiar grooves into the search; the outer loop’s whole job is to break those grooves. Even this, though, is meta-learning in the loop’s vocabulary rather than a brand-new field — and its authors are careful to call recursive self-improvement a direction, not a proven result, which is exactly the restraint the surrounding hype lacks.

## Feel it work in one paragraph

You don’t need special tooling to understand this from the inside. Paste this into any chat model and watch the mechanism run in miniature:

Work in a loop until the result clears the bar.

TASK: [describe exactly what you want produced]SUCCESS CRITERIA (strict — these are your gate):  
- [criterion 1]  
- [criterion 2]  
- [criterion 3]Each turn, out loud:  
1. PLAN   — the single next thing you'll fix.  
2. DO     — produce or improve the work.  
3. VERIFY — score 1-10 on every criterion; say what's still weak.  
4. DECIDE — all criteria 8+? print DONE and stop.  
            Otherwise print ITERATING and go again, weakest score first.Rules: never done below 8 on any criterion; each pass targets the last  
turn's weakest score; don't ask me questions — assume and keep moving.Begin.

The criteria are the verifier, the running score is the state, the “8 or higher” rule is the stop condition. It’s the toy version — you’re still the trigger and it evaporates when you close the tab — but the jump to something autonomous is only adding a heartbeat, a memory file, and a gate that can’t be argued with.

## What the loop doesn’t fix

It doesn’t remove you from the work; it changes the shape of your involvement, and two of its costs grow sharper as the loop gets better. The first is comprehension debt: the faster it ships code you didn’t write, the wider the gap between what’s in your repo and what you understand — and the morning you debug a system nobody has read, that bill dwarfs every token you spent. The second is quieter. When the loop hums, it’s tempting to stop forming an opinion and accept whatever comes back; the same act, designing the loop, is the cure when done with judgment and the accelerant when done to avoid thinking. Two people can build the identical loop and end up in opposite places. The system can’t tell them apart. You can.

Which is where we started. The people getting real value here aren’t the ones who learned the word “loop” the week it trended. They’re the ones who understood the mechanism early enough that the word, when it arrived, told them nothing new. Don’t chase the names. Understand the mechanism, and let the names arrive whenever they like.

- Dinesh Karakambaka