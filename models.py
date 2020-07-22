from sqlalchemy import Column, Integer, String
from database import Base


class Principle(Base):
    __tablename__ = "principle"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)


class Value(Base):
    __tablename__ = "value"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
