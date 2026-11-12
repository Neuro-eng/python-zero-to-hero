# Module 14: Professional Python Development

## Concepts
- **Type hints:** `list[int]`, `dict[str, float]`, `Optional[str]` (or `str | None`), `Union`, `TypeVar` and generics; check with **mypy**
- **PEP 8:** snake_case, 4 spaces, 79-100 char lines, meaningful names
- **Tools:** `ruff check .` (linter), `black .` (formatter), `pytest --cov`
- **Logging** instead of `print`: levels DEBUG, INFO, WARNING, ERROR
- **Clean code:** small functions, one job each, no magic numbers, early returns
- **SOLID (short):** Single responsibility, Open/closed, Liskov, Interface segregation, Dependency inversion
- **Code review:** readability, tests, edge cases, naming, security (no secrets)

```bash
pip install ruff black mypy
ruff check . && black . && mypy .
```

## Practice (easy to hard)
1. Add type hints to five of your functions.
2. Replace `print` with `logging` in the expense tracker.
3. Run `black` and `ruff` on a project and fix every warning.
4. Replace magic numbers with named constants.
5. Split a 40-line function into three small ones.
6. Write a `Protocol` or abstract class and two implementations.
7. Apply dependency injection: pass a storage object instead of hard-coding a file.
8. Write a `pyproject.toml` with ruff and black settings.
9. Review a friend's code with a checklist and write 5 comments.
10. Add `mypy` to CI.

## Interview questions
1. Why use type hints if Python is dynamic?
2. What is PEP 8 and why follow it?
3. `print` vs `logging`?
4. Explain Single Responsibility with an example.
5. What do you check in a code review?

## Mini-project
**Refactor Project 1:** add type hints, logging, a storage class, tests, ruff and black, then open a pull request on your own repo.
