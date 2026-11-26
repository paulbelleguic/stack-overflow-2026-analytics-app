"""Shared presentation helpers; calculation functions live elsewhere."""
import html
import textwrap

import matplotlib.pyplot as plt
import streamlit as st

from src.cache import get_schema, get_population
from src.filters import filter_population
from src.population import EXPERIENCE_LABELS

ACCENT = "#226B80"
GREY = "#C7CDD0"
MINIMUM_ANSWERS = 20


def scope_text():
    roles = st.session_state.get("global_roles", [])
    experience = st.session_state.get("global_experience", [])
    return (
        "2026 · France · coding as the primary part of the job · "
        f"Roles: {', '.join(roles) if roles else 'all, including unanswered'} · "
        f"Experience: {', '.join(experience) if experience else 'all, including unknown'}"
    )


def population_caption(frame, answered_n, scope, extra=""):
    return (
        f"{scope_text()} · {scope} · Selected respondents: n={len(frame):,}; "
        f"respondents used as the answer denominator: n={answered_n:,}. {extra} "
        "Source: Stack Overflow Developer Survey 2026 (ODbL 1.0)."
    )


def question_note(column, multiple=False):
    schema = get_schema()
    row = schema.loc[schema["column"].eq(column)]
    with st.expander("Question and denominator"):
        if len(row):
            st.write(html.unescape(str(row.iloc[0]["question"])))
            if row.iloc[0]["sub"] == row.iloc[0]["sub"]:
                st.write("Part of the question: " + str(row.iloc[0]["sub"]))
        st.write("The denominator includes selected respondents with a non-empty answer to this specific field. Missing answers are not counted as 'no'.")
        if multiple:
            st.write("Multiple selections are split at semicolons. Each choice is counted once per respondent; percentages can sum to more than 100%. For workflow matrices, each column has its own denominator.")


def draw_frequency(frame, table, answered_n, title, scope, top_n=10):
    caption = population_caption(frame, answered_n, scope, f"Showing up to {top_n} answer categories.")
    if answered_n < MINIMUM_ANSWERS:
        st.warning(f"Not enough answers for this chart: {answered_n}; at least {MINIMUM_ANSWERS} are required.")
        st.caption(caption)
        return
    shown = table.head(top_n).iloc[::-1]
    labels = [textwrap.fill(str(value), 44) for value in shown["answer"]]
    fig, ax = plt.subplots(figsize=(9, max(3.4, len(shown) * .65 + 1)))
    colours = [GREY] * len(shown)
    if colours:
        colours[-1] = ACCENT
    bars = ax.barh(labels, shown["share_pct"].astype(float), color=colours)
    ax.bar_label(bars, labels=[f"{share:.1f}% (n={int(n):,})" for share, n in zip(shown["share_pct"], shown["respondents"])], padding=4, fontsize=9)
    ax.set(xlim=(0, 120), xlabel="Share of respondents answering this field (%)", title=title)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="x", alpha=.15)
    ax.set_axisbelow(True)
    # The population travels with the figure, including when downloaded as an image.
    fig.text(.02, .01, textwrap.fill(caption, 130), fontsize=8, va="bottom")
    fig.tight_layout(rect=(0, .17, 1, 1))
    st.pyplot(fig)
    plt.close(fig)
    st.caption(caption)
    with st.expander("View the underlying summary table"):
        st.dataframe(table, hide_index=True, width="stretch")



def common_population():
    """The same loading and common filters for the dashboard and future pages."""
    try:
        base = get_population()
    except (OSError, ValueError, RuntimeError) as error:
        st.error(str(error))
        st.info("Run: uv run python scripts/download_data.py")
        st.stop()
    with st.sidebar:
        st.header("Common filters")
        roles = st.multiselect("Role (empty = all)", sorted(base["Role"].dropna().unique().tolist()),
                              key="global_roles", persist_state="session")
        experiences = st.multiselect("Experience (empty = all)", EXPERIENCE_LABELS,
                                    key="global_experience", persist_state="session")
        st.caption("2026 · France · coding as the primary part of the job. Empty selections include unanswered values.")
    selected = filter_population(base, roles=roles, experiences=experiences)
    st.sidebar.caption(f"Selected: {len(selected):,} / {len(base):,} eligible respondents.")
    if selected.empty:
        st.warning("No respondents match these filters. Clear a filter to continue.")
        st.stop()
    return selected
