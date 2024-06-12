# app/models.py

from sqlalchemy import Column, Integer, String, Boolean  # Import Boolean type from SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CountryConfiguration(Base):
    __tablename__ = "country_configurations"

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True)
    business_name_required = Column(Boolean, default=False)
    pan_number_required = Column(Boolean, default=False)
    gstin_required = Column(Boolean, default=False)
    # Add more fields as per your requirements
