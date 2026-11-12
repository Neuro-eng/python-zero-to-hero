import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("shop")

TAX_RATE = 0.18                      # named constant, not a magic number

@dataclass
class Item:
    name: str
    price: float
    qty: int = 1

def total(items: list[Item], discount: Optional[float] = None) -> float:
    subtotal = sum(i.price * i.qty for i in items)
    if discount:
        subtotal *= 1 - discount
    return round(subtotal * (1 + TAX_RATE), 2)

class Storage(ABC):                  # depend on an abstraction
    @abstractmethod
    def save(self, data: dict) -> None: ...

class MemoryStorage(Storage):
    def __init__(self) -> None:
        self.rows: list[dict] = []
    def save(self, data: dict) -> None:
        self.rows.append(data)

class OrderService:
    def __init__(self, storage: Storage) -> None:
        self.storage = storage       # dependency injection
    def place(self, items: list[Item]) -> float:
        amount = total(items)
        self.storage.save({"amount": amount})
        log.info("order placed amount=%s", amount)
        return amount

svc = OrderService(MemoryStorage())
svc.place([Item("Book", 300, 2), Item("Pen", 20)])
