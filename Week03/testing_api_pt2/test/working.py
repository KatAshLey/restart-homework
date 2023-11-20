""" # test PUT API
def test_put_api(client, good_book01):
    response = client.put("/books/test/", json=good_book01)
    assert response.status_code == 200 


# test PUT API unsuccessful
def test_put_api_unsuccessful(client, bad_book01):
    response = client.put("/books/test", json=bad_book01)
    assert response.status_code == 422


# test PUT then GET API
def test_put_get_api(client, good_book01):
    response = client.put("/books/test/", json=good_book01)
    assert response.status_code == 200
    response = client.get("books/test/")
    assert response.status_code == 200 and response.json() == good_book01 """
