# Interview English: Structures and Sample Answers

## Two structures to memorize

**STAR** (for experience questions): **S**ituation, **T**ask, **A**ction, **R**esult
**PREP** (for opinion/technical questions): **P**oint, **R**eason, **E**xample, **P**oint

## 1. "Tell me about yourself" (60-90 seconds)
Structure: Present, Past, Future.

> "Good morning. My name is ___. I'm a recent graduate in ___ and I'm learning Python development.
> Over the last few months, I've built six projects, including an expense tracker, a log analyzer and a REST API using FastAPI. I publish all of them on GitHub.
> I enjoy solving problems with code and automating repetitive tasks.
> I'm now looking for an entry-level Python role where I can learn from a team and contribute from day one."

## 2. "Why should we hire you?"
> "I'm a fast learner with a strong Python foundation, and I can show it with real projects on GitHub. I communicate clearly, I ask questions early, and I finish what I start. I'd bring energy and discipline to the team."

## 3. "What are your strengths and weaknesses?"
> "My strength is consistency. I practice coding every day and I've committed code for X days in a row.
> A weakness I'm working on is public speaking. I practice by recording presentations and getting feedback, and it's improving every week."

## 4. "Describe a challenge you faced" (STAR)
> "**Situation:** In my expense tracker, the app crashed when the JSON file was empty.
> **Task:** I needed to make the app reliable.
> **Action:** I read the traceback, found the missing error handling, and wrapped file loading in try/except. I also added a test.
> **Result:** The crash disappeared and I learned to always test edge cases."

## 5. Technical questions: sample answers

**What is the difference between a list and a tuple?**
> "A list is mutable, so you can change it after creation. A tuple is immutable. I use tuples for fixed data, like coordinates, and lists for collections that change. Tuples can also be dictionary keys, because they're hashable."

**What is a decorator?**
> "A decorator is a function that takes another function and adds behavior without changing its code. For example, I can write a timer decorator to measure how long a function takes."

**What is the difference between `==` and `is`?**
> "`==` compares values. `is` checks whether two names point to the exact same object in memory."

**What are `*args` and `**kwargs`?**
> "`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary."

**What is a virtual environment and why use it?**
> "It's an isolated Python environment for one project, so dependencies don't conflict between projects. I create it with `python -m venv`."

**What is a REST API?**
> "It's a way for programs to communicate over HTTP using standard methods: GET to read, POST to create, PUT or PATCH to update, DELETE to remove. Data is usually exchanged as JSON."

## 6. Thinking aloud during coding rounds
- "Let me restate the problem to make sure I understand."
- "A simple approach is brute force. It would be O(n squared). Then I'll look for something faster."
- "I'll use a dictionary here because lookups are O(1)."
- "Let me test with an edge case: an empty list."
- "I'd improve this by..."

## 7. When you don't know the answer
> "I haven't worked with that directly. My understanding is ___. I'd start by reading the documentation and testing a small example."

Honesty plus a learning plan is better than guessing.

## 8. Questions to ask the interviewer
- "What does the first 90 days look like for this role?"
- "How does the team handle code reviews and mentoring?"
- "What technologies does the team use day to day?"
- "How do you measure success for this role?"

## 9. Salary and notice period (stay calm and polite)
- "I'm looking for a fair package based on the role and market range. Could you share the budgeted range?"
- "My notice period is ___, and I'm open to discussing a faster transition."

## 10. Closing
> "Thank you for your time. I'm very interested in this role and I'd be glad to share any more details."

## Follow-up email
> Subject: Thank you - Python Developer interview
>
> Dear ___,
> Thank you for speaking with me today. I enjoyed learning about ___. Our discussion made me even more interested in the role. Please let me know if you need anything else from me.
> Best regards,
> ___
