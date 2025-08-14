from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass
class Order:
    """Represents a simulated order."""

    id: str
    symbol: str
    side: str
    amount: float
    price: float
    timestamp: datetime
    status: str


_orders: list[Order] = []


def simulate_order(symbol: str, side: str, amount: float, price: float) -> Order:
    """Create and store a fake filled order."""
    order = Order(
        id=uuid4().hex,
        symbol=symbol,
        side=side,
        amount=amount,
        price=price,
        timestamp=datetime.utcnow(),
        status="filled",
    )
    _orders.append(order)
    return order


def list_orders() -> list[Order]:
    """Return a copy of all simulated orders."""
    return list(_orders)
