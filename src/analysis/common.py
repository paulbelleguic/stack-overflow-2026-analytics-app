"""Explicit denominators for single- and multiple-choice questions."""
import pandas as pd


def valid_answers(frame, column):
    return frame[column].notna() & frame[column].astype(str).str.strip().ne("")


def frequency_table(frame, column, multiple=False):
    """Return (table, number of respondents answering this field).

    Count each choice once per respondent. For a field derived from a matrix,
    use this field's answer denominator, not the full matrix population.
    """
    answered = frame.loc[valid_answers(frame, column), ["ResponseId", column]].copy()
    n_answers = len(answered)
    if multiple:
        answered[column] = answered[column].str.split(";")
        answered = answered.explode(column)
        answered[column] = answered[column].str.strip()
        answered = answered.loc[answered[column].ne("")].drop_duplicates(["ResponseId", column])
    counts = answered[column].value_counts().rename_axis("answer").rename("respondents").reset_index()
    counts["share_pct"] = counts["respondents"] / n_answers * 100 if n_answers else 0.0
    return counts, n_answers


def known_rate(frame, column):
    answers = frame[column].dropna()
    return (float(answers.mean()) if len(answers) else None), len(answers)
