"""Words-per-minute calculator for your presentation script.

Usage:
    python tools/wpm_calculator.py my_script.txt 90
Target pace for clear presentations: about 120-150 WPM.
"""
import sys
from pathlib import Path


def words_per_minute(text, seconds):
    if seconds <= 0:
        raise ValueError("seconds must be positive")
    return round(len(text.split()) / (seconds / 60), 1)


def pace_feedback(wpm):
    if wpm < 100:
        return "Slow: add energy, trim long pauses."
    if wpm <= 160:
        return "Good pace for presenting."
    return "Fast: slow down and pause after key points."


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    wpm = words_per_minute(text, float(sys.argv[2]))
    print(f"{wpm} words per minute. {pace_feedback(wpm)}")


if __name__ == "__main__":
    main()
