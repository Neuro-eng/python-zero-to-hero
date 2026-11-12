from datetime import date

import pytest

import analyzer
import organizer
import speaking_tracker as st
import tracker
import wpm_calculator as wpm


def test_expense_tracker(tmp_path):
    db = tmp_path / "e.json"
    data = tracker.load(db)
    assert data == []
    tracker.add_expense(data, 100, "food", "lunch")
    tracker.add_expense(data, 50, "food")
    tracker.add_expense(data, 200, "travel")
    tracker.save(data, db)
    assert tracker.summarize(tracker.load(db)) == {"food": 150.0, "travel": 200.0}
    with pytest.raises(ValueError):
        tracker.add_expense(data, -5, "x")


def test_log_analyzer():
    lines = [
        "2026-01-10 09:00:01 INFO ok",
        "2026-01-10 09:05:12 ERROR db fail",
        "2026-01-10 09:06:00 ERROR db fail",
        "bad line",
    ]
    levels, errors = analyzer.analyze(lines)
    assert levels["INFO"] == 1 and levels["ERROR"] == 2
    assert errors.most_common(1) == [("db fail", 2)]


def test_file_organizer(tmp_path):
    (tmp_path / "a.png").write_text("x")
    (tmp_path / "b.pdf").write_text("x")
    (tmp_path / "c.xyz").write_text("x")
    organizer.organize(tmp_path, dry_run=True)
    assert (tmp_path / "a.png").exists()
    organizer.organize(tmp_path)
    assert (tmp_path / "Images" / "a.png").exists()
    assert (tmp_path / "Documents" / "b.pdf").exists()
    assert (tmp_path / "Other" / "c.xyz").exists()


def test_speaking_tracker_streak():
    entries = []
    st.log_entry(entries, 20, day=date(2026, 1, 1))
    st.log_entry(entries, 30, day=date(2026, 1, 2))
    st.log_entry(entries, 10, day=date(2026, 1, 3))
    s = st.stats(entries, today=date(2026, 1, 3))
    assert s["current_streak"] == 3 and s["total_minutes"] == 60
    assert st.current_streak(entries, today=date(2026, 1, 6)) == 0
    with pytest.raises(ValueError):
        st.log_entry(entries, 0)


def test_wpm():
    assert wpm.words_per_minute("word " * 130, 60) == 130
    assert "Good" in wpm.pace_feedback(130)
    with pytest.raises(ValueError):
        wpm.words_per_minute("x", 0)
