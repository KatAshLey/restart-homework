from dto import BookItem, Author, BookStore
from pydantic import ValidationError

def main():
    #define authors
    author01 = Author(name="Rick Riordan", 
                      author_id="RRIO-4358")
    author02 = Author(name="Christopher Paolini", 
                      author_id="CPAO-6455")
    #print(author01)
    #print(author02)
        
    #define bookItems
    book01 = BookItem(name="Percy Jackson and the Lightning Thief",
                      author=author01,
                      year_published=2005)
    book02 = BookItem(name="Heroes of Olympus: the Lost Hero",
                      author=author01,
                      year_published=2010)
    book03 = BookItem(name="Eragon",
                     author=author02,
                     year_published=2002)
    book04 = BookItem(name="Eldest",
                     author=author02,
                     year_published=2005)
    
    #print(book01)
    #print(book02)
    #print(book03)
    #print(book04)
    
    #define bookstore
    book_store01 = BookStore(name="Page Turner's",
                             bookshelf=[book01, book02, book03, book04])
    #print(book_store01)
    
    
    try:
        #valid data
        print(book_store01)
        
        #invalid data
        author_invalid = Author(name="John Doe",
                                author_id="j5oe-6435")
        book_invalid = BookItem(name="Not Real",
                                author=author_invalid,
                                year_published=2016)
        book_store_invalid = BookStore(name="Invalid Book Shop",
                                       bookshelf=[book_invalid, book01])
    except ValidationError as ve:
        print("Invalid Author name.  Name must start with capitals.")
    else:
        print(author_invalid.__dict__)

if __name__ == "__main__":
    main()