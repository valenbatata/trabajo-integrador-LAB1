# tests/conftest.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # <repo-raiz>
SRC = ROOT / "src"                          # <repo-raiz>/src
src_str = str(SRC)
if src_str not in sys.path:
    sys.path.insert(0, src_str)

