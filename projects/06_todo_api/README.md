# Project 6: To-do REST API (FastAPI + SQLite)

```bash
pip install fastapi uvicorn
uvicorn app:app --reload
```
Open http://127.0.0.1:8000/docs to try the endpoints.

| Method | Path | Purpose |
|--------|------|---------|
| GET | /todos | List todos |
| POST | /todos | Create a todo |
| PUT | /todos/{id} | Update a todo |
| DELETE | /todos/{id} | Delete a todo |

**Stretch goals:** authentication (JWT), pagination, Docker, deploy to Render or Railway.
