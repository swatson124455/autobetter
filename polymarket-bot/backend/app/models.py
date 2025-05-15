from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Market(Base):
    __tablename__ = 'markets'
    id = Column(String, primary_key=True)
    name = Column(String)
    yes_prob = Column(Float)
    no_prob = Column(Float)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class Trade(Base):
    __tablename__ = 'trades'
    id = Column(Integer, primary_key=True, autoincrement=True)
    market_id = Column(String)
    side = Column(String)
    amount = Column(Float)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
