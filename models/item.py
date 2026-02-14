from pydantic import BaseModel

from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    owner = Column(String)
    college = Column(String)
    contact = Column(String)
    category = Column(String)
