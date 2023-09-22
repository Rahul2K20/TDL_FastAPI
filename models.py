from database import Base 
from sqlalchemy import Column, Integer, Boolean, String 

class ToDo(Base):

    __tablename__ = "TDL"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    complete = Column(Boolean, default=False)

