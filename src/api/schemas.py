from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Channel(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class Message(BaseModel):
    id: int
    channel_id: int
    content: str
    date: datetime
    has_image: bool

    class Config:
        orm_mode = True

class ImageDetection(BaseModel):
    id: int
    message_id: int
    detected_object_class: str
    confidence_score: float

    class Config:
        orm_mode = True 