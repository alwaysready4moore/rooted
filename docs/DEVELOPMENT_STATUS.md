# Rooted — public development status

Updated 2026-10-20.

## Current status

- Rooted: concept and design documentation, no validated executable build.
- Engine direction: Godot 4 / GDScript, **not final until actual import and movement/interaction testing**.
- Lux's Little Tea Shop: independent Godot source ZIP in Google Drive. The ZIP has been structurally checked, but has **not** been executed in Godot or tested with players.
- Current GitHub PR: public overview and approved mechanical decisions. The standalone project's complete source files are **not yet mirrored as extracted code in this branch**. Do not mistake its Drive link for a GitHub source checkout.

## Source of truth

- [Rooted Drive workspace](https://drive.google.com/drive/folders/1uZkuzvTPPbHrOXsdGrf2z0c-iJ--NZgu): Game Bible, Game Design Document, crop catalog, character design guide, mega roster, art archive and development tracker.
- [Lux's Little Tea Shop workspace](https://drive.google.com/drive/folders/1bjX5Cq_G6W9OIvsRUOFRH_a2aLCnJevT): standalone mini-game brief and source project ZIP.

Those Drive files are not automatically synced into GitHub. The linked documents' effective sharing permissions are **not verified**; do not assume they are public.

## Relevant current design

Rowan's farm is **plant-only**. It can produce crops, herbs, seasonings, flowers and fruits. There is no player livestock farming, no breeding and no animal-output production loop. Companion pets are a separate optional idea. A local husbandry NPC, not yet designed, would supply animal-derived ingredients for cooking and trade. Art offers a manageable farm workload when Rowan arrives and would not place animal care on them as an initial responsibility.

## Work still needed

1. Transfer the approved Lux Godot source files from its ZIP into GitHub as reviewable scripts/scenes/assets, avoiding story spoilers and licensed third-party data.
2. Import in a verified stable Godot 4.x editor; fix any parser/runtime errors.
3. Validate movement, collisions, ingredient selection, six-customer flow and save/resume.
4. Test approved character artwork at real game scale and accessibility settings.
5. Prototype Rowan's ingredient delivery, a changed tea menu and at least one moving scheduled visitor.
6. Review and approve changes before merging a PR into `main`.

Historical story planning remains on `agent/rooted-story-foundation`, not automatically merged because it predates newer canon.
