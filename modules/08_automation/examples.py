import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser(description="Count .py files in a folder")
parser.add_argument("folder", nargs="?", default=".")
args = parser.parse_args()

files = list(Path(args.folder).rglob("*.py"))
print(f"Found {len(files)} Python files")
print(re.findall(r"[\w.]+@[\w.]+\.\w+", "Mail asha@example.com or ravi@test.org"))
