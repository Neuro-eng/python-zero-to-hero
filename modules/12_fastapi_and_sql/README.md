# Module 12: FastAPI and SQL

## SQL (SQLite)
```sql
CREATE TABLE todos (id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER DEFAULT 0);
INSERT INTO todos (title) VALUES ('Learn Python');
SELECT * FROM todos WHERE done = 0 ORDER BY id DESC;
UPDATE todos SET done = 1 WHERE id = 1;
DELETE FROM todos WHERE id = 1;
-- JOIN and GROUP BY
SELECT c.name, COUNT(o.id) FROM customers c JOIN orders o ON o.customer_id = c.id GROUP BY c.name;
```

## FastAPI
- Routes, path/query parameters, request bodies with Pydantic
- Automatic docs at `/docs`
- Run: `uvicorn app:app --reload`

## Practice
Build **Project 6: To-do REST API** (`projects/06_todo_api`).

## Interview tip
Know the difference between PUT and PATCH, and between SQL `WHERE` and `HAVING`.
