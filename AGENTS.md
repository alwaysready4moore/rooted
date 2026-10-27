# Cursor / Coding Agent Guidance for Rooted

Project: **Rooted**. Town: **Bluebird Bay** (never Hearthshore in new code, UI or asset paths).

## Start here
- `docs/community-calendar.md` owns the public calendar and community requirements: 30-day seasons, 120-day years, optional romance/family, and persistent friendship behavior. Festival dates/names and numeric system rules remain proposals.
- `docs/art-direction.md` is the approved visual direction and technical art acceptance checklist.
- Use Godot 4.x 2D/GDScript for a proposed proof; **do not imply a runtime version has been tested** unless it has.
- Keep all rendering fully 2D. Build depth by feet-based sorting, authored foreground masks and explicit elevation layers.
- Use temporary labeled placeholder art until House Art Style production assets are approved. Do not generate or treat generic pixel sprites as final.
- Keep art, physics/collision, navigation, story events and UI modular.

## Scope discipline
- First prototype: movement, correct occlusion, small bridge/elevation transition, NPC prompt/dialogue, ambient animation, and doorway transition.
- Keep story/character canonical sources private in Google Drive. This repository is public; **do not commit private docs, secrets, prompts revealing plot twists, unreleased dialogue or unapproved character sprites**.
- Art's venue and prototype scenery are test locations, not approved full-map content.
- Do not add animal ranching to Rowan's crop-focused farm or turn community participation into optimization pressure.

## Definition of done
A feature is complete only after editor/runtime verification and a repeatable test, not after files are generated. Log Godot version, errors, viewport sizes and screenshots for draw-order checks. Preserve the approved 2D and House Art Style constraint throughout revisions.
