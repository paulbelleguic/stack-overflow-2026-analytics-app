import streamlit as st

from src.analysis import axis_2
from src.ui import axis_intro, local_population, draw_frequency, question_note


def render(frame):
    axis_intro("Axis 2 · Tools", "Which coding assistants have respondents used, and which do they want to try?")
    selected, scope = local_population(frame, "axis_2")
    fields = {"Coding assistants used": "AICodeAgentHaveWorkedWith", "Coding assistants wanted": "AICodeAgentWantToUseNext6Months", "Language models used": "LLMHaveWorkedWith"}
    choice = st.selectbox("Tool view", list(fields), key="axis_2_view", persist_state="session")
    column = fields[choice]
    table, answered_n = axis_2.summarise(selected, column)
    draw_frequency(selected, table, answered_n, choice, scope)
    question_note(column, multiple=True)
    st.caption("Reported popularity is not evidence that a product is better. Used and wanted columns have different answer denominators.")
