from fastapi.testclient import TestClient
from main import app
import json
import jsondiff

# basic test
# def test_basic_example():
#    assert True

# create test client
client = TestClient(app)




# TEST PUT API successful
def test_put_api():
    response = client.put("/books/Percy Jackson and the Lightning Thief", json={
        "name": "Percy Jackson and the Lightning Thief",
        "author": {"name": "Rick Riordan",
                   "author_id": "RRIO-4358"},
        "year_published": 2005
    })
    assert response.status_code == 200



# TEST PUT API unsuccessful
def test_put_api_unsuccessful():
    response = client.put("/books/Percy Jackson and the Lightning Thief", json={
        "name": "Percy Jackson and the Lightning Thief",
        "author": {"name": "rick riordan",
                   "author_id": "RRIO-4358"},
        "year_published": 2005
    })
    assert response.status_code == 400



# TEST GET API == PUT, GET, compare
def test_get_api():
    book01 = {"name": "Percy Jackson and the Lightning Thief",
              "author": {"name": "Rick Riordan",
                         "author_id": "RRIO-4358"},
              "year_published": 2005
              }

    book02 = {"name": "Heroes of Olympus: the Lost Hero",
              "author": {"name": "Rick Riordan",
                         "author_id": "RRIO-4358"},
              "year_published": 2010
              }

    # PUT
    put_response = client.put("/books/Percy Jackson and the Lightning Thief",
                              json=book01)

    # GET
    get_response = client.get("/books/Percy Jackson and the Lightning Thief")

    # compare request_json==get_response
    compare = jsondiff.diff(book02, get_response)

    if compare:
        print("difference found")
    # how to return status code to give fail as this gives pass even on forced error
    else:
        print("same data")





# TEST DELETE API == PUT, GET-successful, DELETE, GET-has to fail here
def test_delete_api():
    book03 = {"name": "Eragon",
              "author": {"name": "Christopher Paolini",
                         "author_id": "CPAO-6455"},
              "year_published": 2002}

    # PUT
    put_response = client.put("/books/Eragon",
                              json=book03)
    
    # GET - successful
    get_response = client.get("/books/Eragon")
    
    # compare del_request_json == get_response
    compare = jsondiff.diff(get_response, book03)
    
    if compare:
        print("difference found")
    # how to return status code to give fail as this gives pass even on forced error
    else:
        print("same data")
        
    # DELETE
    deleted_json = client.delete("/books/Eragon")
    
    # GET - unsuccessful/ item deleted
    get_response = client.get("/books/Eragon")
    
    # compare del_request_json == get_response
    compare = jsondiff.diff(get_response, book03)
    
    if compare:
        print("difference found")
    # how to return status code to give fail as this gives pass even on forced error
    else:
        print("same data")
        
        
        
        
    
# test GET all books
def test_get_all_api():
    book01 = {"name": "Percy Jackson and the Lightning Thief",
              "author": {"name": "Rick Riordan",
                         "author_id": "RRIO-4358"},
              "year_published": 2005
              }
    book02 = {"name": "Heroes of Olympus: the Lost Hero",
              "author": {"name": "Rick Riordan",
                         "author_id": "RRIO-4358"},
              "year_published": 2010
    }

    book03 = {"name": "Eragon",
              "author": {"name": "Christopher Paolini",
                         "author_id": "CPAO-6455"},
              "year_published": 2002
    }

    book04 = {"name": "Eldest",
              "author": {"name": "Christopher Paolini",
                         "author_id": "CPAO-6455"},
              "year_published": 2005
    }
    
    # PUT
    put_response = client.put("/books/Percy Jackson and the Lightning Thief",
                              json=book01)
    put_response = client.put("/books/Heroes of Olympus: the Lost Hero",
                              json=book02)
    put_response = client.put("/books/Eragon",
                              json=book03)
    put_response = client.put("/books/Eldest",
                              json=book04)
    
    # GET all
    response = client.get("/books/")
    
    ################### have to compare put * 4 books with response