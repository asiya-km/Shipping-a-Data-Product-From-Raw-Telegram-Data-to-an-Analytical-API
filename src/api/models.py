from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Channel(Base):
    __tablename__ = 'dim_channels'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Message(Base):
    __tablename__ = 'fct_messages'
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey('dim_channels.id'))
    content = Column(String)
    date = Column(DateTime)
    has_image = Column(Boolean)

class ImageDetection(Base):
    __tablename__ = 'fct_image_detections'
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey('fct_messages.id'))
    detected_object_class = Column(String)
    confidence_score = Column(Float) 