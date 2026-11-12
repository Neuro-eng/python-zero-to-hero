def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def total_with_tip(bill, tip_percent):
    return round(bill * (1 + tip_percent / 100), 2)


def swap(a, b):
    a, b = b, a
    return a, b


def is_even(n):
    return n % 2 == 0
