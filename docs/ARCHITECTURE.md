# Technical architecture — common core

## Data flow

```text
Official 2026 response CSV and schema
    -> src/data.py: ensure_data, load_responses, load_schema
    -> src/population.py: prepare_population
    -> src/cache.py: cached public population and schema
    -> src/ui.py: common_population and common controls
    -> src/filters.py: filtered population
    -> src/analysis/common.py: rates and frequency tables
    -> views/dashboard.py and src/ui.py: main message, charts and captions
```

`app.py` runs the common dashboard. The analysis and filtering functions have no Streamlit dependency. UI controls, chart display and cache decorators are separate from those calculations.

## Features and functions

| Feature | Location |
|---|---|
| Download absent data, explicit errors and header checks | `src/data.py: ensure_data`; `scripts/download_data.py` |
| One row per respondent and source reading | `src/data.py: load_responses`, `load_schema` |
| France and coding as a primary job | `src/population.py: prepare_population` |
| AI-use and experience variables | `src/population.py: ai_status`, `prepare_population` |
| Shared filters | `src/filters.py: filter_population`; `src/ui.py: common_population` |
| Shared frequencies and rates | `src/analysis/common.py: frequency_table`, `known_rate` |
| Main dashboard | `views/dashboard.py: render` |
| Figure population and question | `src/ui.py: population_caption`, `draw_frequency`, `question_note` |
| Source coverage | `scripts/audit_data.py`; `notebooks/00_shared_audit.ipynb` |

## Cache

`@st.cache_data` caches the prepared public-data population and source schema. The expensive reading and initial preparation happen once per cache entry. Callers receive copies. Filtering and small summaries are recomputed and are not separately cached. No private session choices or resources such as connections are cached.

After changing preparation code or replacing the CSV, use Clear cache in the app menu or restart the server. A cached wrapper does not necessarily notice changes in imported helpers.

## Session state

The common controls use `global_roles` and `global_experience` as widget keys with `persist_state="session"`, available in pinned Streamlit 1.67.0. These choices are per browser session. Empty selections mean all eligible values, including unknowns. Selecting experience groups excludes unknown experience, and the new count is shown.

The future axis pages must use their own keys such as `axis_1_role` so choices cannot overwrite one another. They must reuse `common_population()` rather than read a second copy of the data. Raw responses are not manually stored in session state.

## Future axes — not preimplemented

Each owner creates `axes/axis_N/` with their exploration notebook, pure calculation module and `render(population)` view. A small, uniquely named entry in `pages/` calls the common population helper and that owner's render function. Native Streamlit pages provide navigation without merging five separate applications or editing a shared page registry for every axis.

All owners branch from the reviewed common `main`, work on their own files, then merge completed contributions back into `main`. The combined app must be checked before deployment. Each future figure must include the year, scope, filters, selected count and actual answer denominator.

## Deliberate limits

No individual axis calculations or charts, automated tests, GitHub Actions workflow, SHA-256 verification or deployment are included in this shared-core version. 2025 remains disabled until an explicit harmonisation is reviewed. Manual checking and explaining all retained code remain required.
