from pydantic import BaseModel

class Author(BaseModel):
    name: str
    author_id: str

def main():
    author_01 = Author(name = "Rick Riordan", author_id = "RRIO-8625")
    print(author_01)
    author_not_valid_name = Author(name = "john doe", author_id="Jfo1-5H46")
    print(author_not_valid_name)
    
if __name__ == "__main__":
    main()