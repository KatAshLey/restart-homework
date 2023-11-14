Part I (should really finish):
Construct 3 classes with Pydantic classes in a modules

BookItem:
name type of string
author type of Author object
year_published type of integer, validate to be in range of current year (2023 to -3000)

Author:
name type of string, validate name to be normal capital case "John Doe"
author_id type of string, validate it to have format "XXXX-YYYY", X is capital letter, and Y is number

BookStore:
name of book store, type of string
book_shelve, type of List of BookItem

Give some examples inside `main()` of `main.py`

Part II (bonus):

Demonstrate property validation using the flow of `try/except/else` in `main()`

try:
 do something wrong with input validation
except ValidationError as ve:
 print("demonstrating that the Author name has to be valid")
else:
 print(my_author.__dict__)
