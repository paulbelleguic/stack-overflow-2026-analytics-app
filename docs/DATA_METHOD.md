# Sources and shared calculation rules

## Verified 2026 source

The official response CSV has 30,903 rows and 212 fields. The official schema has fields including `column`, `question`, `sub`, `transformation` and `nonmissing`. Both CSVs are stored with Git LFS; the downloader uses `media.githubusercontent.com/media/…` and checks the official SHA-256 fingerprints.

The schema and the [2026 question bank](https://github.com/StackExchange/Survey/tree/releases/2026/questions) are the references for wording and conditional questions. Do not assume an unanswered conditional question means a respondent rejected its premise.

## Eligible population

France (`Country`) and coding as the primary part of the job (`CodeMain`), across all industries: 628 respondents. No join is necessary. An answer's key is `ResponseId` within 2026. If another edition is later added, use `(year, ResponseId)`; the same number in two years does not identify the same person.

The dataset cannot identify a representative sample of DINUM or French public-sector developers. Present it to the sponsor as an exploratory benchmark from volunteers.

## Multiple-choice answers

Verified columns including `AISelect`, coding-assistant lists, workflow lists, `AIWorkNext`, `LearnAIHow` and `AIAdopt` use semicolon-separated selections. Split them, trim spaces and remove duplicate `(ResponseId, choice)` pairs. Divide each choice's count by the number of selected respondents with a non-empty value in that specific field. The sum can exceed 100%.

For matrix-derived workflow columns, people answering another matrix column are not automatically known non-users of the currently displayed tasks. Each view states its own column denominator. Used and wanted tool lists also have different answering populations and time windows; they are not a direct conversion or growth rate.

## Derived AI-use indicator

- Any of the four verified positive `AISelect` tool categories → `True`.
- Only `I don’t use AI tools` → `False`.
- Missing, unknown categories or a contradictory combination of use and non-use → unknown (`pd.NA`).

The adoption denominator contains only known `True` and `False` values. Unknown values remain in the eligible population and are reported separately. This indicator is self-reported current use, not measured usage logs.

## Experience

`WorkExp` is converted to a numeric field, retaining values between 0 and 80 years inclusive. Out-of-range or unparseable values are unknown, while the raw field remains available. The 80-year bound is a declared plausibility check, not a source-provided threshold. Groups are 0–2, 3–5, 6–10, 11–20 and 21–80 years. Unknown experience remains eligible unless a group filter is selected.

## Interpretation

The dashboard's AI-use and trust rates have different denominators; they are not a paired comparison. Tool popularity does not establish quality. Self-reported checks do not establish that outputs are correct. Training activity does not establish learning benefit. A minimum of 20 answers reduces especially sparse charts but does not confer representativeness or significance.

Source attribution: **Stack Overflow Developer Survey 2026**, data ODbL 1.0, contents DbCL 1.0. No individual respondent rows are committed to this repository.
