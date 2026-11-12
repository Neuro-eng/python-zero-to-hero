#!/usr/bin/env bash
# Upload the current folder to a NEW GitHub repo in one go (Mac / Linux / Git Bash).
# Usage:  bash upload_to_github.sh [repo-name] [private|public]
# Example: bash upload_to_github.sh python-zero-to-hero private

set -e

REPO_NAME="${1:-python-zero-to-hero}"
VISIBILITY="${2:-private}"

if [ "$VISIBILITY" != "private" ] && [ "$VISIBILITY" != "public" ]; then
  echo "Visibility must be 'private' or 'public'."; exit 1
fi

echo "== 1/6 Checking tools =="
command -v git >/dev/null 2>&1 || { echo "Git not found. Install from https://git-scm.com"; exit 1; }
command -v gh  >/dev/null 2>&1 || { echo "GitHub CLI not found. Install from https://cli.github.com"; exit 1; }

echo "== 2/6 Checking GitHub login =="
if ! gh auth status >/dev/null 2>&1; then
  echo "Not logged in. Starting login (choose GitHub.com, HTTPS, Y, web browser)..."
  gh auth login
fi

echo "== 3/6 Checking Git name and email =="
if [ -z "$(git config --global user.name)" ]; then
  read -r -p "Your name for commits: " GIT_NAME
  git config --global user.name "$GIT_NAME"
fi
if [ -z "$(git config --global user.email)" ]; then
  read -r -p "Your GitHub email: " GIT_EMAIL
  git config --global user.email "$GIT_EMAIL"
fi

echo "== 4/6 Preparing local repository =="
if [ ! -f README.md ]; then
  echo "README.md not found here. Run this script from inside the project folder."; exit 1
fi
[ -d .git ] || git init
git add .
if git diff --cached --quiet; then
  echo "Nothing new to commit."
else
  git commit -m "Initial commit: Python zero to hero"
fi
git branch -M main

echo "== 5/6 Creating GitHub repo and uploading everything =="
if git remote get-url origin >/dev/null 2>&1; then
  echo "Remote 'origin' already exists. Pushing to it..."
  git push -u origin main
else
  gh repo create "$REPO_NAME" "--$VISIBILITY" --source=. --remote=origin --push
fi

echo "== 6/6 Done =="
gh repo view --web || true
echo "Repo uploaded: $(git remote get-url origin)"
