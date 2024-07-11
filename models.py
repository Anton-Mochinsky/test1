from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Mem(Base):
    __tablename__ = "mems"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    image_url = Column(String)
