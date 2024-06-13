# app/schemas.py

from pydantic import BaseModel

class CountryConfigurationBase(BaseModel):
    country_code: str
    business_name_required: bool = False
    pan_number_required: bool = False
    gstin_required: bool = False
    

class CountryConfigurationCreate(CountryConfigurationBase):
    pass

class CountryConfigurationUpdate(CountryConfigurationBase):
    pass

class CountryConfiguration(CountryConfigurationBase):
    id: int

    class Config:
        orm_mode = True
