from .database import SessionLocal
from .models import Message, Channel, ImageDetection
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List

def get_top_products(limit: int = 10):
    db: Session = SessionLocal()
    try:
        # Example: count most mentioned products in messages (stub, replace with real logic)
        # Replace 'content' with actual product extraction logic
        result = db.query(Message.content, func.count(Message.id).label('count')) \
            .group_by(Message.content).order_by(func.count(Message.id).desc()).limit(limit).all()
        return [{"product": r[0], "count": r[1]} for r in result]
    finally:
        db.close()

def get_channel_activity(channel_name: str):
    db: Session = SessionLocal()
    try:
        channel = db.query(Channel).filter(Channel.name == channel_name).first()
        if not channel:
            return None
        # Example: count messages per day
        activity = db.query(func.date(Message.date), func.count(Message.id)) \
            .filter(Message.channel_id == channel.id) \
            .group_by(func.date(Message.date)).all()
        return {"channel": channel_name, "activity": [{"date": str(a[0]), "count": a[1]} for a in activity]}
    finally:
        db.close()

def search_messages(query: str):
    db: Session = SessionLocal()
    try:
        messages = db.query(Message).filter(Message.content.ilike(f"%{query}%")).all()
        return [
            {
                "id": m.id,
                "channel_id": m.channel_id,
                "content": m.content,
                "date": m.date,
                "has_image": m.has_image
            } for m in messages
        ]
    finally:
        db.close() 