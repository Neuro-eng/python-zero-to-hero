import sqlite3
from contextlib import closing

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

DB_PATH = "todos.db"
app = FastAPI(title="To-do API")


class TodoIn(BaseModel):
    title: str
    done: bool = False


def conn():
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    c.execute("CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER DEFAULT 0)")
    return c


@app.get("/todos")
def list_todos():
    with closing(conn()) as c:
        return [dict(r) for r in c.execute("SELECT * FROM todos ORDER BY id")]


@app.post("/todos", status_code=201)
def create_todo(todo: TodoIn):
    with closing(conn()) as c:
        cur = c.execute("INSERT INTO todos (title, done) VALUES (?, ?)", (todo.title, int(todo.done)))
        c.commit()
        return {"id": cur.lastrowid, **todo.model_dump()}


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoIn):
    with closing(conn()) as c:
        cur = c.execute("UPDATE todos SET title=?, done=? WHERE id=?", (todo.title, int(todo.done), todo_id))
        c.commit()
        if cur.rowcount == 0:
            raise HTTPException(404, "Todo not found")
        return {"id": todo_id, **todo.model_dump()}


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    with closing(conn()) as c:
        cur = c.execute("DELETE FROM todos WHERE id=?", (todo_id,))
        c.commit()
        if cur.rowcount == 0:
            raise HTTPException(404, "Todo not found")
