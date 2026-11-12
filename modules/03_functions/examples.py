def greet(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"


def total(*numbers, **options):
    result = sum(numbers)
    if options.get("round"):
        result = round(result)
    return result


print(greet("Ravi"))
print(greet("Ravi", greeting="Namaste"))
print(total(1.4, 2.4, round=True))

people = [("Asha", 25), ("Ravi", 21), ("Meena", 30)]
print(sorted(people, key=lambda p: p[1]))
