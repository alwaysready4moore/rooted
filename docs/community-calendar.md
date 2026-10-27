# Community and calendar direction

Updated October 27, 2026. Status: approved design principles and explicitly labeled prototype work. No gameplay implementation or runtime validation is claimed.

## Approved calendar

- Four seasons: Spring, Summer, Autumn, Winter.
- 30 days per season; 120 days per year; no separate months.
- Date format: Spring 7, Year 1.
- This supersedes the 28-day-season and twelve-month proposals.
- Weekday model, starting weekday, daily clock, pause behavior, season-transition rules and aging remain unspecified.

## Community progression

The central experience is joining an already-functioning community. Friendship changes residents' behavior and the player's everyday life through visits, invitations, collaboration and reciprocal assistance.

Dating, marriage and children are optional. Friendship-only and child-free play must support a complete main progression experience. Family mechanics remain to be specified; do not treat them as a required ending or highest progression tier.

Residents have relationships and histories with each other, independent of the player. Their schedules and shared events should reflect those connections. Canonical character relationships and unpublished stories remain in the creative source of truth; do not invent them from this public specification.

Character stories and seasonal life continue beyond Year 1. Seasons provide context rather than a compulsory deadline to complete personal arcs.

## Seasonal celebrations

Approved direction:
- Each season has visible anticipation, preparations, decorations and opportunities for social participation.
- Winter includes a warm Christmas-style community celebration with food, gifts and music.
- A Halloween-style celebration occurs at the end of Autumn.
- The calendar can include smaller occasions alongside major festivals.
- Participation does not require donating goods, volunteering, romance or parenthood.

Specific festival names, exact dates, activities, weather requirements and operating hours remain proposals. Do not hard-code the illustrative private calendar as final.

## Relationship behavior requirements

Accepted design direction, implementation details pending:
- Separate casual visits, invitations and planned assistance.
- Residents retain independent work, preferences and availability.
- Keep leisure and ordinary companionship alongside practical benefits.
- Major friendship scenes should lead to observable recurring behavior.
- Resident-to-resident event progression is separate from romance with the player.

Prototype assumptions to validate:
- Avoid stacking several visitors at the farm.
- Make time commitments legible before accepting an activity.
- Provide later opportunities for essential personal events.
- Define scheduling, eligibility, cooldowns, attendance overrides and save/load persistence before implementation.
- Avoid reward systems that imply affection is purchased through expensive gifts.

## First playable scope

Preserve the broader community-loop slice: small plant-care routine; three scheduled residents; one active odd job; an ingredient changes the venue menu; a short service shift; visible relationship or Community Standing change; one reciprocal favor.

The compact 2D art proof and the separate standalone engine experiment are distinct from that broader slice. Complete festival systems and full relationship routes are later content.

## Next implementation contracts

1. Daily time and calendar rollover.
2. Minimum farm, inventory and ingredient/menu rules.
3. NPC schedules and relationship-dependent overrides.
4. Event IDs, prerequisites, choices and retry behavior.
5. Community Standing and individual relationship behavior.
6. Recurring visits, assistance and saved-state persistence.
7. Runtime acceptance checks for the vertical slice.

Suggested calendar checks: day 30 advances to day 1 of the next season; Winter 30 advances to Spring 1 of the next year; invalid dates are rejected; save/load preserves the date. These checks are proposed, not executed.

## References and publication boundary

Primary creative inspirations are Harvest Moon: Back to Nature, DS and A Wonderful Life. Those references do not authorize copying assets or automatically importing mechanics such as aging.

Keep unpublished character histories, secret identities, reveal explanations, private design documents and dialogue out of this public repository. The private creative documents distinguish APPROVED, DEVELOPMENT DIRECTION, PROPOSED and OPEN material. Do not promote proposals into canon.

See [art direction](art-direction.md) and [agent guidance](../AGENTS.md).
