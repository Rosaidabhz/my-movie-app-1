from sqlalchemy import Column,String, Integer
from sqlalchemy.orm import relationship

from config.database import Base

class Reviewer(Base):
    __tablename__ = "reviewer"

    id = Column(Integer, primary_key = True, index =True)
    name = Column(String)