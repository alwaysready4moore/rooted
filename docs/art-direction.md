# Rooted: Layered 2D Art Direction & Implementation Specification

**Status:** Visual direction approved October 27, 2026. Technical measures and scene details proposed pending implementation and playtest.

## 1. Design lock

- Canonical setting: **Bluebird Bay** (old development name: Hearthshore; do not use for new assets/content).
- Production rendering: **100% 2D**, no 3D models or 3D geometry.
- Perspective: fixed elevated **three-quarter** / top-down inspired view; illusion of dimensionality from layered illustrations and draw-order rules.
- Art language: project's **House Art Style** (rounded, original hand-illustrated chibi forms, distinctive silhouettes, organic weight-varying dark outlines, matte fills, subtle cel/pencil/watercolor texture, bright controlled palette).
- World composition: hand-illustrated environmental pieces, optional subtle ambient animation, directional 2D sprites, foreground occlusion.
- No pixel-art style, pixellated filter, sepia/yellow wash, glossy plastic/3D shading, hyper-detailed clutter, or cloned reference game UI.
- The fixed viewpoint does **not** imply a true 3D camera.

**Priority:** latest creator approval > character/project canon > House Art Style > experimental art defaults. Earlier pixel-art advice is historical.

## 2. Scene rendering model

Use separate elements for:
1. distant/backdrop paintings and architecture far surfaces,
2. walkable ground/paths (2D visual geometry),
3. interactable bases, props and colliders,
4. Y-sorted sprites/NPCs using foot-level anchor points,
5. split foreground occluders (roofs, foliage, railings, signs, counter tops),
6. screen-space HUD/dialogue.

Some items span multiple layers: a tree has trunk plus canopy, a counter has a base and lip, a house has background wall/door plus near roof overhang. Sort based on **feet/ground-contact location**, not sprite top-left or character centers.

For bridges and stairs: draw-order alone is insufficient. Author walkable/collision shapes and explicit **elevation/state transitions**; ensure the avatar renders in the correct layer when on the bridge and when walking beneath or alongside it. Keep interactions and nav paths consistent with the visual state.

## 3. Character production

- 2D sprite turnarounds with readable front/back/side idle and walking animation for an initial proof. Add diagonals only if needed.
- Avoid generic interchangeable chibi designs; maintain approved species traits, facial proportions, outfits and palette per character.
- Preserve one stable foot anchor and collision footprint through all animation frames.
- Side flipping is permitted only if costume/hair/accessories stay correct.
- Dialogue uses separate more expressive House Art Style portraits; keep identities consistent with overworld sprites.
- Do not set sprite resolution before testing actual on-screen size.

## 4. Ambient motion and camera

- Recommended Godot 4.x pieces: `Camera2D`, `Sprite2D` / `AnimatedSprite2D`, `AnimationPlayer`, `Area2D`, 2D collision and suitable tile/illustration layer nodes.
- Camera follows with modest smoothing and designed bounds; no free camera orbit.
- Animations: water ripple/flow, leaves/flowers, cloth/sign sway, selective light/weather details. Keep low-motion variants and avoid covering interactive objects.
- Animation must enhance life without becoming a requirement to understand important game states.

## 5. HUD and dialogue

- Minimal overlay during traversal; interaction prompt appears contextually in range.
- Use readable fonts, adequate contrast, scalable text and predictable keyboard/controller focus.
- House Art Style rounded interface treatments should share controls/padding/panel and icon motifs without overwhelming the illustrated town.
- Larger dialogue portrait, name, text and deliberate expression changes; don't animate every sentence.
- Inventory/business/noticeboard/minigame UI components should be reusable; exact layouts are not yet locked.

## 6. Asset organization (provisional)

Keep layered editable masters in the private art pipeline; only export approved spoiler-safe assets into this public repo. Suggested directories if game sources are later added:

```text
assets/
  environments/bluebird_bay/
  characters/
  props/
  ui/
scenes/
  world/
  characters/
  ui/
scripts/
  world/
  actors/
docs/
```

Potential names: `bb_art_venue_bg.png`, `bb_art_venue_roof_fg.png`, `bb_bridge_deck.png`, `rowan_walk_down_01.png`, `tuck_idle_side_01.png`. Use transparent PNGs for exported sprites/occluders; maintain their authored layer/source files separately. File names and resolutions are examples, not canon.

## 7. First environment proof (proposed, not canon map lock)

One small **Bluebird Bay** outdoor cluster near Art's venue with stream, footbridge, trees and a short footpath connecting toward the farm. The test uses Rowan's avatar and one NPC (e.g. Tuck). Do not invent a full town map or new character lore to implement this.

Demonstrate:
- consistent four-way walking, collision, stop/idle, camera follow;
- pass in front of/behind an occluder without draw-order popping;
- approach/leave bridge and stairs with correct layering/collision;
- water and foliage loop without distracting from interaction;
- NPC idle/moving state plus one contextual interaction prompt;
- dialogue panel with House Art Style portrait;
- clean doorway/scene transition.

This visual proof is **separate from** the broader gameplay vertical slice and the independent Lux's Little Tea Shop engine test. Do not mark mechanics completed based on documentation alone.

## 8. Acceptance test and status

- [ ] Actual Godot 4.x project opens without parser errors.
- [ ] Every world asset renders in 2D without pixelated/faux-3D effects.
- [ ] Sprite foot anchors and movement animation work in all supported directions.
- [ ] Correct behind/in-front occlusion at tree, house, counter or similar split objects.
- [ ] Bridge/stair elevation transitions behave correctly at approach and exit.
- [ ] Collision, doorway transition and interaction areas align with art.
- [ ] Ambient animation loops are seamless and reduced-motion setting has an appropriate effect.
- [ ] UI is legible at desktop/handheld viewport, keyboard and controller.
- [ ] Gameplay still expresses Rooted's low-pressure, community-first intent.
- [ ] Playtest evidence exists (capture + observed problems), and any issues are tracked.

**Undecided:** production export resolution, design viewport, camera zoom, sample map proportions, animation frame rates, exact GUI layout, sprite frames/diagonals, platform targets, art authoring/export tool.

**Internal authority:** the Rooted Google Drive Art Direction Bible and established House Art Style/character references. Do not publish private story Bible, confidential story beats or unreleased character disclosures in this public repository.
