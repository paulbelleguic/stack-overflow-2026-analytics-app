# Local validation at handoff

Checked on 26 November 2026, using Windows and the project's Python 3.12 environment.

## Passed
- Official 2026 responses and schema downloaded and verified against the recorded Git LFS sizes and SHA-256 hashes.
- Raw response IDs are unique; the shared population contains 628 French primary-job coders.
- Coverage for every starter field recorded in `DATA_AUDIT.md`.
- Seven automated checks pass: nullable AI-use classification, contradictory answers, multiple-choice de-duplication and denominators, small groups, scope and experience handling, empty answers, all six views, persistent local choices and an empty-filter result.
- All six starter notebooks execute using the project's environment, from the `notebooks/` directory. Their displayed outputs are aggregate tables and plots, not individual records.
- The live dashboard and trust/verification axis load in the browser, with the 628 eligible population and actual question-specific denominators.
- A **fresh local Git clone** was created without data or an environment. `uv sync --locked`, the official downloader, the audit script and `uv run pytest -q` all succeed there. Seven checks pass again.
- `git ls-files data .venv` is empty. French onboarding material is outside this repository.

## Not yet checked or completed
- The owner requested a review **before any GitHub push**. Remote cloning and GitHub-hosted CI cannot yet be checked: the remote repository is still empty.
- Tests have not yet run on Linux or another member's computer.
- No online deployment or public bonus URL exists.
- Real group account invitations and trainer access require their GitHub handles.
- The owners' individual investigations, hypotheses, robustness checks, final conclusions and peer reviews remain to be completed.
- The final two submission screenshots must be captured after integration. The narrow local review tab is not a substitute for those final captures.

The scaffold's readiness and these checks must not be presented as evidence that the whole assessed project is finished.
