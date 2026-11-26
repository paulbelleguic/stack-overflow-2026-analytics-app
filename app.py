import streamlit as st

st.set_page_config(page_title="Stack Overflow 2026 Analytics App", layout="wide")

from src.cache import get_population
from src.filters import filter_population
from src.population import EXPERIENCE_LABELS
from views import dashboard, axis_1, axis_2, axis_3, axis_4, axis_5

st.title("Stack Overflow 2026 Analytics App")
st.caption("An exploratory AI coding-assistant pilot for a DINUM project team · 2026 data only")

try:
    base = get_population()
except (OSError, ValueError, RuntimeError) as error:
    st.error(str(error))
    st.info("Check your internet connection and run: uv run python scripts/download_data.py")
    st.stop()

pages = {
    "Main dashboard": dashboard,
    "1 · Adoption and profiles": axis_1,
    "2 · Tools": axis_2,
    "3 · Assisted tasks": axis_3,
    "4 · Trust and verification": axis_4,
    "5 · Training and support": axis_5,
}
with st.sidebar:
    st.header("Explore")
    selected_page = st.radio("View", list(pages), key="navigation", persist_state="session")
    st.subheader("Common filters")
    roles = st.multiselect("Role (empty = all)", sorted(base["Role"].dropna().unique().tolist()), key="global_roles", persist_state="session")
    experiences = st.multiselect("Experience (empty = all)", EXPERIENCE_LABELS, key="global_experience", persist_state="session")
    st.caption("Population: France; coding as the primary part of the job. An empty filter includes unanswered values.")

selected = filter_population(base, roles, experiences)
st.sidebar.caption(f"Selected: {len(selected):,} / {len(base):,} eligible respondents.")
if selected.empty:
    st.warning("No respondents match these filters. Clear a filter to continue.")
    st.stop()
pages[selected_page].render(selected)
st.divider()
st.caption("Voluntary survey responses are not representative of all French developers or public-sector staff. Associations are not causal effects. Source: Stack Overflow Developer Survey 2026; ODbL 1.0.")
