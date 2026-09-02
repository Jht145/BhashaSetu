import sys
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "backend")

for p in [BASE_DIR, BACKEND_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)
