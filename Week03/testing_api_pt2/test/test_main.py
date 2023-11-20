from fastapi.testclient import TestClient
from main import app
import json
import jsondiff

# basic test
# def test_basic_example():
#    assert True

# create test client
client = TestClient(app)

book01 = {
    "name": "Percy Jackson and the Lightning Thief",
    "author": {"name": "Rick Riordan", "author_id": "RRIO-4358"},
    "year_published": 2005,
}

book01_unsuccess = {
    "name": "Percy Jackson and the Lightning Thief",
    "author": {"name": "dgrick Riordan", "author_id": "RRIO-4358"},
    "year_published": 2005,
}

book02 = {
    "name": "Heroes of Olympus: the Lost Hero",
    "author": {"name": "Rick Riordan", "author_id": "RRIO-4358"},
    "year_published": 2010,
}

book03 = {
    "name": "Eragon",
    "author": {"name": "Christopher Paolini", "author_id": "CPAO-6455"},
    "year_published": 2002,
}

book04 = {
    "name": "Eldest",
    "author": {"name": "Christopher Paolini", "author_id": "CPAO-6455"},
    "year_published": 2005,
}


# TEST PUT API successful
def test_put_api():
    response = client.put(
        "/books/Percy Jackson and the Lightning Thief", json=book01
    )
    assert response.status_code == 200


# TEST PUT API unsuccessful
def test_put_api_unsuccessful():
    response = client.put(
        "/books/Percy Jackson and the Lightning Thief",
        headers={"Content-Type": "application/json"},
        json=book01_unsuccess,
    )
    print(response.json())
    assert response.status_code == 422


# TEST GET API successful == PUT, GET, compare
def test_get_api():
    # PUT
    put_response = client.put(
        "/books/Percy Jackson and the Lightning Thief", json=book01
    )
    # assert put_response.status_code == 200

    # GET
    get_response = client.get("/books/Percy Jackson and the Lightning Thief")
    # assert get_response.status_code == 200

    # compares get_response with original book01
    assert get_response.json() == book01


# TEST DELETE API == PUT, GET-successful, DELETE, GET-404
def test_delete_api():
    # PUT
    put_response = client.put("/books/Eragon", json=book03)

    # GET - successful
    get_response = client.get("/books/Eragon")

    # compare get_response with original book03
    assert get_response.json() == book03

    # DELETE
    deleted_json = client.delete("/books/Eragon")

    # GET - item deleted
    get_response = client.get("/books/Eragon")
    assert get_response.status_code == 404


# test GET all books
def test_get_all_api():
    # PUT for 4 books
    put_response = client.put(
        "/books/Percy Jackson and the Lightning Thief", json=book01
    )
    put_response = client.put(
        "/books/Heroes of Olympus: the Lost Hero", json=book02
    )
    put_response = client.put("/books/Eragon", json=book03)
    put_response = client.put("/books/Eldest", json=book04)

    bookshelf01 = [book01, book02, book03, book04]

    # GET all
    response = client.get("/books/")  # returns a list of books
    response_data = response.json()

    for book in response_data:
        assert book in bookshelf01
