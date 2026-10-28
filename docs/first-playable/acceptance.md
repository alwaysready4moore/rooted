# Acceptance plan

Status: these are engine and human checks to execute, not claims of passed gameplay.
Fixture: prototype/first-playable/prepared-save.json. Settings: default speed, dry weather, no stamina. Build owner records Godot version, commit, fixture, settings and actual result for each ID.

| ID | Action | Required result |
|---|---|---|
| FP-QA-01 | Load prepared fixture | Spring 8 Year 1, 06:00, 20 coins, six plots, three NPCs; no real story secrets |
| FP-QA-02 | Open inventory, then dialogue/settings via supported flow; close one | Clock stays paused until all owners release pause |
| FP-QA-03 | Read dialogue for two real minutes | No game-time advance or late arrival caused by reading |
| FP-QA-04 | Advance 60 active seconds | 60 game minutes at default speed, within one displayed tick |
| FP-QA-05 | Sleep on Spring 30, then Winter 30 using debug snapshots | Summer 1 same year; Spring 1 next year; one overnight update |
| FP-QA-06 | Water same plot twice; refill | First valid watering uses one charge; second uses none; refill caps at 6 |
| FP-QA-07 | Sleep watered and dry crops, reload | Only watered growth increments once; dry crop survives; reload does not grow again |
| FP-QA-08 | Try harvest with full inventory | No plant or item loss; make space then harvest exactly once |
| FP-QA-09 | Plant with missing seed; buy with insufficient money | No partial mutation; actionable message |
| FP-QA-10 | Observe morning through afternoon | All three residents visibly travel; active conversation holds actor until finished |
| FP-QA-11 | Place job props in wrong/correct order | Wrong placement retries freely; three correct spots complete once, +6 coins |
| FP-QA-12 | Cancel job before and after first placement | Before free; after commits 30 min/no wage and resets props; reoffer next day |
| FP-QA-13 | Confirm mint contribution twice with same transaction ID | Exactly one mint removed, exactly 3 servings added; menu visibly changes |
| FP-QA-14 | Start/complete shift at noon | World paused during assembly; finishes 14:00; +12 coins once; 3 orders |
| FP-QA-15 | Shift with no mint | All house drinks; valid paid completion and service evidence |
| FP-QA-16 | Incorrect herb assembly and assist | No stock loss; assist does not reduce wage |
| FP-QA-17 | Start shift after 18:00 | Clear closing-time explanation; next-day opportunity |
| FP-QA-18 | Abandon shift before/after first served order | Before free/restores all reservations; after full time/no wage, restores only unserved reservations |
| FP-QA-19 | Save midshift, reload, finish twice | Same orders/reservations; no double ingredient, wage or time effects |
| FP-QA-20 | Complete job and chat in either order | Helper visit eligibility identical; offered in 16:00–19:00 window |
| FP-QA-21 | Decline/postpone favor | Gate stays usable; friendship intact; postponed visit returns |
| FP-QA-22 | Accept favor by 18:45 | 15 min once; gate stays repaired after reload |
| FP-QA-23 | Gain two distinct contribution categories | Neighbor state and optional guest invitation; repeating same category adds no breadth |
| FP-QA-24 | Befriend two synthetic NPCs | Their pair relation remains unchanged |
| FP-QA-25 | Save after transactions and at sleep; corrupt newest save | Exact state restored or previous-good recovery; original retained |
| FP-QA-26 | Load future save/content version | Clear incompatibility, no overwrite or item deletion |
| FP-QA-27 | Reach 22:00 or sleep early | Neutral day end, no penalty; day advances once to 06:00 |
| FP-QA-28 | Keyboard/controller-only full route | All actions possible, focus visible, no rapid input requirement |
| FP-QA-29 | Text 150%, 1280x720, reduced motion | Readable/wrapped UI; no color-only information; reduced animation |
| FP-QA-30 | Pass tree/counter/bridge and doorway | Feet-based depth correct, layer changes explicit, collision intact, state preserved |
| FP-QA-31 | Leave host before supply or skip job | Town remains usable; opportunities remain discoverable later |
| FP-QA-32 | Reset test fixture | Explicit confirmation, affects test slots only |

## Route and reachability

Happy path target, not mandatory schedule: 06:00 care/harvest; 09:00 helper job; 10:00 venue contribution; 12:00 shift; 14:00 free time/conversations; 16:00 favor; return home and sleep.
A conversation can happen before/after job. Supply and shift can happen independently; zero mint never blocks service. Favor postponed past 18:45 retries later. Guest invitation repeats during eligible venue windows.
Acceptance must cover: zero money, full inventory, missing mint, no job, delayed favor, reload before/after each reward, participant route conflict, day-end while menu paused.

## Human observation

Start with 3 adult volunteer playtesters unfamiliar with the fixture, when a runtime exists. Do not invent sessions.
Prompt: spend a day here; choose what interests you. Explain controls, not the preferred route.
Observe time spent on chores, conversations visited, why the player left/stayed, whether menu change and reciprocal help were understood, and whether they felt rushed.
Provisional success: all can perform essential controls without intervention; at least 2 of 3 explain a contribution's visible consequence and want to see another day; normal six-plot routine under 2 active minutes; no forced optimization felt necessary. Tiny sample is directional only.
If failed: fix the specific friction or pacing before adding crops, NPCs or festivals. Do not treat a numerical pass as proof of fun.

## Evidence record

Per test record ID, build commit, engine version, fixture/settings, steps, observed vs expected, pass/fail/blocked and capture path. Documentation/data validation is not engine or human validation.
