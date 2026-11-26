# Five owners, after the common core

The common data, population, logic and main dashboard are reviewed together before anyone starts an individual axis. Member labels are not real accounts or invented contributions.

| Owner | Branch to create | Proposed question | Files the owner will create | Reviewer |
|---|---|---|---|---|
| Member 1 | `axis-1` | How does reported AI use vary by experience and role? | `axes/axis_1/` and `pages/1_Adoption.py` | Member 2 |
| Member 2 | `axis-2` | Which coding assistants have respondents used or want to try? | `axes/axis_2/` and `pages/2_Tools.py` | Member 3 |
| Member 3 | `axis-3` | Which tasks use AI or are expected to use more AI? | `axes/axis_3/` and `pages/3_Tasks.py` | Member 4 |
| Member 4 | `axis-4` | What trust conditions and verification practices are reported? | `axes/axis_4/` and `pages/4_Verification.py` | Member 5 |
| Member 5 | `axis-5` | How do respondents learn AI skills and what matters for adoption? | `axes/axis_5/` and `pages/5_Support.py` | Member 1 |

No owner notebooks, calculations or views are prefilled. Each folder will contain the owner's original exploration, an `analysis.py` without Streamlit, a `view.py` and an `__init__.py`. Each owner must provide their own filters, views, question, defensible comparison, alternative explanation and limits.

## Branch procedure
After the common core is agreed on and available on `main`, each member clones the same repository, updates `main`, then creates their own assigned `axis-N` branch. Start by committing genuine notebook exploration. Develop calculations and the page on that same branch. Push actual progress under the correct account. Completed contributions are reviewed and merged into `main` with merge commits, retaining individual commits. Final integration is followed by checks of all five axes and the dashboard, then optional deployment.

The owner of the initial scaffold does not create or push all five member branches on their behalf. If an owner later needs a change to common files, coordinate it with the group. Common files include `app.py`, `src/`, `views/dashboard.py`, dependencies and architecture documents. Every member must understand the whole app for the defence.

## Honest history
Deleting a file from the current version does not erase it from earlier commits. Initial local drafts and later scope corrections are real work, not five completed individual contributions. Never change dates or authors to simulate participation. The private repository remains unpushed pending the owner's review.
