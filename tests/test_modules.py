import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent / "modules"


def load(module_dir):
    spec = importlib.util.spec_from_file_location(module_dir, ROOT / module_dir / "solutions.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_basics():
    m = load("01_basics")
    assert m.celsius_to_fahrenheit(100) == 212
    assert m.total_with_tip(100, 10) == 110
    assert m.swap(1, 2) == (2, 1)
    assert m.is_even(4) and not m.is_even(7)


def test_control_flow():
    m = load("02_control_flow")
    assert m.fizzbuzz(15)[-1] == "FizzBuzz"
    assert m.fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert [n for n in range(20) if m.is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19]
    assert m.digit_sum(-123) == 6


def test_functions():
    m = load("03_functions")
    assert m.factorial(5) == 120
    assert m.fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    assert m.is_palindrome("A man, a plan, a canal: Panama")
    assert len(m.generate_password(16)) == 16
    with pytest.raises(ValueError):
        m.generate_password(4)


def test_data_structures():
    m = load("04_data_structures")
    assert m.word_count("Hi hi, there!") == {"hi": 2, "there": 1}
    assert m.remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert m.group_by_length(["a", "bb", "c"]) == {1: ["a", "c"], 2: ["bb"]}
    assert m.two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_oop():
    m = load("05_oop")
    acct = m.BankAccount("Asha", 100)
    acct.deposit(50)
    acct.withdraw(30)
    assert acct.balance == 120
    with pytest.raises(ValueError):
        acct.withdraw(1000)
    assert m.Rectangle(2, 3).area() == 6
    assert round(m.Circle(1).area(), 2) == 3.14


def test_files(tmp_path):
    m = load("06_files_and_errors")
    f = tmp_path / "d.json"
    m.save_json(f, [{"a": 1}])
    assert m.load_json(f) == [{"a": 1}]
    assert m.load_json(tmp_path / "missing.json", default=[]) == []
    csv_file = tmp_path / "x.csv"
    csv_file.write_text("name,amount\na,10\nb,5.5\n")
    assert m.column_total(csv_file, "amount") == 15.5
    assert m.safe_int("x", 7) == 7 and m.safe_int("12") == 12


def test_automation():
    m = load("08_automation")
    assert m.extract_emails("a@b.com and x.y@z.org") == ["a@b.com", "x.y@z.org"]
    parsed = m.parse_log_line("2026-01-10 09:05:12 ERROR Database down")
    assert parsed["level"] == "ERROR" and parsed["msg"] == "Database down"
    assert m.parse_log_line("garbage") is None
