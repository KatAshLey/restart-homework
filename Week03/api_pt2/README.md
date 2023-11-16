1) Start your main.py file clean, based on your Homework 1 or 2 output
2) Depending on whether you start off with Homework 1 or 2, create a few dictionaries

**Homework 2**
my_book_items_dict: Dict[str, BookItem]
    expecting 'name' to be the keys of the dictionary

3) Create PUT APIs, depending on your starting point
**Homework 2**
PUT /books/{name}
    body is the type of BookItem

4) Create GET APIs
**Homework 2**
GET /book/{name}
    if an item is found in the dictionary above(using dict keys) -> return body BookItem otherwise return HTTP Code 404

5) Create DELETE APIs

6) Create GET APIs(all items saved)

How do you test your API?
Just print out the contents of the dictionaries