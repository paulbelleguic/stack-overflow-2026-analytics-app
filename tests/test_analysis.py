import pandas as pd

from src.analysis.common import frequency_table, adoption_by, known_rate
from src.filters import filter_population
from src.population import ai_status, prepare_population, PRIMARY_CODER


def test_missing_and_conflicting_ai_answers_are_not_non_use():
    assert pd.isna(ai_status(None))
    assert pd.isna(ai_status("I don’t use AI tools;AI coding assistants or coding agents"))
    assert ai_status("I don’t use AI tools") is False
    assert ai_status("AI coding assistants or coding agents;General-purpose AI chat tools") is True
    assert pd.isna(ai_status("an unrecognised future answer"))


def test_multiple_choices_count_people_once_and_keep_answer_denominator():
    frame = pd.DataFrame({"ResponseId": [1, 2, 3, 4], "tools": ["A;B;A", "A", None, ""]})
    table, n = frequency_table(frame, "tools", multiple=True)
    assert n == 2
    assert table.set_index("answer").loc["A", "respondents"] == 2
    assert table.set_index("answer").loc["B", "share_pct"] == 50
    assert table["share_pct"].sum() == 150


def test_unknown_is_excluded_from_rate_but_false_is_retained():
    frame = pd.DataFrame({"ai_user": pd.Series([True, False, pd.NA], dtype="boolean")})
    rate, n = known_rate(frame, "ai_user")
    assert rate == .5 and n == 2


def test_small_groups_are_reported_but_not_given_a_rate():
    frame = pd.DataFrame({"group": ["A", "A", "B"], "ai_user": [True, False, True]})
    table, n = adoption_by(frame, "group", minimum=2)
    table = table.set_index("group")
    assert n == 3 and table.loc["A", "share_pct"] == 50
    assert table.loc["B", "answers"] == 1 and pd.isna(table.loc["B", "share_pct"])


def test_population_scope_and_experience_outlier_do_not_remove_unknown_ai():
    frame = pd.DataFrame({
        "ResponseId": [1, 2, 3, 4], "Country": ["France", "France", "Germany", "France"],
        "CodeMain": [PRIMARY_CODER, PRIMARY_CODER, PRIMARY_CODER, "I create code occasionally"],
        "WorkExp": [4, 100, 8, 2], "AISelect": [None, "I don’t use AI tools", "AI coding assistants or coding agents", None],
        "Role": ["Back-end"] * 4, "Employment": ["Employed"] * 4,
    })
    selected = prepare_population(frame)
    assert selected["ResponseId"].tolist() == [1, 2]
    assert pd.isna(selected.loc[1, "experience_years"])
    assert len(filter_population(selected)) == 2
    assert len(filter_population(selected, experiences=["3–5 years"])) == 1


def test_no_answers_returns_an_empty_table_and_known_zero_denominator():
    table, n = frequency_table(pd.DataFrame({"ResponseId": [1], "answer": [None]}), "answer", True)
    assert table.empty and n == 0
