import streamlit as st

from src.analysis import axis_1
from src.ui import axis_intro, local_population, draw_adoption, question_note


def render(frame):
    axis_intro("Axis 1 · Adoption and profiles", "How does reported AI use vary by experience and role?")
    selected, scope = local_population(frame, "axis_1")
    choice = st.selectbox("Compare profiles by", ["Experience", "Role"], key="axis_1_view", persist_state="session")
    column = {"Experience": "experience_group", "Role": "Role"}[choice]
    table, answered_n = axis_1.summarise(selected, column)
    draw_adoption(selected, table, answered_n, scope)
    question_note("AISelect", multiple=True)
