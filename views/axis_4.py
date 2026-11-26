import streamlit as st

from src.analysis import axis_4
from src.ui import axis_intro, local_population, draw_frequency, question_note


def render(frame):
    axis_intro("Axis 4 · Trust and verification", "What conditions of trust and verification practices are reported?")
    selected, scope = local_population(frame, "axis_4")
    fields = {"Conditions of trust": "AITrust", "Steps before using an AI answer": "AIWorkNext", "Attitude towards AI": "AISentiment"}
    choice = st.selectbox("Verification view", list(fields), key="axis_4_view", persist_state="session")
    column = fields[choice]
    table, answered_n = axis_4.summarise(selected, column)
    draw_frequency(selected, table, answered_n, choice, scope)
    question_note(column, multiple=(column == "AIWorkNext"))
    st.caption("Trust and stated checks are self-reports, not observed measures of model accuracy or safe behaviour.")
