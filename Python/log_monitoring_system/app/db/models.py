from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class AlertLog(Base):
    __tablename__ = 'alert_logs'

    id = Column(Integer, primary_key=True)
    message = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow)
