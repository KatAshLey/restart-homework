1) Start your main.py file clean, based on your Homework 1 or 2 output
2) Depending on whether you start off with Homework 1 or 2, create a few dictionaries

**Homework 1**
my_inventory_items_dict: Dict[str, InventoryItem]
    expecting the 'serial_num' to be keys of the Dict


3) Create PUT APIs, depending on your starting point

**Homework 1**
PUT /items/{serial_num}
    body is the type of InventoryItem


4) Create GET APIs

**Homework 1**
GET /items/{serial_num}
    if an item is found in the dictionary above (using dict keys) -> returns body InventoryItem otherwise return HTTP Code 404


How do you test your API?
Just print out the contents of the dictionaries






2)
**Homework 2**
my_book_items_dict: Dict[str, BookItem]
    expecting 'name' to be the keys of the dictionary

3)
**Homework 2**
PUT /books/{name}
    body is the type of BookItem

4)
**Homework 2**
GET /book/{name}
    if an item is found in the dictionary above(using dict keys) -> return body BookItem otherwise return HTTP Code 404