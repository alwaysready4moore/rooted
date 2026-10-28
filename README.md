# Rooted

**Rooted** is a cozy fantasy community life sim set in **Bluebird Bay**, a lived-in coastal town. The player cultivates plants, contributes to local businesses, develops relationships, and becomes part of the community through everyday routines and reciprocal help.

## Approved visual direction (October 27, 2026)

- **Entirely 2D**, hand-illustrated in the project's **House Art Style**.
- Fixed **elevated three-quarter view** with 2.5D-inspired depth made from separate 2D illustration layers.
- **Directional 2D character sprites**, a gently following 2D camera, ambient sprite animation, and correct foreground/behind-object occlusion.
- Readable, compact chibi silhouettes, confident ink contours, bright controlled color, matte texture, and restrained UI.
- No 3D models/geometry, no faux 3D camera, and no pixel-art production requirement. Earlier Harvest Moon DS/FoMT pixel-art notes are superseded.
- The former setting name **Hearthshore** is obsolete. Use **Bluebird Bay** in all new content, assets and code.

Read [the 2D art and technical specification](docs/art-direction.md) before producing scenes, sprites or UI.

## Engine and status

**Godot 4.x / GDScript** is the *recommended prototype environment*, pending hands-on runtime validation. The repo currently records design and implementation requirements; it does **not** yet contain a verified running game.

The first proposed art proof is a compact Bluebird Bay outdoor scene testing character movement, depth sorting, bridge/stair layering, foreground occlusion, ambient animation, an NPC interaction, and a doorway transition. This is a **prototype proposal**, not a locked final map.

Rooted's priorities are community participation, manageable crop-focused farming, relationship building, and low-pressure progression. Core mechanics should serve those priorities.

## Calendar and community direction (October 27, 2026)

Rooted uses four **30-day seasons**, for a **120-day year**, without separate months. Friendship and community belonging support a complete experience; dating, marriage and children are optional. Residents have relationships of their own, and friendship should visibly change daily routines and reciprocal assistance.

Seasonal celebrations include a Christmas-style winter gathering and Halloween-style festivities at the end of Autumn. Exact festival dates and names remain proposed.

Read [the community and calendar specification](docs/community-calendar.md) for approved principles, open decisions and prototype scope.

## First playable review package

The [first-playable framework](docs/first-playable/README.md) supplies system contracts, a prepared test day, synthetic data fixtures, 32 runtime acceptance checks, and a dependency-ordered Cursor backlog. New tuning values are provisional. The fixture validator passes; a playable Godot build has **not** been created or engine-tested.

## Working with Cursor

Consult [AGENTS.md](AGENTS.md) for implementation guardrails and acceptance criteria. Prototype one slice and validate in the actual Godot editor before expanding the asset library or claiming gameplay is operational.

## Documentation and canon

Full narrative and character canon, including unpublished material, remains in the private project Google Drive. This public repository should contain only spoiler-safe design/engineering guidance. Do not invent lore, reveal unreleased character/story details, or publish the private Game Bible and art references here.
