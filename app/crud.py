# app/crud.py

from sqlalchemy.orm import Session
from .models import CountryConfiguration
from .schemas import CountryConfigurationCreate, CountryConfigurationUpdate

def create_country_configuration(db: Session, config: CountryConfigurationCreate):
    db_config = CountryConfiguration(**config.dict())
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def get_country_configuration(db: Session, country_code: str):
    return db.query(CountryConfiguration).filter(CountryConfiguration.country_code == country_code).first()

def update_country_configuration(db: Session, country_code: str, config: CountryConfigurationUpdate):
    db_config = db.query(CountryConfiguration).filter(CountryConfiguration.country_code == country_code).first()
    if db_config:
        for key, value in config.dict().items():
            setattr(db_config, key, value)
        db.commit()
        db.refresh(db_config)
    return db_config

def delete_country_configuration(db: Session, country_code: str):
    db_config = db.query(CountryConfiguration).filter(CountryConfiguration.country_code == country_code).first()
    if db_config:
        db.delete(db_config)
        db.commit()
    return db_config
