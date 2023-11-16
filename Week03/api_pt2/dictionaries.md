author01 = Author(name="Rick Riordan", 
                  author_id="RRIO-4358")

author02 = Author(name="Christopher Paolini", 
                  author_id="CPAO-6455")

book01
"name": "Percy Jackson and the Lightning Thief",
"author": {"name": "Rick Riordan",
            "author_id": "RRIO-4358"},
"year_published": 2005

book02
"name": "Heroes of Olympus: the Lost Hero",
"author": {"name": "Rick Riordan",
            "author_id": "RRIO-4358"},
"year_published": 2010

book03
"name": "Eragon",
"author": {"name": "Christopher Paolini",
            "author_id": "CPAO-6455"},
"year_published": 2002

book04
"name": "Eldest",
"author": {"name": "Christopher Paolini",
            "author_id": "CPAO-6455"},
"year_published": 2005


book_store01 = BookStore(name="Page Turner's",
                         bookshelf=[book01, book02, book03, book04])


#invalid data
author_invalid = Author(name="John Doe",
                        author_id="j5oe-6435")

book_invalid = BookItem(name="Not Real",
                        author=author_invalid,
                        year_published=2016)

book_store_invalid = BookStore(name="Invalid Book Shop",
                               bookshelf=[book_invalid, book01])