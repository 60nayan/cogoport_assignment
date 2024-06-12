# app/api/endpoints/configurations.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import crud, schemas, models

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_configuration", response_model=schemas.CountryConfiguration)
def create_configuration(config: schemas.CountryConfigurationCreate, db: Session = Depends(get_db)):
    return crud.create_country_configuration(db=db, config=config)

@router.get("/get_configuration/{country_code}", response_model=schemas.CountryConfiguration)
def read_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_country_configuration(db=db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.post("/update_configuration/{country_code}", response_model=schemas.CountryConfiguration)
def update_configuration(country_code: str, config: schemas.CountryConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.update_country_configuration(db=db, country_code=country_code, config=config)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.delete("/delete_configuration/{country_code}", response_model=schemas.CountryConfiguration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.delete_country_configuration(db=db, country_code=country_code)
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config
