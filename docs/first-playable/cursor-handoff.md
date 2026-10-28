# Cursor implementation handoff

This package supplies role briefs and a sequenced backlog. It does not install Cursor agents, create cloud agents or claim a running Godot project.
Read root AGENTS.md, docs/art-direction.md, this folder's README, data-contract and acceptance plan. Prototype defaults are editable; preserve approved pillars.
Use one implementation task at a time until system ownership and save boundaries stabilize. These roles can be run sequentially in Cursor; no extra tool subscriptions required.

## Dependency-ordered backlog

| ID | Work and owned scope | Depends on | Done evidence |
|---|---|---|---|
| FP-01 | Pin installed stable Godot 4 version; create game/ scaffolding, two transitions, 2D movement/depth proof | none | Actual editor import/run log, occlusion/bridge/door capture |
| FP-02 | ClockCalendar, pause leases, calendar and day-end | FP-01 | QA 02–05,27 and automated rollover/pause checks |
| FP-03 | Validated state model and SaveCoordinator skeleton | FP-02 | Roundtrip initial fixture, corrupt/future version recovery |
| FP-04 | InventoryEconomy and six-plot Farm | FP-03 | QA 06–09; atomic overflow; overnight idempotence |
| FP-05 | Three NPC schedules, interaction pinning and event arbitration | FP-02,FP-03 | QA 10; route and lease conflicts demonstrated |
| FP-06 | Helper job, relationship evidence and Community Standing | FP-04,FP-05 | QA 11–12,20,23–24 |
| FP-07 | Venue contribution, stock reservation and three-order shift | FP-04,FP-05 | QA 13–19 including midshift save |
| FP-08 | Reciprocal favor, independent leisure/seat invitations | FP-06 | QA 21–22,31; changed behavior persists |
| FP-09 | Integrate service evidence, complete save/recovery and daily reset | FP-06,FP-07,FP-08 | QA 19,25–27,32; no replay reward |
| FP-10 | Accessibility, readable temporary art and complete QA sweep | FP-09 | QA 01–32 actual results, honest failures |
| FP-11 | Human playtest and tune configuration | FP-10 | Observation notes; before/after values and findings |

Do not mark tasks Done because files exist. Pin API documentation to the chosen engine version during implementation. No release/version number is assumed by this planning package.

## Canon Guardian role brief

Input: approved public specs; authorized private sources only when available.
Task: review proposed changes for calendar, crop-only scope, 2D direction, optional romance/family and independent NPC relationships. Classify APPROVED / prototype default / proposed canon / conflict.
Output: concise findings with exact source and changed file. Never author missing history to make a mechanic work.
Public-review output must omit secrets, private quotes and character-specific unreleased events.

## Godot Architect role brief

Input: contracts and current repository. First task FP-01 boundary design.
Task: propose scene/service ownership, persistence boundaries, commands and event notification order. Validate atomic item/time/reward transactions and actor leases. Pin actual engine before using API claims.
Output: narrow implementation notes and scaffold; no speculative full-town or generalized framework expansion.
Review: ensure future systems can use data without replacing the slice.

## Godot Developer role brief

Input: one backlog ID, dependencies, contracts and acceptance IDs.
Task: implement only that increment in GDScript. Use anonymous fixture and labeled placeholder art until creator-approved source is available. Add focused tests for invariants, run available editor/headless checks and disclose unavailable checks.
Output: changed paths, behavior, test commands/results, remaining limits. Do not modify unrelated files or implement parked features.
Cannot award progression in UI callbacks independently of the owning transaction service.

## QA & Playtest role brief

Input: build commit, pinned engine, fixture and acceptance.md.
Task: independently reproduce happy and alternate paths, prioritize save/reload duplication, time charging, unavailable NPCs, overflow and blocked event branches. Check keyboard/controller/reduced motion and larger text.
Output: reproducible issues with expected/actual behavior; engine evidence and player findings reported separately.
Never infer a pass from reading code. Human playtest results require actual participants.

## First Cursor task (ready to paste)

Implement FP-01 in the existing Rooted repository. Read AGENTS.md and docs/first-playable/README.md first. Inspect the checkout before creating files. Establish the installed Godot 4 version and use its official API documentation. Create the smallest fully 2D movement/depth/doorway proof under game/, using anonymous placeholders and the three planned scene roles. Reuse the existing art-direction constraints, including feet anchors and explicit bridge elevation. Do not add the full farm, festivals, private dialogue or character history yet. Report exact engine execution and blockers honestly. Keep this increment on a review branch and provide its runtime evidence before expanding to FP-02.

## Review boundaries

Significant code changes receive review before merge. Routine reversible technical choices are delegated; do not ask the creator for every variable. Escalate only conflicts with canon, major creative scope or irreversible publication. Provisional defaults are reviewable in one package.
