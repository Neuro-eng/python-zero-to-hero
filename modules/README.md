# Module 17: Deployment and DevOps

## Concepts
- **Linux essentials:** `ls cd pwd cat grep find chmod ps top df tail -f`, `ssh`, `systemctl`
- **Environment variables:** config and secrets outside code (`.env` locally, platform settings in production)
- **Docker:** image (recipe) vs container (running instance); `Dockerfile`, `docker build`, `docker run -p 8000:8000`
- **CI/CD:** CI runs tests on every push; CD deploys when tests pass (GitHub Actions)
- **Cloud deployment:** Render, Railway, Fly.io (simple), AWS/Azure/GCP (industry)
- **Monitoring:** logs, health-check endpoint, uptime alerts, error tracking

## Dockerfile for a FastAPI app
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```
```bash
docker build -t todo-api .
docker run -p 8000:8000 -e APP_ENV=production todo-api
```

## GitHub Actions workflow (`.github/workflows/tests.yml`)
```yaml
name: tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -r requirements.txt
      - run: pytest -q
```

## Practice (easy to hard)
1. Find all `.py` files with `find` and count lines with `wc -l`.
2. Search a log for ERROR with `grep -c`.
3. Read a setting from an environment variable with a default.
4. Write a `.gitignore` that excludes `.env`.
5. Write a `Dockerfile` for Project 6 and run it.
6. Add a `/health` endpoint returning `{"status": "ok"}`.
7. Add a CI workflow that runs pytest and ruff.
8. Deploy the API to Render or Railway.
9. Add structured logging and read the logs on the platform.
10. Roll back a bad deployment to the previous version.

## Interview questions
1. Docker image vs container?
2. What is CI/CD?
3. Why use environment variables?
4. What happens if a container crashes?
5. How do you debug a failing production deployment?

## Mini-project
**Ship it:** containerize the to-do or notes API, add CI, deploy to a free tier, and put the live URL on your resume.
