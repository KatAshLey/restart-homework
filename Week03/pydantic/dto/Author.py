from pydantic import BaseModel, field_validator
import re

class Author(BaseModel):
    name: str
    author_id: str
    
    @field_validator("name")
    @classmethod
    def check_valid_name(cls, name: str):
        assert name.istitle(), "Name does not start with capitals"
        return name
    
    @field_validator("author_id")
    @classmethod
    def check_valid_author_id(cls, author_id: str):
        check_id=re.search(r"[A-Z]{4}-[0-9]{4}", author_id)
        return check_id != None and len(author_id) == 9
        """ assert author_id[0:4].isalpha() and author_id[-4:].isnumeric(), "Author Id is not XXXX-YYYY, X is capital letter, and Y is number"
        return author_id """
