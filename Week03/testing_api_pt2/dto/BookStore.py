#Initializes book store class with name and bookshelf as list
from pydantic import BaseModel
from .BookItem import BookItem

class BookStore(BaseModel):
    name: str
    bookshelf: list[BookItem]