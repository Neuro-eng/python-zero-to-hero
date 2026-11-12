# Module 07: Modules, Virtual Environments, Git and GitHub

## Python
- `import`, `from x import y`, writing your own module
- `if __name__ == "__main__":`
- Virtual environments: `python -m venv .venv`
- `pip install`, `pip freeze > requirements.txt`

## Git essentials
```bash
git init
git add .
git commit -m "Add expense tracker"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```
Everyday commands: `git status`, `git log --oneline`, `git switch -c feature/x`, `git pull`, `git merge`.

## Practice
1. Create a `utils.py` and import it into another file.
2. Put every module solution on GitHub with a clear README.
3. Make a branch, change something, open a Pull Request on your own repo.

## Good commit messages
Short, imperative, specific: `Fix crash when amount is empty`, not `changes`.

## Speak it
Explain "What is Git and why do teams use it?" in 1 minute.
