# Module 16: Advanced Backend Development

## Concepts
- **FastAPI in depth:** Pydantic validation (`Field`), response models, dependencies (`Depends`), routers, error handlers
- **Authentication vs authorization:** who you are vs what you may do
- **Passwords:** never store plain text; hash with `bcrypt` or `argon2`
- **JWT:** signed token with an expiry; send as `Authorization: Bearer <token>` (`pip install pyjwt`)
- **Middleware:** code that runs on every request (logging, CORS, timing)
- **Pagination:** `limit` + `offset` (or cursor) so lists stay fast
- **Background tasks:** `BackgroundTasks` for emails and slow jobs; Celery for heavy queues
- **Caching:** Redis for hot data with a time-to-live (TTL)
- **Config:** secrets in environment variables, never in code

## Practice (easy to hard)
1. Add `Field(min_length=3)` validation to a Pydantic model.
2. Return 422 and 404 errors with clear messages.
3. Add `limit` and `offset` query parameters to a list endpoint.
4. Add a timing middleware that adds `X-Process-Time`.
5. Create a dependency that checks an API key header.
6. Hash and verify a password.
7. Create and verify a JWT with a 15-minute expiry.
8. Protect an endpoint with a JWT dependency.
9. Send a fake email in a background task.
10. Cache an expensive endpoint in a dict, then in Redis.

## Interview questions
1. Authentication vs authorization?
2. How does JWT work and what are its risks?
3. Why paginate?
4. What is middleware?
5. How do you keep secrets out of code?

## Mini-project
**Notes API with login:** register, login (JWT), CRUD notes owned by the user, pagination, tests with `TestClient`.
