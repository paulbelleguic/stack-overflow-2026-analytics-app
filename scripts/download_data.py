"""Data-download entry point for a fresh clone."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data import ensure_data

if __name__ == "__main__":
    directory = ensure_data()
    print(f"2026 files verified in {directory}")
