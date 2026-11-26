"""Définition de la population et variables communes, sans Streamlit."""
import pandas as pd

PRIMARY_CODER = "I create code as a primary part of my job"
EXPERIENCE_LABELS = ["0–2 years", "3–5 years", "6–10 years", "11–20 years", "21–80 years"]
AI_TOOLS = {
    "AI coding assistants or coding agents",
    "General-purpose AI chat tools",
    "AI agents or automated workflows",
    "Internal AI tools built by my company",
}
NO_AI = "I don’t use AI tools"


def ai_status(answer):
    """Une absence ou une réponse contradictoire reste inconnue, jamais 'non'."""
    if pd.isna(answer) or not str(answer).strip():
        return pd.NA
    choices = {choice.strip() for choice in str(answer).split(";")}
    if not choices <= AI_TOOLS | {NO_AI}:
        return pd.NA
    if NO_AI in choices and choices & AI_TOOLS:
        return pd.NA
    return bool(choices & AI_TOOLS)


def prepare_population(responses):
    """France + création de code comme activité principale du travail; toutes industries."""
    frame = responses.loc[
        responses["Country"].eq("France") & responses["CodeMain"].eq(PRIMARY_CODER)
    ].copy()
    frame["survey_year"] = 2026
    years = pd.to_numeric(frame["WorkExp"], errors="coerce")
    # Règle prudente et documentée : les valeurs hors 0–80 ans restent inconnues.
    frame["experience_years"] = years.where(years.between(0, 80))
    frame["experience_group"] = pd.cut(
        frame["experience_years"], [-1, 2, 5, 10, 20, 80], labels=EXPERIENCE_LABELS
    )
    frame["ai_user"] = frame["AISelect"].map(ai_status).astype("boolean")
    return frame.reset_index(drop=True)
