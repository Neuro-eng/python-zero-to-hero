# Module 15: Advanced Database Development

## Concepts
- **Joins:** INNER, LEFT, (RIGHT, FULL); **subqueries**; `GROUP BY` + `HAVING`; window functions (`ROW_NUMBER`, `RANK`)
- **Indexes:** speed up reads, slow writes; use `EXPLAIN` to check
- **Transactions:** ACID, `BEGIN`, `COMMIT`, `ROLLBACK`
- **Normalization:** 1NF, 2NF, 3NF; primary and foreign keys
- **PostgreSQL:** the standard production database; connect with `psycopg`
- **SQLAlchemy ORM:** classes map to tables (see snippet below)
- **Migrations:** version your schema with **Alembic**

```python
# SQLAlchemy 2.x sketch (pip install sqlalchemy)
from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session

class Base(DeclarativeBase): pass
class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    orders: Mapped[list["Order"]] = relationship(back_populates="customer")
class Order(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float]
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    customer: Mapped[Customer] = relationship(back_populates="orders")

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
with Session(engine) as s:
    s.add(Customer(name="Asha", orders=[Order(amount=250)]))
    s.commit()
    print(s.scalars(select(Customer)).all())
```

## Practice (easy to hard)
1. Create `customers` and `orders` tables with a foreign key.
2. INNER JOIN to list customer names with order totals.
3. LEFT JOIN to find customers with no orders.
4. `GROUP BY` customer, `HAVING SUM(amount) > 500`.
5. Subquery: customers whose total is above the average.
6. Create an index and compare `EXPLAIN QUERY PLAN` before and after.
7. Run a transaction that rolls back on error.
8. Window function: rank customers by spend.
9. Normalize a messy single table into three tables.
10. Rebuild the to-do API with SQLAlchemy.

## Interview questions
1. INNER vs LEFT JOIN?
2. What is an index and what is its cost?
3. What does ACID mean?
4. `WHERE` vs `HAVING`?
5. What is an ORM and what are its trade-offs?

## Mini-project
**Shop database:** customers, products, orders and order items; write 10 reporting queries (top customers, monthly revenue, unsold products).
