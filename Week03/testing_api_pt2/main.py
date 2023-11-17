#using API to create, access and delete data related to book items, authors and book stores
from typing import Dict, List
from dto import BookItem
from fastapi import FastAPI,HTTPException

app = FastAPI()

#create dictionary
my_book_items_dict: Dict[str, BookItem] = {}

#create PUT API
@app.put("/books/{name}")
def create_book(name: str, item: BookItem) -> None:
    my_book_items_dict[name] = item
    #print(my_book_items_dict)
    

#create GET API
@app.get("/books/{name}")
def read_book(name: str) -> BookItem:
    if name in my_book_items_dict.keys():
        return my_book_items_dict[name]
    else:
        raise HTTPException(status_code=404, detail="Book not found")

#create delete API
@app.delete("/books/{name}")
def delete_book(name: str) -> Dict:
    if name in my_book_items_dict.keys():
        my_book_items_dict.pop(name)
        #print(my_book_items_dict)
        return {"200": "Book successfully deleted"}

#create get all books API
@app.get("/books/")
def get_all_books() -> List[BookItem]:
    return my_book_items_dict.values()