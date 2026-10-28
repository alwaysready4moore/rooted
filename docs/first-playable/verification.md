# Verification record — framework v0.1

Prepared October 27, 2026.

Executed locally:
- python tools/validate_first_playable.py --self-test
- Initial prepared save and two active-shift snapshots passed structural and cross-reference validation.
- 19 deliberately invalid mutations were rejected (including missing references, a dependency cycle, schedule gap, invalid stock reservation, duplicate receipt and future save version).
- Synthetic active-shift JSON serialization roundtrip preserved all fields.

These tests validate the data package and validator behavior only. They do not execute production gameplay or demonstrate that a future implementation is correct.

Not executed: Godot project import, engine runtime, rendering, movement, controller checks, actual atomic save-file recovery, runtime transactions, human playtest or exported build.
Acceptance IDs FP-QA-01 through FP-QA-32 remain NOT RUN.

Reproduce from repository root with Python 3 (standard library only):
```sh
python tools/validate_first_playable.py --self-test
```

The JSON fixtures contain anonymous synthetic residents and no private narrative. The creator-facing Drive review supplies proposed cast assignments separately. New data defaults are ASSUMED_FOR_PROTOTYPE; existing approved directions remain marked in the specification.
