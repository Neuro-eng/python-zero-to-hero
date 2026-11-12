from collections import Counter, defaultdict

nums = [1, 2, 3, 4, 5, 6]
print([n * n for n in nums if n % 2 == 0])

students = {"Asha": 88, "Ravi": 75}
students["Meena"] = 92
for name, score in students.items():
    print(name, score)

print(Counter("mississippi").most_common(2))

groups = defaultdict(list)
for w in ["cat", "dog", "bird", "fish"]:
    groups[len(w)].append(w)
print(dict(groups))
