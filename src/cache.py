"""The only Streamlit-specific data-loading boundary."""
import streamlit as st

from src.data import ensure_data, load_responses, load_schema
from src.population import prepare_population


@st.cache_data(show_spinner="Loading and preparing verified 2026 data…")
def get_population():
    ensure_data()
    return prepare_population(load_responses())


@st.cache_data
def get_schema():
    return load_schema()
