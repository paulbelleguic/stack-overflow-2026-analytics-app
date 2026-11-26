"""Téléchargement et lecture, sans interface Streamlit."""
from pathlib import Path
import hashlib
import json
import urllib.error
import urllib.request

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "raw" / "2026"
MANIFEST = ROOT / "config" / "sources.json"


def file_hash(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def ensure_data(data_dir=DATA_DIR):
    """Télécharge les fichiers absents et vérifie leurs empreintes officielles."""
    data_dir = Path(data_dir)
    data_dir.mkdir(parents=True, exist_ok=True)
    sources = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for name, info in sources["files"].items():
        target = data_dir / name
        if target.exists():
            if target.stat().st_size == info["bytes"] and file_hash(target) == info["sha256"]:
                continue
            raise ValueError(f"Unexpected data file: {target}. Move it aside and download the documented version.")
        temporary = data_dir / (name + ".part")
        request = urllib.request.Request(info["url"], headers={"User-Agent": "student-so-2026-project"})
        try:
            with urllib.request.urlopen(request, timeout=90) as response, temporary.open("wb") as output:
                for block in iter(lambda: response.read(1024 * 1024), b""):
                    output.write(block)
        except (OSError, urllib.error.URLError) as error:
            temporary.unlink(missing_ok=True)
            raise RuntimeError(f"Could not download {name}. Check internet access and retry: {error}") from error
        if temporary.stat().st_size != info["bytes"] or file_hash(temporary) != info["sha256"]:
            temporary.unlink(missing_ok=True)
            raise ValueError(f"Download verification failed for {name}. A Git LFS pointer or partial download is not valid data.")
        temporary.replace(target)
    return data_dir


def load_responses(path=DATA_DIR / "survey_results_public.csv"):
    frame = pd.read_csv(path, low_memory=False)
    if frame["ResponseId"].isna().any() or not frame["ResponseId"].is_unique:
        raise ValueError("Expected one unique, non-missing ResponseId per 2026 response.")
    return frame


def load_schema(path=DATA_DIR / "survey_results_schema.csv"):
    return pd.read_csv(path)
