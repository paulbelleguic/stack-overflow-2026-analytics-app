# Native Streamlit page entries

There are no individual pages yet. The common app currently contains only the dashboard.

Each axis owner adds their own uniquely named Python page on their branch. Streamlit will list those files in the sidebar when running `uv run streamlit run app.py`.

A page should set its page configuration, obtain the common population from `src.ui.common_population`, and call its own `axes.axis_N.view.render(population)`. This keeps one data-loading system and one common application. Create the axis implementation before importing it from a page.
