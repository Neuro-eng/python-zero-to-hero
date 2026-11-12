import asyncio
import functools
import time
from contextlib import contextmanager
from itertools import islice

def timer(fn):
    @functools.wraps(fn)
    def wrapper(*a, **kw):
        start = time.perf_counter()
        result = fn(*a, **kw)
        print(f"{fn.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

def retry(times=3):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            for attempt in range(1, times + 1):
                try:
                    return fn(*a, **kw)
                except Exception as err:
                    print(f"attempt {attempt} failed: {err}")
            raise RuntimeError("all retries failed")
        return wrapper
    return deco

calls = {"n": 0}
@retry(times=3)
@timer
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ValueError("temporary error")
    return "ok"
print(flaky())

def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
c = make_counter(); c(); print("closure:", c())

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
print(list(islice(fib(), 10)))

@contextmanager
def block_timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.4f}s")
with block_timer("sum"):
    sum(range(1_000_000))

@functools.lru_cache(maxsize=None)
def slow_fib(n):
    return n if n < 2 else slow_fib(n - 1) + slow_fib(n - 2)
print(slow_fib(80))

async def fetch(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"
async def main():
    print(await asyncio.gather(fetch("A", 0.3), fetch("B", 0.2), fetch("C", 0.1)))
asyncio.run(main())
