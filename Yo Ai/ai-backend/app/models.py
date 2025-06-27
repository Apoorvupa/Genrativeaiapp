from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ChatMessage(Base):
    __tablename__ = "chat_messages"
    id = Column(Integer, primary_key=True, index=True)
    sender = Column(String(10))  # 'user' or 'bot'
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
