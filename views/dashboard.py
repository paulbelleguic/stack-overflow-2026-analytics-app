import streamlit as st

from src.analysis.common import frequency_table, known_rate
from src.ui import draw_frequency, question_note


def render(frame):
    st.header("Make verification part of the AI pilot")
    st.write("Sponsor: a DINUM project team planning a pilot of AI coding assistants. This is an exploratory French-market benchmark, not a study of public-sector staff.")
    adoption, answers = known_rate(frame, "ai_user")
    trust, trust_n = frequency_table(frame, "AITrust")
    learning, learning_n = frequency_table(frame, "LearnAI")
    left, middle, right = st.columns(3)
    left.metric("Selected French respondents", f"{len(frame):,}")
    middle.metric("Reported current AI use", f"{adoption:.1%}" if adoption is not None else "Not available")
    middle.caption(f"Denominator: {answers:,} valid AI-use answers; {len(frame) - answers:,} unknown.")
    if trust_n:
        verify = int(frame["AITrust"].eq("I trust it when I can easily verify the output").sum())
        right.metric("Trust when output is verifiable", f"{verify / trust_n:.1%}")
    else:
        right.metric("Trust when output is verifiable", "Not available")
    right.caption(f"Denominator: {trust_n:,} trust answers; {len(frame) - trust_n:,} unanswered.")
    if not trust.empty:
        st.info(f"Most frequent trust response: “{trust.iloc[0]['answer']}” ({trust.iloc[0]['share_pct']:.1f}% of {trust_n:,} answers). Provisional direction: pilot a verification step alongside tool access, then validate it with the five axes and the sponsor.")
    st.caption("Usage and trust metrics have different answering populations. They are not a paired comparison or a causal effect.")
    draw_frequency(frame, trust, trust_n, "Trust is conditional on the task and the checks", "Common dashboard", top_n=6)
    question_note("AITrust")
    draw_frequency(frame, learning, learning_n, "Reported AI learning in the past year", "Common dashboard", top_n=5)
    question_note("LearnAI")
