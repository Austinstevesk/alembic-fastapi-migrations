from geoalchemy2 import Geometry
from sqlalchemy import Column, String, Integer

from ..db.sql import Base


class WeatherSource(Base):
    
    __tablename__ = "weather_source"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(Geometry('POLYGON'))
    location_name = Column(String(length=128), nullable=False)
    source_type = Column(String(length=48), nullable=False),
    source_name = Column(String(length=48), nullable=False)
    