import json
from pathlib import Path

data = [{"item": "Tea", "amount": 20}, {"item": "Book", "amount": 350}]
path = Path("demo.json")
path.write_text(json.dumps(data, indent=2), encoding="utf-8")
print(json.loads(path.read_text(encoding="utf-8")))

try:
    int("abc")
except ValueError as err:
    print("Handled:", err)
finally:
    path.unlink(missing_ok=True)
