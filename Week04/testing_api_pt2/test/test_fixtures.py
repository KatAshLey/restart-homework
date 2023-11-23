from fastapi.testclient import TestClient
from main import app
import pytest
import json
from fastapi import FastAPI, HTTPException


# to reinitialize client app for each use
@pytest.fixture
def client():
    yield TestClient(app)
    #my_book_items_dict.clear()


# define good_book01-04, define bad_book01
@pytest.fixture
def good_book01():
    return {
        "name": "Percy Jackson and the Lightning Thief",
        "author": {"name": "Rick Riordan", "author_id": "RRIO-4358"},
        "year_published": 2005,
    }


@pytest.fixture
def good_book02():
    return {
        "name": "Heroes of Olympus: the Lost Hero",
        "author": {"name": "Rick Riordan", "author_id": "RRIO-4358"},
        "year_published": 2010,
    }


@pytest.fixture
def good_book03():
    return {
        "name": "Eragon",
        "author": {"name": "Christopher Paolini", "author_id": "CPAO-6455"},
        "year_published": 2002,
    }


@pytest.fixture
def good_book04():
    return {
        "name": "Eldest",
        "author": {"name": "Christopher Paolini", "author_id": "CPAO-6455"},
        "year_published": 2005,
    }


@pytest.fixture
def bad_book01():
    return {
        "name": "Percy Jackson and the Lightning Thief",
        "author": {"name": "dgrick Riordan", "author_id": "RRIO-4358"},
        "year_published": 2005,
    }


@pytest.mark.parametrize(
    "put_book, get_book, http_code01, http_code02",
    [
        ("good_book03", "good_book03", 200, 200),
        ("good_book04", "good_book02", 200, 404),
    ],
)
def test_many_put_get_api(
    put_book, get_book, http_code01, http_code02, client, request
):
    put_book_request = request.getfixturevalue(put_book)
    get_book_request = request.getfixturevalue(get_book)

    # is the page empty
    clear_page = client.get("/books/")
    clear_page_json = clear_page.json()
    print(clear_page_json)

    # put book in
    put_response = client.put(
        f"/books/{put_book_request['name']}/", json=put_book_request
    )
    print(f"/books/{put_book_request['name']}/")  # prints url correct /books/Eragon
    print(put_response.status_code)
    assert put_response.status_code == http_code01

    # get single book
    test = client.get("/books/")
    test_json = test.json()
    print(test_json)  # confirm its in the book list
    get_response = client.get(f"/books/{get_book_request['name']}/")
    print(get_response.status_code)
    assert get_response.status_code == http_code02


################################################################
# Anh's help
""" @pytest.mark.parametrize(
    "put_book, get_book, http_code01, expected_result",
    [
        ("good_book03", "good_book03", 200, "successful"),
        ("good_book04", "good_book03", 200, "not found"),
    ],
)
def test_many_put_get_api(
    put_book, get_book, http_code01, expected_result, client, request
):
    put_book_request = request.getfixturevalue(put_book)
    get_book_request = request.getfixturevalue(get_book)

    # put book in
    put_response = client.put(f"/books/{put_book}/", json=put_book_request)
    print(put_response.status_code)
    assert put_response.status_code == http_code01

    if expected_result == "successful":
        get_response = client.get(f"/books/{get_book}/")  # 200
        get_response = get_response.json()
    else:
        with pytest.raises(HTTPException) as excinfo:
            get_response = client.get(f"/books/{get_book}/")
        assert str(excinfo.value) == "File non_existent_file.txt not found" """
