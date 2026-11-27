"""Axis 3: tasks done with AI. Calculations only, without Streamlit."""
import pandas as pd

STATUS_COLUMNS = {
    "AIWorkCurrentlyUse": "Currently use AI",
    "AIWorkExpectMore": "Expect to use AI more",
    "AIWorkExpectLess": "Expect to use AI less",
    "AIWorkDoNotPlanToUse": "Do not use and do not plan to",
    "AIWorkNotInWorkflow": "Not part of my workflow",
}
STATUSES = list(STATUS_COLUMNS.values())
CURRENT = "Currently use AI"

CODING_TASKS = [
    "Generating code in a familiar area",
    "Debugging, troubleshooting, or refactoring code",
    "Writing or improving tests",
]
OPERATIONS_TASKS = [
    "Deploying, operating, or troubleshooting production systems",
    "Creating or configuring development/test environments",
    "Writing tickets, requirements, plans, or project updates",
    "Writing emails, messages, summaries, or other communication",
]

EXPERIENCE_BANDS = ["0–10 years", "11 years or more"]


def task_answers(frame):
    """One row per respondent, task and status."""
    parts = []
    for column, status in STATUS_COLUMNS.items():
        answers = frame[["ResponseId", column]].dropna()
        answers = answers.assign(task=answers[column].str.split(";")).explode("task")
        answers["task"] = answers["task"].str.strip()
        answers["status"] = status
        parts.append(answers[["ResponseId", "task", "status"]])
    result = pd.concat(parts, ignore_index=True)
    return result.loc[result["task"].ne("")].drop_duplicates()


def matrix_respondents(frame):
    """Number of respondents who rated at least one task."""
    return task_answers(frame)["ResponseId"].nunique()


def task_summary(frame):
    """For each task: respondents who rated it, then the count and share of each status.

    The denominator of a task is the number of respondents who gave it at least one status.
    A respondent can select two statuses for the same task, so shares can add up to more than 100%.
    """
    answers = task_answers(frame)
    if answers.empty:
        return pd.DataFrame(columns=["task", "rated"] + STATUSES + [status + " (%)" for status in STATUSES])
    rated = answers.groupby("task")["ResponseId"].nunique().rename("rated")
    counts = answers.groupby(["task", "status"])["ResponseId"].nunique().unstack(fill_value=0)
    counts = counts.reindex(columns=STATUSES, fill_value=0)
    shares = counts.div(rated, axis=0) * 100
    shares.columns = [status + " (%)" for status in STATUSES]
    summary = pd.concat([rated, counts, shares], axis=1).reset_index()
    return summary.sort_values(CURRENT + " (%)", ascending=False).reset_index(drop=True)


def status_ranking(frame, status=CURRENT):
    """Tasks ranked by one status, in the format used by src.ui.draw_frequency."""
    summary = task_summary(frame)
    table = pd.DataFrame({
        "answer": summary["task"],
        "respondents": summary[status],
        "rated": summary["rated"],
        "share_pct": summary[status + " (%)"],
    })
    return table.sort_values("share_pct", ascending=False).reset_index(drop=True)


def task_profile(frame, task):
    """All statuses for one task, in the format used by src.ui.draw_frequency."""
    summary = task_summary(frame)
    row = summary.loc[summary["task"].eq(task)]
    if row.empty:
        return pd.DataFrame(columns=["answer", "respondents", "share_pct"]), 0
    row = row.iloc[0]
    table = pd.DataFrame({
        "answer": STATUSES,
        "respondents": [int(row[status]) for status in STATUSES],
        "share_pct": [float(row[status + " (%)"]) for status in STATUSES],
    })
    return table.sort_values("share_pct", ascending=False).reset_index(drop=True), int(row["rated"])


def experience_band(frame):
    """Two experience bands, large enough to compare. Unknown experience stays missing."""
    return pd.cut(frame["experience_years"], [-1, 10, 80], labels=EXPERIENCE_BANDS)


def compare_groups(frame, groups, status=CURRENT):
    """Share of one status per task, for each group. Returns shares and group sizes."""
    shares = {}
    sizes = {}
    for name, part in frame.groupby(groups, observed=True):
        summary = task_summary(part)
        if summary.empty:
            continue
        shares[name] = summary.set_index("task")[status + " (%)"]
        sizes[name] = matrix_respondents(part)
    return pd.DataFrame(shares), sizes


def coding_vs_operations(frame, status=CURRENT):
    """Average share of one status for core coding tasks and for operations or communication tasks."""
    summary = task_summary(frame).set_index("task")
    column = status + " (%)"
    coding = summary[column].reindex(CODING_TASKS).mean()
    operations = summary[column].reindex(OPERATIONS_TASKS).mean()
    return {"coding_pct": coding, "operations_pct": operations, "gap_points": coding - operations}
