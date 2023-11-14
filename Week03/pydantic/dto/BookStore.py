from pydantic import BaseModel
from .BookItem import BookItem

class BookStore(BaseModel):
    name: str
    bookshelf: list[BookItem]