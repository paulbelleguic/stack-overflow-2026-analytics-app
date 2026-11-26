# Individual axes — not implemented in the common core

Each owner starts from the agreed `main`, creates their own `axis-N` branch, and creates their own notebook, calculations and view. No axis analysis or chart is prefilled here.

Suggested files per owner:

```text
axes/axis_N/__init__.py
axes/axis_N/exploration.ipynb
axes/axis_N/analysis.py
axes/axis_N/view.py
pages/N_Axis_name.py
```

`analysis.py` must not import Streamlit. `view.py` can expose `render(population)` and add the axis's own filters, views and captions. The thin page entry obtains the common filtered population and calls that render function. Streamlit discovers page entry files in `pages/`; the owner can run the same `app.py` locally on their branch without changing the common dashboard.

Keep calculations, source questions, denominators and actual findings in the owner's work. The group combines completed branches into `main`, checks all five pages together, then considers deployment.
