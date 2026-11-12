import csv
import json
from pathlib import Path


def save_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_json(path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def column_total(csv_path, column):
    total = 0.0
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            total += float(row[column])
    return total


def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default
