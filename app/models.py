from calendar import c
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Team(Base):
    __tablename__ = "sports_teams"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    sports = Column(String, nullable=False)
    founded_year = Column(Integer, nullable=True)
    championships = Column(Integer, nullable=True)