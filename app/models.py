# app/models.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class CountryConfiguration(Base):
    __tablename__ = 'country_configurations'
    id = Column(Integer, primary_key=True)
    country_code = Column(String(2), nullable=False)
    business_name_required = Column(Boolean, nullable=False)
    pan_number_required = Column(Boolean, nullable=False)
    gstin_required = Column(Boolean, nullable=False)
