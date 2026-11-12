import argparse
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

DB = Path(__file__).with_name("expenses.json")


def load(path=DB):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save(expenses, path=DB):
    Path(path).write_text(json.dumps(expenses, indent=2), encoding="utf-8")


def add_expense(expenses, amount, category, note=""):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    expenses.append(
        {"date": date.today().isoformat(), "amount": amount, "category": category, "note": note}
    )
    return expenses


def summarize(expenses):
    totals = defaultdict(float)
    for e in expenses:
        totals[e["category"]] += e["amount"]
    return dict(totals)


def main():
    p = argparse.ArgumentParser(description="Expense Tracker")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add")
    a.add_argument("amount", type=float)
    a.add_argument("category")
    a.add_argument("note", nargs="?", default="")
    sub.add_parser("list")
    sub.add_parser("summary")
    args = p.parse_args()

    data = load()
    if args.cmd == "add":
        try:
            save(add_expense(data, args.amount, args.category, args.note))
            print("Added.")
        except ValueError as err:
            print("Error:", err)
    elif args.cmd == "list":
        for e in data:
            print(f'{e["date"]}  {e["amount"]:>8.2f}  {e["category"]:<10} {e["note"]}')
    else:
        for cat, total in sorted(summarize(data).items(), key=lambda x: -x[1]):
            print(f"{cat:<12}{total:>10.2f}")


if __name__ == "__main__":
    main()
