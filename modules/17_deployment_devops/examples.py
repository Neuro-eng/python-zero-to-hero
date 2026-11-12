import json
import logging
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    env: str = os.getenv("APP_ENV", "development")
    db_url: str = os.getenv("DATABASE_URL", "sqlite:///local.db")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    port: int = int(os.getenv("PORT", "8000"))

settings = Settings()

class JsonFormatter(logging.Formatter):
    def format(self, record):
        return json.dumps({"level": record.levelname, "msg": record.getMessage(), "env": settings.env})

handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter())
log = logging.getLogger("app")
log.addHandler(handler)
log.setLevel(logging.INFO)

def health():
    return {"status": "ok", "env": settings.env}

log.info("starting on port %s", settings.port)
print(health())
# Try: APP_ENV=production PORT=9000 python examples.py   (Windows: set APP_ENV=production)
