# Stack Overflow 2026 Analytics App

## Shared core — before individual axis development

**Educational sponsor:** a DINUM project team planning a pilot of AI coding assistants.

**Business question:** which uses, tools, verification practices and training needs should be prioritised for an initial pilot?

This version contains the common data loading, population, shared logic, filters, a shared audit notebook and the main dashboard. The five individual axes are deliberately not implemented. The group must review the core together before each owner starts their branch.

## Run from a fresh clone in WSL

On Windows, use **Ubuntu in WSL**, not Docker Desktop's WSL distribution. Open Ubuntu, or run `wsl -d Ubuntu` from PowerShell. Keep the project under the Linux home directory and recreate the environment there; do not copy a Windows `.venv`.

Prerequisites inside Ubuntu: Git and [uv](https://docs.astral.sh/uv/getting-started/installation/). Once the repository has been published and access granted:

```bash
mkdir -p ~/projects
cd ~/projects
git clone https://github.com/paulbelleguic/stack-overflow-2026-analytics-app.git
cd stack-overflow-2026-analytics-app
uv sync --locked
uv run python scripts/download_data.py
uv run streamlit run app.py
```

Open `http://localhost:8501` in the Windows browser. Stop the app with Ctrl+C. `code .` from Ubuntu opens the project in VS Code with the WSL extension. The Python version is 3.12; uv can install it if necessary.

The downloader uses the official Git LFS media URLs, not raw pointers. It downloads absent CSVs into ignored `data/raw/2026/`, reports errors, and checks expected CSV headers. No SHA-256 verification, automated test suite or GitHub Actions workflow is included. About 123 MB is needed for the data, plus the environment. The app uses the same downloader if the files are missing at startup.

## Current files

| File | Responsibility |
|---|---|
| `app.py` | Common dashboard entry point |
| `src/data.py` | Download and read the CSV files |
| `src/population.py` | Define the common population and derived fields |
| `src/filters.py` | Filter a population without Streamlit |
| `src/analysis/common.py` | Shared frequencies and known-answer rates |
| `src/cache.py` | Cache the prepared public data and schema |
| `src/ui.py` | Common filter controls, charts, population captions and question notes |
| `views/dashboard.py` | Main dashboard message and interface |
| `notebooks/00_shared_audit.ipynb` | Shared exploration of scope and response coverage |
| `axes/`, `pages/` | Entry locations for future member contributions; no individual implementations yet |

## Population and care with interpretation

2026 respondents in France who selected `I create code as a primary part of my job`: **628 eligible respondents**, from 794 in France and 30,903 overall. They are volunteers across industries, not a sample of DINUM staff or a representative estimate of the French developer workforce.

Question-specific rates use the people who answered that field; missing values stay unknown. Multiple selections count each person once per choice, so percentages can add to more than 100%. The dashboard's provisional direction is to examine verification alongside access to tools. It is not a demonstrated effect of a policy or proof of tool quality.

## Shared exploration and manual checking

```bash
uv run python scripts/audit_data.py
uv sync --locked --group exploration
uv run jupyter lab
```

Check the selected count, answer counts, empty filters and captions in the app. Notebooks locate the root from either the project folder or `notebooks/`.

## Group progression

1. Review the data, framing, mockup and architecture together on the common core.
2. Agree on the five owners and finish the common core on `main`.
3. Each owner creates **their own** `axis-1` to `axis-5` branch from up-to-date `main`.
4. On that branch: explore in a notebook, formulate and examine a hypothesis, then build calculations and the axis page with its own controls.
5. Review and merge the completed contributions into `main`, preserving their actual commits.
6. Check the combined app, reproduce setup, explain choices and capture the two required screenshots.
7. Online deployment is an optional bonus, not a prerequisite to local development.

## Documentation

- [Framing and proposed axes](docs/FRAMING.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Data coverage](docs/DATA_AUDIT.md)
- [Sources and denominators](docs/DATA_METHOD.md)
- [Ownership and integration](docs/TEAM_PLAN.md)
- [2025 comparison policy](docs/HARMONISATION.md)
- [Real local progress](docs/PROGRESS.md)
- [Validation status](docs/VALIDATION.md)
- [Submission checklist](docs/SUBMISSION.md)
- [Dashboard and navigation mockup](docs/MOCKUP.md)

Private French group instructions are kept outside the repository.

## Source

[Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026), [official archive](https://github.com/StackExchange/Survey/tree/main/packages/archive/2026), data under ODbL 1.0 and contents under DbCL 1.0. The [archived question bank](https://github.com/StackExchange/Survey/tree/releases/2026/questions) documents wording, options and routing. The 2026 questionnaire archive is interactive. No 2025 comparison is enabled and no affiliation with DINUM or Stack Overflow is claimed.
