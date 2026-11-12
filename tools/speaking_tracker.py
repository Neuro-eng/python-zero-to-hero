"""Log daily English-speaking practice and see your streak.

Usage:
    python tools/speaking_tracker.py log 20 "Shadowing + self intro"
    python tools/speaking_tracker.py stats
"""
import argparse
import json
from datetime import date, timedelta
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "english" / "practice_log.json"


def load(path=DB):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save(entries, path=DB):
    Path(path).write_text(json.dumps(entries, indent=2), encoding="utf-8")


def log_entry(entries, minutes, note="", day=None):
    if minutes <= 0:
        raise ValueError("minutes must be positive")
    entries.append({"date": (day or date.today()).isoformat(), "minutes": minutes, "note": note})
    return entries


def current_streak(entries, today=None):
    today = today or date.today()
    days = {e["date"] for e in entries}
    streak, d = 0, today
    if d.isoformat() not in days:  # allow the streak to continue if today isn't logged yet
        d -= timedelta(days=1)
    while d.isoformat() in days:
        streak += 1
        d -= timedelta(days=1)
    return streak


def stats(entries, today=None):
    total = sum(e["minutes"] for e in entries)
    days = len({e["date"] for e in entries})
    return {
        "total_minutes": total,
        "days_practiced": days,
        "average_per_day": round(total / days, 1) if days else 0,
        "current_streak": current_streak(entries, today),
    }


def main():
    p = argparse.ArgumentParser(description="English speaking practice tracker")
    sub = p.add_subparsers(dest="cmd", required=True)
    lg = sub.add_parser("log")
    lg.add_argument("minutes", type=int)
    lg.add_argument("note", nargs="?", default="")
    sub.add_parser("stats")
    args = p.parse_args()

    entries = load()
    if args.cmd == "log":
        try:
            save(log_entry(entries, args.minutes, args.note))
            print("Logged. Keep going!")
        except ValueError as err:
            print("Error:", err)
    else:
        for k, v in stats(entries).items():
            print(f"{k.replace('_', ' ').title():<20}{v}")


if __name__ == "__main__":
    main()
