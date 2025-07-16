from .database import SessionLocal
from .models import Message, Channel, ImageDetection
from sqlalchemy.orm import Session

# Example: get top products (stub)
def get_top_products(limit: int = 10):
    db: Session = SessionLocal()
    # Replace with actual query logic
    return [{"product": "paracetamol", "count": 42} for _ in range(limit)]

def get_channel_activity(channel_name: str):
    db: Session = SessionLocal()
    # Replace with actual query logic
    return {"channel": channel_name, "activity": []}

def search_messages(query: str):
    db: Session = SessionLocal()
    # Replace with actual query logic
    return [{"id": 1, "content": f"Message containing {query}"}] 