from sqlalchemy import  Column,  Integer, String, Float
from .database import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True)
    expression = Column(String, index=True)
    result = Column(Float, index=True)
