# Shared-core validation in Ubuntu WSL

Checked on 26 November 2026. The current version contains the common core only; individual axes are not implemented.

## Checks completed
- Cloned the current common core into `/home/paul/projects/stack-overflow-2026-analytics-app`, rather than reusing a Windows environment.
- Ran `uv sync --locked` in Ubuntu, creating a fresh Linux `.venv` with Python 3.12.14 and the pinned app dependencies.
- Downloaded the official 2026 CSVs using the simplified downloader and ran the source audit in Ubuntu.
- Confirmed 30,903 source responses, 794 in France and 628 eligible primary-job coders in France. The derived AI-use indicator has 507 known answers; missing and contradictory answers remain unknown.
- Started the app with the Linux interpreter and confirmed its health endpoint and actual dashboard in the browser.
- Manually selected the back-end developer role: the dashboard changed from 628 to 82 respondents and showed the question-specific answer denominators. Clearing the filter restored the full population.
- Confirmed that only `main` exists in the working clone, there are no individual Python pages, and no test suite or GitHub Actions workflow remains in the current source.
- Installed the official VS Code WSL extension and opened the Linux project. Use Ubuntu WSL for ongoing development.

## Still to do
- Review and agree on the common core together; assign the five real owners.
- Obtain approval for the first GitHub push and invite the members and trainer. A remote GitHub clone cannot yet be verified because no source has been pushed.
- Each owner creates their own branch from up-to-date main, then their own notebook, calculations, controls and page.
- Integrate the finished branches, check the combined six-page app and create the final screenshots.
- Re-run any newly created notebooks and the shared audit in the group's chosen notebook environment as the analysis evolves. The retained shared notebook was executed before the WSL migration; its data-loading functions and population have since been checked directly in Ubuntu.
- Optional online deployment is not yet done.

Earlier local drafts remain in Git history. Removing their current files does not erase old commits. No dates or authors have been rewritten, and no earlier scaffold is presented as a member's individual contribution.
