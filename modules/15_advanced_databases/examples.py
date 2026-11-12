import sqlite3

db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), amount REAL);
INSERT INTO customers (name) VALUES ('Asha'), ('Ravi'), ('Meena');
INSERT INTO orders (customer_id, amount) VALUES (1, 250), (1, 400), (2, 120);
CREATE INDEX idx_orders_customer ON orders(customer_id);
""")

print("INNER JOIN:", db.execute(
    "SELECT c.name, SUM(o.amount) FROM customers c JOIN orders o ON o.customer_id = c.id GROUP BY c.name").fetchall())
print("LEFT JOIN (no orders):", db.execute(
    "SELECT c.name FROM customers c LEFT JOIN orders o ON o.customer_id = c.id WHERE o.id IS NULL").fetchall())
print("HAVING:", db.execute(
    "SELECT customer_id, SUM(amount) t FROM orders GROUP BY customer_id HAVING t > 300").fetchall())
print("Subquery above average:", db.execute(
    "SELECT name FROM customers WHERE id IN (SELECT customer_id FROM orders GROUP BY customer_id "
    "HAVING SUM(amount) > (SELECT AVG(amount) FROM orders))").fetchall())
print("Rank:", db.execute(
    "SELECT customer_id, SUM(amount), RANK() OVER (ORDER BY SUM(amount) DESC) FROM orders GROUP BY customer_id").fetchall())
print("Plan:", db.execute("EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 1").fetchall())

try:                                   # transaction: all or nothing
    with db:
        db.execute("INSERT INTO orders (customer_id, amount) VALUES (3, 999)")
        raise RuntimeError("payment failed")
except RuntimeError:
    pass
print("rows after rollback:", db.execute("SELECT COUNT(*) FROM orders").fetchone()[0])
