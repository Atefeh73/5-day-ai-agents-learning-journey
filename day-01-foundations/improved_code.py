
import time
from typing import Dict, List, Optional


def get_user_data(users_dict: Dict[int, dict], user_id: int) -> Optional[dict]:
    # O(1) dictionary lookup
    return users_dict.get(user_id)


def process_payments(items: List[dict]) -> float:
    total = 0.0
    for i in items:
        price = i.get("price", 0.0)  # Safe key access
        tax = price * 0.1
        total += price + tax
        time.sleep(0.1)  # Simulate network latency

    return total


def run_batch() -> None:
    # Use a dictionary for O(1) user lookup by ID
    users = {
        1: {"id": 1, "name": "Alice"},
        2: {"id": 2, "name": "Bob"},
    }
    items = [{"price": 10}, {"price": 20}, {"price": 100}]

    # Safe retrieval with fallback check
    u = get_user_data(users, 3)
    if u:
        print(f"User found: {u['name']}")
    else:
        print("User not found.")

    print(f"Total: {process_payments(items):.2f}")


if __name__ == "__main__":
    run_batch()
