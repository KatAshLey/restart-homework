from pydantic import BaseModel, field_validator
from .Author import Author

class BookItem(BaseModel):
    name: str
    author: Author
    year_published: int
    
    @field_validator("year_published")
    @classmethod
    def check_valid_year_published(cls, year_published: int):
        assert year_published <= 2023 and year_published >= -3000, "Year published must be within -3000 and 2023"
        return year_published 