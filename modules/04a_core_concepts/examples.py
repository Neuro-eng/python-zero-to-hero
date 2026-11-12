import copy
import time

# 1. Mutability
a = [1, 2]
b = a
b.append(3)
print("shared list:", a)          # [1, 2, 3]
s = "hi"
print("string methods create new strings:", s.upper(), s)

# 2. Mutable default trap and fix
def bad(x, items=[]):
    items.append(x)
    return items

def good(x, items=None):
    items = [] if items is None else items
    items.append(x)
    return items

print(bad(1), bad(2))             # [1, 2] - shared!
print(good(1), good(2))           # [1] [2]

# 3. Shallow vs deep copy
nested = [[1, 2], [3]]
shallow, deep = nested.copy(), copy.deepcopy(nested)
nested[0].append(99)
print("shallow:", shallow, "deep:", deep)

# 4. Scope
x = "global"
def outer():
    x = "enclosing"
    def inner():
        return x
    return inner()
print("LEGB:", outer(), x)

# 5. Strings
text = "  Python makes automation easy  "
print(text.strip().title(), "|", "-".join(text.split()), "|", text.strip()[::-1])
print(f"{1234567.891:,.2f}", f"{0.256:.1%}")

# 6. Truthiness
for v in [0, "", [], None, "0", [0]]:
    print(repr(v), bool(v))

# 7. Complexity
data = list(range(100_000)); lookup = set(data)
t = time.perf_counter(); 99_999 in data; t1 = time.perf_counter() - t
t = time.perf_counter(); 99_999 in lookup; t2 = time.perf_counter() - t
print(f"list: {t1:.6f}s  set: {t2:.6f}s")
