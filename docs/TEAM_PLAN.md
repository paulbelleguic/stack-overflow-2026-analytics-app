# Ownership and genuine remaining work

| Owner | Branch | Usual files | Deliverables still required | Shared dependencies | Reviewer |
|---|---|---|---|---|---|
| Member 1 | `axis-1` | `notebooks/01_adoption_profiles.ipynb`, `src/analysis/axis_1.py`, `views/axis_1.py` | Explore profile differences; choose and justify a comparison and a subgroup check; explain uncertainty and small groups | Population, AI indicator, experience groups, captions | Member 2 |
| Member 2 | `axis-2` | `notebooks/02_tools.ipynb`, `src/analysis/axis_2.py`, `views/axis_2.py` | Explore tool combinations; separate used/wanted denominators; justify a tool-focused view without claiming product quality | Multiple-choice helper, population, captions | Member 3 |
| Member 3 | `axis-3` | `notebooks/03_tasks.ipynb`, `src/analysis/axis_3.py`, `views/axis_3.py` | Inspect workflow routing; compare task views defensibly; identify a pilot-task proposal and an alternative explanation | Matrix-column denominators, filters, captions | Member 4 |
| Member 4 | `axis-4` | `notebooks/04_verification.ipynb`, `src/analysis/axis_4.py`, `views/axis_4.py` | Deepen trust and checks; test an association within a clear population; separate stated trust from accuracy | Missing-value and multiselect rules, captions | Member 5 |
| Member 5 | `axis-5` | `notebooks/05_training_support.ipynb`, `src/analysis/axis_5.py`, `views/axis_5.py` | Investigate learning/adoption needs; propose an evidence-based support action; assess conditional answering populations | Shared filters, learning-field denominators, captions | Member 1 |

Names and GitHub handles must replace these owner labels once the group agrees on the assignment. No contributions or reviews are attributed to the placeholders.

## The common core belongs to everyone

Shared files are `app.py`, `src/data.py`, `src/population.py`, `src/filters.py`, `src/cache.py`, `src/ui.py`, `src/analysis/common.py`, `views/dashboard.py`, `config/`, the lock file, shared tests and architecture documents. Coordinate changes to these files before editing. Each member should understand and make a real, useful improvement or review of the core; a label in a table is not a contribution.

## Starter status

The six views coexist and calculate initial summaries. The five notebooks contain a basic exploration and a work plan, **not five completed independent investigations**. Final hypotheses, robustness checks, defensible conclusions and sponsor recommendations remain with the owners. Main-dashboard wording and screenshots must be reviewed after integration.

Use reviewed pull requests and merge commits to preserve actual authorship. Do not fabricate commits, dates, reviews or group participation. The first bootstrap commits can legitimately be close together; subsequent history should reflect actual ongoing work.
