#Initialize Item Origin, check valid country
from pydantic import BaseModel, field_validator

#initialize item origin class
class ItemOrigin(BaseModel):
    country: str
    production_date: str
    
    #checks for a valid country
    @field_validator("country")
    @classmethod 
    def check_valid_country(cls, country: str):
        assert country == "Ethiopia", "country name must be Ethiopia"
        return country

