import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
for sub in ["tools", "projects/01_expense_tracker", "projects/02_log_analyzer", "projects/03_file_organizer"]:
    sys.path.insert(0, str(ROOT / sub))
