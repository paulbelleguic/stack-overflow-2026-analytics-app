"""Download and read the official 2026 files, without Streamlit."""
from pathlib import Path
import csv
import urllib.error
import urllib.request

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "raw" / "2026"
SOURCE = "https://media.githubusercontent.com/media/StackExchange/Survey/main/packages/archive/2026/"
FILES = {"survey_results_public.csv": "ResponseId", "survey_results_schema.csv": "column"}


def ensure_data(data_dir=DATA_DIR):
    """Download absent files; reject empty files or a Git LFS pointer."""
    data_dir = Path(data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    for name, required_column in FILES.items():
        target = data_dir / name
        if target.exists() and target.stat().st_size > 0:
            continue
        temporary = data_dir / (name + ".part")
        try:
            urllib.request.urlretrieve(SOURCE + name, temporary)
            with temporary.open(encoding="utf-8-sig", newline="") as stream:
                header = next(csv.reader(stream), [])
            if required_column not in header:
                raise ValueError(f"{name} is not the expected CSV. Use the official Git LFS media URL.")
            temporary.replace(target)
        except (OSError, urllib.error.URLError, ValueError) as error:
            temporary.unlink(missing_ok=True)
            raise RuntimeError(f"Could not download {name}: {error}") from error
    return data_dir


def load_responses(path=DATA_DIR / "survey_results_public.csv"):
    frame = pd.read_csv(path, low_memory=False)
    if "ResponseId" not in frame or frame["ResponseId"].isna().any() or not frame["ResponseId"].is_unique:
        raise ValueError("Expected one unique, non-missing ResponseId per 2026 response.")
    return frame


def load_schema(path=DATA_DIR / "survey_results_schema.csv"):
    frame = pd.read_csv(path)
    if not {"column", "question"}.issubset(frame.columns):
        raise ValueError("The schema does not contain the expected question fields.")
    return frame
