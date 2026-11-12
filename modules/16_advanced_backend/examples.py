# pip install fastapi uvicorn httpx
# Run: uvicorn examples:app --reload     then open http://127.0.0.1:8000/docs
import time

from fastapi import BackgroundTasks, Depends, FastAPI, Header, HTTPException, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Advanced backend demo")
ITEMS = [{"id": i, "name": f"item-{i}"} for i in range(1, 51)]
API_KEY = "demo-key"          # in real apps: read from an environment variable


class ItemIn(BaseModel):
    name: str = Field(min_length=3, max_length=40)


@app.middleware("http")
async def timing(request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}"
    return response


def require_key(x_api_key: str = Header(default="")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")


@app.get("/items")
def list_items(limit: int = Query(10, ge=1, le=100), offset: int = Query(0, ge=0)):
    page = ITEMS[offset: offset + limit]
    return {"total": len(ITEMS), "limit": limit, "offset": offset, "items": page}


def send_email(name: str):
    print(f"(background) email sent about {name}")


@app.post("/items", status_code=201, dependencies=[Depends(require_key)])
def create_item(item: ItemIn, tasks: BackgroundTasks):
    new = {"id": len(ITEMS) + 1, "name": item.name}
    ITEMS.append(new)
    tasks.add_task(send_email, item.name)
    return new
