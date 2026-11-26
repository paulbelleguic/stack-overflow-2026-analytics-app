# Verified 2026 data audit

This report was generated from the checksum-verified official response CSV and schema. It exports aggregate counts only.

- Source responses: **30,903**; fields: **212**.
- France: **794**.
- France and `I create code as a primary part of my job`: **628**.
- Unique response IDs: **True**.
- Known derived AI-use answers: **507**; unknown: **121**.
- Unknown experience after the documented plausibility rule: **21**.

## Answer coverage before interactive filters

| Axis | Verified field | Answered | Unanswered | Multiple selections / matrix-derived list? |
|---|---|---:|---:|---|
| 1 | `AISelect` | 510 | 118 | Yes |
| 1 | `WorkExp` | 608 | 20 | No |
| 1 | `Role` | 627 | 1 | No |
| 1 | `Employment` | 628 | 0 | No |
| 2 | `AICodeAgentHaveWorkedWith` | 334 | 294 | Yes |
| 2 | `AICodeAgentWantToUseNext6Months` | 201 | 427 | Yes |
| 2 | `LLMHaveWorkedWith` | 332 | 296 | Yes |
| 3 | `AIWorkCurrentlyUse` | 303 | 325 | Yes |
| 3 | `AIWorkExpectMore` | 260 | 368 | Yes |
| 3 | `AIWorkDoNotPlanToUse` | 246 | 382 | Yes |
| 4 | `AITrust` | 388 | 240 | No |
| 4 | `AIWorkNext` | 355 | 273 | Yes |
| 4 | `AISentiment` | 389 | 239 | No |
| 5 | `LearnAI` | 628 | 0 | No |
| 5 | `LearnAIHow` | 434 | 194 | Yes |
| 5 | `AIAdopt` | 337 | 291 | Yes |

## Interpretation of coverage

The five axes have usable initial answer counts, but counts fall after filtering. Fields inside one axis do not necessarily share an answering population. Missing values may reflect routing or non-response. In particular, a blank matrix-derived current-task list cannot be interpreted as observed non-use for every task.

The source schema and archived questionnaire must be checked again when an owner adds a field. Counts in this report describe this fixed 2026 archive, not the French workforce.

Source: Stack Overflow Developer Survey 2026, ODbL 1.0. File hashes and download locations: `config/sources.json`.
