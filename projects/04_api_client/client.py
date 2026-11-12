import sys
import time

import requests

BASE = "https://jsonplaceholder.typicode.com"


def get_json(path, retries=3):
    for attempt in range(1, retries + 1):
        try:
            resp = requests.get(f"{BASE}{path}", timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as err:
            print(f"Attempt {attempt} failed: {err}")
            time.sleep(attempt)
    raise RuntimeError("API unavailable")


def completion_report(todos):
    done = sum(1 for t in todos if t["completed"])
    return {"total": len(todos), "done": done, "pending": len(todos) - done}


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    todos = get_json(f"/todos?_limit={limit}")
    print(completion_report(todos))
