import streamlit as st

from src.analysis import axis_5
from src.ui import axis_intro, local_population, draw_frequency, question_note


def render(frame):
    axis_intro("Axis 5 · Training and support", "How do respondents learn AI skills, and what matters for adoption?")
    selected, scope = local_population(frame, "axis_5")
    fields = {"AI learning in the past year": "LearnAI", "Ways of learning AI": "LearnAIHow", "Factors in adopting AI": "AIAdopt"}
    choice = st.selectbox("Support view", list(fields), key="axis_5_view", persist_state="session")
    column = fields[choice]
    table, answered_n = axis_5.summarise(selected, column)
    draw_frequency(selected, table, answered_n, choice, scope)
    question_note(column, multiple=(column != "LearnAI"))
    st.caption("Learning activity and adoption preferences do not measure actual training effectiveness. AIAdopt permits up to three selections.")
