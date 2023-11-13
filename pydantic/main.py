from dto import BookItem, Author, BookStore

def main():
    #define authors
    author01 = Author(name="Rick Riordan", 
                      author_id="RRIO-4358")
    author02 = Author(name="Christopher Paolini", 
                      author_id="CPAO-6455")
    print(author01)
    print(author02)
        
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
    
    print(book01)
    print(book02)
    print(book03)
    print(book04)
    
    #define bookstore
    book_store01 = BookStore(name="Page Turner's",
                             bookshelf=[book01, book02, book03, book04])
    print(book_store01)

if __name__ == "__main__":
    main()