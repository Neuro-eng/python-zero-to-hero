# Module 13: Advanced Python

## Concepts
- **Closures:** inner function remembers outer variables
- **Decorators:** wrap a function to add behavior (`@timer`, `@retry`)
- **Iterators and generators:** `__iter__`/`__next__`, `yield`, generator expressions (memory-friendly)
- **Context managers:** `with`, `__enter__`/`__exit__`, `contextlib.contextmanager`
- **Comprehensions in depth:** dict/set comprehensions, nested, conditional
- **asyncio:** `async def`, `await`, `asyncio.gather` (concurrent I/O, not CPU)

## Practice (easy to hard)
1. Write a closure `make_counter()`.
2. Write a `@timer` decorator printing run time.
3. Write `@retry(times=3)` that retries on exception.
4. Generator `countdown(n)`.
5. Generator that reads a large file line by line.
6. Generator for infinite Fibonacci; take first 10 with `itertools.islice`.
7. Context manager that times a code block.
8. Dict comprehension: word to length.
9. `asyncio.gather` three simulated API calls with `sleep`.
10. Cache a function with `functools.lru_cache` and compare speed.

## Interview questions
1. What is a decorator and how does it work?
2. Generator vs list: when to use which?
3. What does `yield` do?
4. What is the GIL and when does asyncio help?
5. What problem do context managers solve?

## Mini-project
**Resilient fetcher:** a `@retry` + `@timer` decorated function that downloads data, and a generator that yields results in chunks.
