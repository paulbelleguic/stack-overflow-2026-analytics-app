"""Point d'entrée unique du téléchargement, utilisable depuis un clone neuf."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.data import ensure_data

if __name__ == "__main__":
    directory = ensure_data()
    print(f"Fichiers 2026 vérifiés dans {directory}")
