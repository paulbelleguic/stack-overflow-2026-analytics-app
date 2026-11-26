import streamlit as st

st.set_page_config(page_title="Stack Overflow 2026 Analytics App", layout="wide")

from src.ui import common_population
from views.dashboard import render

st.title("Stack Overflow 2026 Analytics App")
st.caption("AI coding-assistant pilot for a DINUM project team · shared core · 2026 data only")

population = common_population()
render(population)

st.divider()
st.caption("Voluntary survey responses are not representative of all French developers or public-sector staff. Associations are not causal effects. Source: Stack Overflow Developer Survey 2026; ODbL 1.0.")
