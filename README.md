# Stack Overflow 2026 Analytics App

One shared Streamlit app, one common core and five complementary investigations.

**Educational sponsor:** a DINUM project team planning a pilot of AI coding assistants.

**Business question:** which uses, tools, verification practices and training needs should be prioritised for an initial pilot?

The starter is functional, but the individual investigations are **not finished**. Each owner must deepen their axis, assess alternative explanations and contribute their own documented work. The initial dashboard direction is provisional.

## Run from a fresh clone

Prerequisites: Git and [uv](https://docs.astral.sh/uv/getting-started/installation/). The project uses Python 3.12; uv can obtain it when needed. In PowerShell:

```powershell
git clone https://github.com/paulbelleguic/stack-overflow-2026-analytics-app.git
cd stack-overflow-2026-analytics-app
uv sync --locked
uv run python scripts/download_data.py
uv run streamlit run app.py
```

Open `http://localhost:8501`. Stop the server with Ctrl+C. If the data is missing at app startup, the same downloader is called automatically; the explicit command makes initial setup easier to diagnose. A private repository requires access from the owner before cloning.

No raw data is committed. Downloading the two verified 2026 files needs internet access and approximately 123 MB of disk space, in addition to the environment. Subsequent runs can use the verified local files offline.

## What is included

- A main dashboard with a provisional message about including verification in a pilot.
- Five connected starting views: adoption and profiles, tools, assisted tasks, trust and verification, training and support.
- Shared role and experience filters, plus independent controls on each axis.
- Pure calculation modules separate from the Streamlit interface.
- Cached shared loading and session-persistent choices.
- One shared audit notebook and five owner notebooks, with starting calculations and explicit work still to do.
- A source manifest, integrity checks, tests and CI.

## Population and interpretation

2026 respondents in France who selected `I create code as a primary part of my job`: **628 eligible responses** before interactive filters, out of 794 French responses and 30,903 overall. These are volunteers across industries, **not a sample of DINUM staff** or a representative estimate of the French developer workforce.

Each figure shows the selected population and the number answering its field. Missing answers stay unknown. Multiple-choice shares count each respondent once per option and may sum above 100%. The denominator for a workflow column is the set naming at least one task in that column. Statements of use, trust or learning do not measure actual effectiveness.

## Checks and notebooks

```powershell
uv run pytest -q
uv run python scripts/audit_data.py
uv sync --locked --group exploration
uv run jupyter lab
```

Notebooks locate the project from either the root or `notebooks/`. The optional exploration group is not needed to run the app. CI uses synthetic data and never downloads or commits respondents' records.

## Project documentation

- [Framing and five questions](docs/FRAMING.md)
- [Technical architecture and data flow](docs/ARCHITECTURE.md)
- [Data audit and verified coverage](docs/DATA_AUDIT.md)
- [Rules, sources and denominators](docs/DATA_METHOD.md)
- [Team ownership and remaining work](docs/TEAM_PLAN.md)
- [2025 comparison policy](docs/HARMONISATION.md)
- [Bootstrap progress](docs/PROGRESS.md)
- [Submission and defence checklist](docs/SUBMISSION.md)

The private French onboarding instructions are distributed separately and are not part of this repository.

## Source and attribution

[Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026), [official archive](https://github.com/StackExchange/Survey/tree/main/packages/archive/2026), data under ODbL 1.0 and contents under DbCL 1.0. CSV integrity is checked against the official Git LFS SHA-256 values recorded in `config/sources.json`.

The [archived 2026 question bank](https://github.com/StackExchange/Survey/tree/releases/2026/questions) documents answer options and branching. Unlike the 2025 edition, the 2026 questionnaire archive is interactive, not a PDF. This project is not affiliated with Stack Overflow or DINUM.
