# First playable framework v0.1

Prepared October 27, 2026. **Review package, not a runnable game.**
The creator authorized implementation-oriented defaults for inspection and refinement. New defaults below are ASSUMED FOR PROTOTYPE, not narrative canon or final balance.

## 1. What the player should experience

A prepared day after introductions: care for a small plant plot, see three residents following routines, work alongside one resident, supply an ingredient to the venue, serve a short shift, and receive a personal offer of help. The player can decline individual activities; a completion checklist is only a QA tool.

Question: does participating in town life feel worth leaving the farm for?
Hypothesis: a useful ingredient, a concrete collaboration and a subsequent favor make the community loop understandable without a large crop catalog.
Target: 20–30 real minutes including paused reading, not a timer or promise. Sixteen active hours equal 16 real minutes at the test speed.

## 2. Decision status

APPROVED: Bluebird Bay; fully illustrated layered 2D; crop-only farming; 30-day seasons/120-day year/no months; optional romance/family; resident-to-resident relationships distinct from player relationships; dialogue and important choices pause time; exploration/farming advance time.
APPROVED FOR PROTOTYPE: 1 real second = 1 game minute; inventory/map/journal/settings pause; fixed-duration activities charge once; prepared slice after introductions; important personal events can retry.
ASSUMED FOR THIS PACKAGE: six plots; mint and turnip as test crop names; no stamina in this experiment; times, prices, quantities, simple standing rules, save format, map geometry and attendance below. All are easy to replace.
OPEN FOR FULL GAME: final bedtime/fatigue, crop catalog/balance, festivals and aging, romance/family mechanics, complete town, production art resolution, exact Godot release. None blocks this test.
Source conflict rule: newest explicit creator decision wins; this package replaces earlier unspecified prototype parameters only for this experiment.

## 3. Play space and prepared fixture

Three small connected scenes: farmhouse, farm/path exterior, venue interior. Exterior includes six plots, refill point, helper work area, sorting tree and bridge. The bridge tests explicit 2D elevation transitions, not a 3D environment. Two test indoor/outdoor transitions exercise persistence. Map layout is provisional.
Use anonymous public NPC IDs resident_helper, resident_host, resident_guest. Their synthetic schedules and debug lines do not establish cast lore. Private cast assignments live only in Drive.
Fixture starts Spring 8 Year 1 at 06:00, farmhouse; money 20; seeds and watering can; one mature mint plant. Prior introductions and a prior helper visit are seeded explicitly. This does not imply friendship arose in one day.
No live weather: dry day. No festival is needed. Four-direction motion and walking sprites may be temporary labeled 2D shapes; final art must follow the art bible.
Prepared NPCs: helper travels between work area/venue/farm; host visits exterior before venue work; guest walks from path to venue and back. All three must visibly travel at least once. Off-map home anchors are test exits, not canonical homes.

## 4. Time and calendar

Clock holds absolute_day (0 = Spring 1 Year 1), minute_of_day and subminute accumulator.
year=floor(absolute_day/120)+1; season=floor((absolute_day%120)/30); day=absolute_day%30+1.
Use continuous seven-day cycle, weekday=absolute_day%7, Monday at day 0, only as a prototype default. Never reset weekday on season rollover.
Wake 06:00; stop active exploration at 22:00. At cutoff, show a neutral end-day panel and offer sleep or load. No collapse, lost money or medical scene. Sleep can be chosen earlier at the bed. Sleep advances exactly one date, resets clock to 06:00 and triggers overnight processing once.
Menus/dialogue pause by scoped tokens. Closing one nested panel cannot release another panel's token. Losing app focus pauses. Pause tokens and interpolation are reconstructed, not serialized.
Ordinary tool animations consume elapsed clock time only. Paused dialogue has no hidden fee. Do not accumulate wall-clock debt during pauses.
Activity time reservation: before acceptance show duration and wage. Capture start time; require start+duration <= closing minute and participant availability. Freeze world clock during the minigame. On completion or leaving after the first committed action, advance to start+duration once. Canceling before that action refunds time. In-progress state records end time; save/load must not charge twice.
After a fixed jump, update crossed schedule milestones in order. Busy participants remain assigned until activity ends, then take the currently valid destination. No catch-up crop growth during time jumps.
Example: accept a 120-minute shift at 12:00; finish at 14:00 regardless of reading speed. Reject starts after 18:00 for a venue closing at 20:00. Show why and next opportunity.

## 5. Farm and inventory

Six plots: mint ready; two immature turnips; one newly planted mint; one empty tilled plot; one untilled plot. Hoe changes untilled -> tilled once; planting consumes one seed atomically; watering changes a planted crop to watered and consumes one can charge once per day; harvesting consumes a mature single-harvest plant and yields one item, leaving tilled soil.
Test growth: mint 2 watered nights; turnip 3. At sleep increment growth once for watered immature plants, cap at maturity, clear water flags and refill no tools automatically. Dry crops pause growth, do not die. Prototype plants survive season change; this is deliberately not a full crop-season model.
Watering can capacity 6; refill is free at the nearby point. Tools are permanent equipment separate from inventory. No stamina, tool upgrades, livestock, shipping or processing machines.
Inventory: 12 slots, stack cap 99. Deposit fills existing stacks then empty slots. Before any exchange, simulate the entire delta; if capacity/resources fail, change nothing. Never delete an overflowing harvest or consume a seed for a blocked plot.
Inventory has mint, turnip, mint_seed and turnip_seed. Contextual seed purchase at venue supply shelf is a synthetic test interface: 2 coins/mint seed, 3/turnip seed, unlimited stock in this experiment. Do not canonize a seed merchant. No crop selling or gifting economy in slice.
Money >=0 integer. Job pays 6 once; shift pays 12 once on all three orders completed, no tip/quality multiplier. Ingredient supply is explicitly a voluntary contribution in this experiment; full-game trade/payment is open.

## 6. Active odd job and reciprocity

Job: help the helper arrange three lightweight test props at marked work positions. This is a synthetic mechanics task, not unreleased character dialogue.
Player walks, picks up and places each prop, with distinct progress and free retry for wrong placement. No button mashing or reflex timer. Accept at work area 09:00–11:30; reserve 30 minutes, finish by noon. Show duration/pay first.
Commit first valid placement locks the time reservation. Cancel before then is free; after then, show time cost and no wage; restore test props and reoffer next day. Completion pays 6 and records unique evidence once. Replaying a completed one-time job does nothing.
Prepared helper relationship starts familiar. Complete the job and have one optional conversation (either order) -> companion visit becomes eligible; record eligibility, do not deduct friendship for refusal.
Helper's farm visit window 16:00–19:00. He follows the visit route on an eligible day. Offer repair of a synthetic sticking gate; accepting reserves 15 minutes and sets gate_repaired permanently. Latest start 18:45. Postpone queues the next eligible day. Declining the task does not prevent ordinary conversations.
A leisure invitation is independently available after conversation; repair acceptance is not required. Only one optional farm visitor can hold the visit slot. Cooldown one day; no surprise forced dialogue.
The gate remains passable before repair; repaired version removes an extra interaction animation. No essential traversal is friendship-gated.

## 7. Venue contribution and service

Host open 10:00–20:00. Transfer exactly one mint only after explicit confirmation. Validate inventory removal, menu addition and supply ledger as one transaction. One mint creates 3 herb-drink servings in venue stock; menu label shows remaining quantity. Duplicate confirmation/transaction IDs do not duplicate stock.
House drink is always available from existing venue supplies. No mint means the venue still functions. Each shift has three orders: first herb drink if one can be reserved, otherwise house drink; last two house drinks.
At start reserve the required herb serving from stock into the activity. On correct service consume reservation. Incorrect assembly neither spends stock nor advances order. On abandonment restore any unserved reserved stock; served drinks remain consumed. Reserved stock is persisted across reloads.
Preparation is click/confirm assembly with text and icon cues: house base -> cup -> serve; herb drink adds herb before serve. No timing score; retry and assist mode exist. Customer text is neutral debug placeholder text pending approved script.
At most one completed paid shift per day. Shift starts 10:00–18:00, lasts 120 minutes. Partial shift pays no wage and consumes reserved time after first served order; player sees terms beforehand. Uncommitted cancellation is free. Do not lock the whole day's shift on a no-action cancellation.
A completed shift adds service evidence once. Customer arrivals and menu state visibly react without spawning permanent new residents.

## 8. Relationships and Community Standing

For the slice, use evidence flags instead of unbalanced point farming. Individual state: met bool, contact_days unique integers, evidence unique IDs, romance separate enum (none in fixture). Shared NPC-pair state has its own map; public fixture is empty.
One chat per NPC/day records contact, repeated chat gives no extra progression. No friendship decay in prototype.
Standing derives distinct contribution categories: job, supply, service. Fixture starts newcomer with zero categories; two distinct categories -> neighbor for this test only. No money score or romance contribution. Permanent story evidence is keyed to event IDs to avoid replay gains.
On first neighbor transition, guest offers a reusable optional venue-seat invitation. Show behavior and a modest journal update rather than only a numeric badge. The temporary threshold/stage subset does not redefine the full six-stage system.
Helper favor depends on the helper relationship evidence, not global standing. Never automatically change an NPC-pair relationship because Rowan befriends either person.

## 9. Narrative and event arbitration

Definitions are data; event runtime evaluates prerequisites and revalidates at commitment. Deterministic priority: day-end/system recovery > active activity > accepted scheduled invitation > authored one-time event > ambient encounter. Tie: earliest eligibility then lexical event ID.
At most one dialogue/activity owns player input. Actor activity leases prevent simultaneous bookings. Interacting pins that NPC through the exchange, then resumes current schedule.
State transitions: unavailable -> available -> offered -> active -> completed. Decline/postpone returns to available with next eligible day; cancellation behavior follows transaction rules. Completed one-time IDs persist.
Opening story is separate from prepared fixture. Do not expose final creative dialogue via public debug text. Festival dates do not force personal-event completion. Future content must provide recognition variants for already-met residents.

## 10. Saving and recovery

Save version 1 JSON with fixture_id and content_version. Persist date/minute/remainder, scene/position, plot/can/inventory/money, NPC anchor/destination, flags, contact/evidence, pair relations, visit reservations, standing categories, venue stock, completed IDs, daily records and active activity including reservation/end time.
Write temp -> validate -> preserve previous good file -> atomic replace. One autosave slot plus previous-good backup; three manual slots. No cloud or offline-time simulation.
Autosave after scene transitions, committed exchanges/activity completion and sleep; manual save from pause menu when no uncommitted UI transaction exists. An active activity saves only a stable step boundary, never midway through applying a delta.
Restore active activity at saved step with pause lease re-established. No second wage, supply or time charge. Saved input focus is not trusted; rebuild focus explicitly.
Future save versions: do not load destructively. Show incompatibility, retain file and allow backup. Invalid/truncated save: offer previous valid backup. Missing optional content: diagnostic and safe unavailable state; unknown inventory/crop IDs cause validation failure instead of silently dropping goods.
Test fixtures are isolated from production slots, labeled Prepared Slice; resetting requires explicit confirmation and affects test slots only.

## 11. Architecture and scope

Godot 4/GDScript target, exact version to be pinned at implementation. No engine API assertions or existing scene files implied.
Ownership:
- ClockCalendar owns time/date and pause leases.
- InventoryEconomy owns item/money transactions.
- Farm owns plots/growth/can state; overnight subscribes once.
- NPCSchedule owns travel destinations; EventDirector owns actor reservations.
- RelationshipService owns evidence and independent pair states.
- VenueService owns menu stock and service reservations.
- SaveCoordinator snapshots these services and validates load.
- UI displays state and issues commands; never independently awards rewards.
Commands return structured success/error; emit change notification only after atomic commit. Every reward/stock transfer has an idempotency key.
Suggested future paths: game/project.godot; game/scenes/{farmhouse,exterior,venue}.tscn; game/scripts/{systems,actors,ui}; game/data/public_fixture; tests/. These are planned paths, not files created by this package.
In scope: one job, one menu transformation, one shift, one favor, three schedules, six plots, clock/save/load and 2D proof checks.
Out of slice: romance, children, major festivals, private relationship drama, full shop arcs, wide map, livestock, combat, large economy.

## 12. UI, accessibility and art checklist

HUD date/time/money only plus contextual prompt; can charge indicator when selected. Inventory displays counts and exact transaction changes.
Keyboard and controller focus for every action; remappable inputs and hold-free interactions. Pointer optional; service can be completed using focus/confirm only. Text scale 100/125/150%; layouts wrap without clipping. No color-only crop/order states.
Pause anytime outside atomic writes; reduced-motion toggles ambient loops and camera smoothing; no speed bonus for fast readers; assist completes one service assembly step on request without reducing wage.
Target QA viewports initially 1280x720 and 1920x1080, provisional desktop/handheld readability checks, not platform shipping promises.
Respect art bible: fully 2D, foot anchors, split occluders, explicit bridge layer transitions, readable silhouettes, no generic pixel/faux-3D final assets.

## 13. Review and execution

See [acceptance checks](acceptance.md), [implementation backlog and role briefs](cursor-handoff.md) and [data contract](data-contract.md).
Public fixture JSON is synthetic, structurally checked, and not Godot-imported. Private cast/story mappings belong in Drive. Do not commit secrets in fixtures, logs, PR descriptions or prompt attachments.
Main highest risk: a technically correct day could feel transactional. Human playtest must examine choosing company, not just task completion. No statement of fun or runtime correctness follows from data validation.
