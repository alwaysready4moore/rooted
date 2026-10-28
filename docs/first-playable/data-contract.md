# Data contract v0.1

Status: prototype defaults. JSON is engine-neutral test content, not a functioning event engine or final narrative. Public NPCs are anonymous. Read definitions.json and prepared-save.json under prototype/first-playable/.

## Definitions

format_version integer=1; content_version string=slice-0.1; status=ASSUMED_FOR_PROTOTYPE; public_fixture=true.
calendar: days_per_season=30; seasons ordered spring/summer/autumn/winter; week_days=7; start_weekday=0. Week values are provisional.
clock: positive seconds_per_game_minute; wake_minute and cutoff_minute are minute offsets in [0,1440], wake < cutoff.
items: unique IDs, kind produce or seed; seed purchase price nonnegative integer.
crops: unique ID, existing seed_id and harvest_id; watered_nights positive integer, yield positive integer. Single-harvest only.
locations: unique logical scene/anchor IDs; actual coordinates and paths belong in scenes.
npcs: unique IDs; schedule intervals [start,end) contiguous from wake to cutoff; location references must resolve. Schedule time is a desired destination: actors physically travel, never pop between on-screen anchors.
schedule_overrides: priority overrides normal destination within interval when all required flags and no unless flags hold. Active activity leases outrank overrides. Unknown flags are errors.
venue: explicit open/close window, duration, latest start, order count, contribution quantity and batch yield, recipe step lists.
events: unique id; kind; actor; location or any; inclusive earliest start and exclusive window end; integer duration; depends_on list; repeat policy; abstract effect IDs; optional condition ID. An activity may finish exactly at window end. Eligibility alone never applies effects.

## Effect semantics

record_contact: add current absolute_day once to actor's contact_days.
set_helper_chat: set flag helper_chat after conversation.
pay_job/pay_shift: award configured wage only at completion, protected by transaction key.
set_helper_job_done: flag plus completed FP_JOB.
add_job_category/add_supply_category/add_service_category: add unique category; recalculate stage.
take_mint/add_herb_stock: one atomic contribution exchange, both or neither.
set_helper_visit_eligible: derive from completed FP_CHAT_HELPER and FP_JOB; these survive day rollover.
repair_gate: set gate_repaired once, complete FP_FAVOR; no pay.
set_neighbor_invitation_available: stage transition enables optional FP_SEAT, not forced dialogue.
Conditions: two_distinct_categories means at least standing.neighbor_distinct_categories unique categories.
depends_on means prerequisite has completed at least once. Daily/repeatable events retain first completion in completed_events and use daily_records for repeat eligibility. FP_LEISURE requires chat only, not job/favor/standing.
Derived events use no actor interaction; actor identifies whose subsequent behavior changes.
Do not implement arbitrary executable code embedded in JSON.

## Save types and invariants

save_version integer=1; fixture_id prepared-community-day; matching content_version.
clock: absolute_day >=0 integer; minute_of_day integer within wake/cutoff inclusive; subminute in [0,seconds_per_game_minute). Calendar derives from absolute_day.
player: scene known; position two finite numbers; coins nonnegative integer.
inventory: array <=slots; each stack existing item_id, quantity 1..stack_limit integer. Multiple stacks of same item allowed when needed.
farm: can_charges 0..capacity; exactly plot_count uniquely identified plots; last_processed_day=absolute_day-1 at a stable boundary. Each plot: tilled bool, crop_id known/null, growth 0..crop maturity integer, watered bool. Empty plots have growth=0 and watered=false; planted plots must be tilled.
npcs: one entry per configured NPC, anchor/destination known. On load reconstruct travel path; saved anchors must exist in scene data.
relationships: one entry per NPC; met bool; unique nonnegative contact_days <=current day; unique evidence strings; romance none in public slice. New interactions never mutate pair_relationships implicitly.
pair_relationships: map of two distinct sorted NPC IDs joined with | to an authored string state. Empty fixture; no private story history here.
flags: exactly definition flag names, boolean values.
community: unique allowed categories; stage newcomer below threshold else neighbor. Relationship flags are never substituted for category evidence.
venue.herb_stock nonnegative integer; excludes servings reserved by active_activity.
completed_events: unique existing event IDs, representing first completion.
transactions: unique nonempty strings, never cleared at day rollover. Keys include event, day/instance and action; receipt written with mutation.
daily_records: keys existing event IDs; values unique day integers <=current day, used to cap successful repeats. No-action cancellation writes no completion.
visits: at most one reservation for farm; {npc_id, day, start, end}, valid NPC/date/time. Persist postponement and reconstruct routes.
active_activity: null or object defined below. No transient input/animation/UI-node references in saves.

## Active activity object

Fields: event_id (job, shift, favor or invitation), instance_id (unique string), day (current absolute_day), start_minute, end_minute=start+event.duration, committed bool, step_index nonnegative integer, reserved_herb nonnegative integer, orders array, placements array.
For shift: orders exactly 3 recipe IDs; step_index counts completed orders 0..3; reserved_herb equals the number of remaining herb_drink orders. One herb order maximum in slice. placements empty.
For job: orders empty, reserved_herb=0; placements unique values spot_a/spot_b/spot_c and step_index equals count 0..3.
For other activities: empty orders/placements, reserved_herb=0, step_index 0.
Clock remains at start while active. All completion effects, return of unused reservations, timestamp advancement and activity removal occur in one atomic transaction. Snapshot before or after it, never halfway.
The supplied validator checks these structures and cross-references. It does not execute Godot movement, schedules, transactions, growth or event effects.

## Data ownership and extension

Definitions are immutable during a save. If content changes meaning, bump content_version and supply an explicit migration; do not silently load incompatible content.
Adding a character requires schedule, reference IDs, relationship initial state and authored dialogue. Adding events requires repeat/cancel/save semantics plus acceptance cases.
Keep real actor assignments and narrative in private source. Importing private canon into a local working build is not permission to publish it.
