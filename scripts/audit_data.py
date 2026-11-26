"""Regenerate the aggregate coverage report; no respondent rows are exported."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data import ensure_data, load_responses, load_schema, ROOT
from src.population import prepare_population, PRIMARY_CODER

FIELDS = {
    1: ["AISelect", "WorkExp", "Role", "Employment"],
    2: ["AICodeAgentHaveWorkedWith", "AICodeAgentWantToUseNext6Months", "LLMHaveWorkedWith"],
    3: ["AIWorkCurrentlyUse", "AIWorkExpectMore", "AIWorkDoNotPlanToUse"],
    4: ["AITrust", "AIWorkNext", "AISentiment"],
    5: ["LearnAI", "LearnAIHow", "AIAdopt"],
}


def main():
    ensure_data()
    raw = load_responses()
    schema = load_schema().set_index("column")
    selected = prepare_population(raw)
    missing_fields = set(sum(FIELDS.values(), [])) - set(raw.columns)
    if missing_fields:
        raise ValueError(f"Required fields missing: {missing_fields}")
    lines = [
        "# Verified 2026 data audit", "",
        "This report was generated from the official response CSV and schema. It exports aggregate counts only.", "",
        f"- Source responses: **{len(raw):,}**; fields: **{len(raw.columns)}**.",
        f"- France: **{raw['Country'].eq('France').sum():,}**.",
        f"- France and `{PRIMARY_CODER}`: **{len(selected):,}**.",
        f"- Unique response IDs: **{raw['ResponseId'].is_unique}**.",
        f"- Known derived AI-use answers: **{selected['ai_user'].notna().sum():,}**; unknown: **{selected['ai_user'].isna().sum():,}**.",
        f"- Unknown experience after the documented plausibility rule: **{selected['experience_years'].isna().sum():,}**.", "",
        "## Answer coverage before interactive filters", "",
        "| Axis | Verified field | Answered | Unanswered | Multiple selections / matrix-derived list? |",
        "|---|---|---:|---:|---|",
    ]
    for axis, fields in FIELDS.items():
        for column in fields:
            answered = selected[column].notna().sum()
            multiple = "semicolon" in str(schema.loc[column, "transformation"])
            lines.append(f"| {axis} | `{column}` | {answered} | {len(selected) - answered} | {'Yes' if multiple else 'No'} |")
    lines += ["", "## Interpretation of coverage", "",
              "The five axes have usable initial answer counts, but counts fall after filtering. Fields inside one axis do not necessarily share an answering population. Missing values may reflect routing or non-response. In particular, a blank matrix-derived current-task list cannot be interpreted as observed non-use for every task.", "",
              "The source schema and archived questionnaire must be checked again when an owner adds a field. Counts in this report describe this fixed 2026 archive, not the French workforce.", "",
              "Source: Stack Overflow Developer Survey 2026, ODbL 1.0. Download locations and basic file checks: `src/data.py`.", ""]
    target = ROOT / "docs" / "DATA_AUDIT.md"
    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote aggregate audit: {target}")


if __name__ == "__main__":
    main()
