import requests

URL = "https://jsonplaceholder.typicode.com/todos/1"

try:
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()
    print(resp.json())
except requests.RequestException as err:
    print("Request failed:", err)
