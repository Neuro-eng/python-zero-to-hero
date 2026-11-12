import random
import string


def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    return 1 if n in (0, 1) else n * factorial(n - 1)


def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq


def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def generate_password(length=12):
    if length < 8:
        raise ValueError("length must be at least 8")
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))
