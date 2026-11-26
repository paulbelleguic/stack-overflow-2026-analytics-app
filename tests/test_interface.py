import pandas as pd
from pathlib import Path
from streamlit.testing.v1 import AppTest

from src.population import prepare_population, PRIMARY_CODER


def test_all_views_and_filters_coexist_without_real_data(monkeypatch):
    """Synthetic fixtures let CI check the UI without downloading raw data."""
    import src.cache
    import src.ui

    frame = pd.DataFrame({
        "ResponseId": range(30), "Country": "France", "CodeMain": PRIMARY_CODER,
        "WorkExp": 5, "Role": "Developer, back-end", "Employment": "Employed",
        "AISelect": "AI coding assistants or coding agents",
        "AITrust": "I trust it when I can easily verify the output",
        "LearnAI": "Yes, at work", "AICodeAgentHaveWorkedWith": "Tool A;Tool B",
        "AICodeAgentWantToUseNext6Months": "Tool B", "LLMHaveWorkedWith": "Model A",
        "AIWorkCurrentlyUse": "Writing tests", "AIWorkExpectMore": "Writing tests",
        "AIWorkDoNotPlanToUse": "Production deployment", "AIWorkNext": "Run it locally",
        "AISentiment": "Somewhat favorable", "LearnAIHow": "Documentation", "AIAdopt": "Security",
    })
    population = prepare_population(frame)
    monkeypatch.setattr(src.cache, "get_population", lambda: population.copy())
    monkeypatch.setattr(src.ui, "get_schema", lambda: pd.DataFrame(columns=["column", "question", "sub"]))
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / "app.py").run(timeout=30)
    assert not app.exception
    views = list(app.radio[0].options)
    assert len(views) == 6
    for view in views:
        app.radio[0].set_value(view).run(timeout=30)
        assert not app.exception, view
    app.radio[0].set_value("2 · Tools").run(timeout=30)
    app.selectbox[0].set_value("Coding assistants wanted").run(timeout=30)
    app.radio[0].set_value("Main dashboard").run(timeout=30)
    app.radio[0].set_value("2 · Tools").run(timeout=30)
    assert app.selectbox[0].value == "Coding assistants wanted"
    experience = next(widget for widget in app.multiselect if widget.key == "global_experience")
    experience.set_value(["0–2 years"]).run(timeout=30)
    assert not app.exception
    assert any("No respondents match" in warning.value for warning in app.warning)
