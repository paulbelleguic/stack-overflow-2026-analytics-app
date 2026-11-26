# 2025 comparison policy

**No 2025 comparison is implemented or displayed in the starter app.** All figures and source counts are 2026. The project must not silently substitute another year if the 2026 source fails.

The optional comparison can only be enabled after an owner documents and reviews the following for every field:

| Required evidence | What to record |
|---|---|
| Source and question | Official 2025 and 2026 files, field names, exact wording and routing |
| Actual categories | Observed answers and missing counts in each edition |
| Mapping | Each original answer mapped to a common category; unknown and excluded values explicit |
| Denominators | Eligible people, people asked the question, and valid answers, separately by year |
| Scope | Whether the two definitions describe comparable populations |
| Limits | Changed response options, selection, wording, and conditional questions |
| Validation | Tests for mappings, unexpected answers and duplicates; one concrete table checked manually |

Known warnings from the verified 2026 schema and the supplied earlier survey exercise:
- `CodeMain` in 2026 is not simply the old `MainBranch` label: coding as a primary job and being a professional developer need a reasoned scope comparison.
- `AISelect` in 2026 is a multiple-choice list of tool types plus explicit non-use. A rule matching the literal `Yes` or the 2025 usage frequencies is invalid for 2026.
- Workflow questions, trust categories and tool catalogues may have changed. Matching similar column names is insufficient.

Until this work is complete, adding a 2025 selector or a growth claim would be misleading. An honest 2026-only project meets the assignment's optional-year requirement.
