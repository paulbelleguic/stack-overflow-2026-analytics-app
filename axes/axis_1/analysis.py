"""Simple descriptive comparisons for axis 1, without Streamlit."""
import pandas as pd


def with_career_groups(frame):
    """Use the shared cleaned experience; missing values stay ungrouped."""
    result = frame.copy()
    result["career_group"] = pd.cut(
        result["experience_years"], [-1, 5, 80], labels=["0–5 years", "6+ years"]
    )
    return result


def adoption_table(frame, group_column):
    """Summarise one row per respondent from the prepared population.

    selected_n includes unknown AI use; answered_n counts known True/False values.
    users_n counts True values. Unknown group values are excluded, while groups
    with zero usable answers keep an undefined use_pct rather than a zero rate.
    lower_pct and upper_pct use selected_n and are extreme missing-answer scenarios.
    """
    table = frame.groupby(group_column, observed=True).agg(
        selected_n=("ResponseId", "size"),
        answered_n=("ai_user", "count"),
        users_n=("ai_user", "sum"),
    )
    table["unknown_n"] = table.selected_n - table.answered_n
    table["answer_pct"] = 100 * table.answered_n / table.selected_n
    denominator = table.answered_n.replace(0, float("nan"))
    table["use_pct"] = 100 * table.users_n / denominator
    # Extreme scenarios for unanswered/contradictory AI-use responses, not confidence intervals.
    table["lower_pct"] = 100 * table.users_n / table.selected_n
    table["upper_pct"] = 100 * (table.users_n + table.unknown_n) / table.selected_n
    return table


def subgroup_comparison(frame):
    """Repeat the same experience comparison under three population restrictions.

    Subgroups overlap and must not be added together. Missing experience remains
    excluded. This is descriptive evidence, not a causal adjustment.
    """
    rows = []
    for name, subset in [
        ("Current selection", frame),
        ("Full-stack developers only", frame.loc[frame.Role.eq("Developer, full-stack")]),
        ("Employed respondents only", frame.loc[frame.Employment.eq("Employed")]),
    ]:
        table = adoption_table(with_career_groups(subset), "career_group")
        row = {"Population": name, "Selected n": len(subset),
               "Known experience n": int(table.selected_n.sum())}
        for group in ["0–5 years", "6+ years"]:
            label = group.replace(" years", "")
            present = group in table.index
            row[f"{label} users n"] = int(table.loc[group, "users_n"]) if present else 0
            row[f"{label} answers n"] = int(table.loc[group, "answered_n"]) if present else 0
            row[f"{label} use (%)"] = float(table.loc[group, "use_pct"]) if present and row[f"{label} answers n"] else float("nan")
        row["Difference (pp)"] = row["6+ use (%)"] - row["0–5 use (%)"]
        rows.append(row)
    return pd.DataFrame(rows)
