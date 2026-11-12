import argparse
import re
from collections import Counter

LOG_RE = re.compile(r"^(\S+) (\S+) ([A-Z]+) (.*)$")


def analyze(lines):
    levels, errors = Counter(), Counter()
    for line in lines:
        m = LOG_RE.match(line.strip())
        if not m:
            continue
        level, msg = m.group(3), m.group(4)
        levels[level] += 1
        if level == "ERROR":
            errors[msg] += 1
    return levels, errors


def main():
    p = argparse.ArgumentParser()
    p.add_argument("logfile")
    args = p.parse_args()
    with open(args.logfile, encoding="utf-8") as f:
        levels, errors = analyze(f)
    print("Levels:", dict(levels))
    print("Top errors:")
    for msg, count in errors.most_common(5):
        print(f"  {count}x {msg}")


if __name__ == "__main__":
    main()
