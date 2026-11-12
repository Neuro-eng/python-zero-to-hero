# Module 4B: Core Concepts Supplement

Fills the gaps beginners hit in interviews: mutability, scope, truthiness, strings, copying, complexity.

## Concepts
- **Mutable** (list, dict, set) vs **immutable** (int, str, tuple, frozenset)
- **Scope (LEGB):** Local, Enclosing, Global, Built-in
- **Truthiness:** `0`, `""`, `[]`, `{}`, `None` are falsy
- **Strings:** `split`, `join`, `strip`, `replace`, `find`, `startswith`, slicing `s[::-1]`, f-string formats `{x:.2f}`, `{n:,}`
- **Copying:** assignment shares the object; `.copy()` is shallow; `copy.deepcopy()` is deep
- **Complexity:** list index O(1), list `in` O(n), set/dict lookup O(1) average, sort O(n log n)

## Practice (easy to hard)
1. Print the type and truthiness of `0, "", [], None, "0"`.
2. Reverse a string with slicing.
3. Count vowels in a sentence.
4. Title-case a sentence and strip extra spaces.
5. Format `1234567.891` as `1,234,567.89`.
6. Show that appending to a list inside a function changes the caller's list.
7. Fix the mutable default argument bug `def f(x, items=[])`.
8. Copy a nested list shallow vs deep and show the difference.
9. Check whether two strings are anagrams.
10. Time `x in list` vs `x in set` for 100,000 items.

## Interview questions
1. Mutable vs immutable: examples and why it matters?
2. What is the mutable default argument trap?
3. Shallow vs deep copy?
4. Explain LEGB.
5. Why is set lookup faster than list lookup?

## Mini-project
**Text analyzer:** read a paragraph, report word count, longest word, top 3 words, and vowel count.
