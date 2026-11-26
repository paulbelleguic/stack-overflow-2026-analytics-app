"""Dénominateurs explicites pour les questions simples et multiples."""
import pandas as pd


def valid_answers(frame, column):
    return frame[column].notna() & frame[column].astype(str).str.strip().ne("")


def frequency_table(frame, column, multiple=False):
    """Renvoie (table, nombre de répondants ayant renseigné cette colonne).

    Une modalité n'est comptée qu'une fois par répondant. Pour une colonne issue
    d'une matrice, le dénominateur est celui de cette colonne, pas de toute la matrice.
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


def adoption_by(frame, group_column, minimum=20):
    valid = frame.dropna(subset=[group_column, "ai_user"])
    table = valid.groupby(group_column, observed=True)["ai_user"].agg(answers="size", users="sum")
    table["share_pct"] = table["users"] / table["answers"] * 100
    table["sufficient_n"] = table["answers"] >= minimum
    table.loc[~table["sufficient_n"], "share_pct"] = float("nan")
    return table.rename_axis("group").reset_index(), len(valid)
