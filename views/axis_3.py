import streamlit as st

from src.analysis import axis_3
from src.ui import axis_intro, local_population, draw_frequency, question_note


def render(frame):
    axis_intro("Axis 3 · Assisted tasks", "For which tasks is AI used, expected to expand, or not planned?")
    selected, scope = local_population(frame, "axis_3")
    fields = {"Current AI-assisted tasks": "AIWorkCurrentlyUse", "Tasks expecting more AI": "AIWorkExpectMore", "Tasks with no planned AI use": "AIWorkDoNotPlanToUse"}
    choice = st.selectbox("Workflow view", list(fields), key="axis_3_view", persist_state="session")
    column = fields[choice]
    table, answered_n = axis_3.summarise(selected, column)
    draw_frequency(selected, table, answered_n, choice, scope)
    question_note(column, multiple=True)
    st.caption("A blank current-use column does not prove non-use on every task. Each view includes people naming at least one task in that column.")
