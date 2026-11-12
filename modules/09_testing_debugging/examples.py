def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b


# Try: uncomment breakpoint() to step through with pdb
# breakpoint()
print(divide(10, 2))
