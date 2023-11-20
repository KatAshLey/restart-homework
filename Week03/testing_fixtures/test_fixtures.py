from fastapi.testclient import TestClient
from main import app
import pytest


# everything we refer to client, it creates a new test client
@pytest.fixture
def client():
    yield TestClient(app)


# client = TestClient(app)

# fixture = precondition to test case. Pre initialization of an object and return it
# providing a matrix of inputs and receiving a matrix of outputs
# mock - black box testing, try not to use this


@pytest.fixture
def good_payload():
    return {
        "name": "Chocolate",
        "quantity": 551,
        "serial_num": "5155465",
        "origin": {"country": "Ethiopia", "production_date": "21/05/2038"},
    }


@pytest.fixture
def bad_payload():
    return {
        "name": "Chocolate",
        "quantity": 551,
        "serial_num": 54,
        "origin": {"country": "Ethiopia", "production_date": "21/05/2038"},
    }


def test_incorrect_input_put_api(client, bad_payload):
    response = client.put("/items/test/", json=bad_payload)
    assert response.status_code == 422


def test_get_api(client):
    response = client.get("/items/test/")
    assert response.status_code == 404


def test_put_then_get_api(client, good_payload):
    response = client.put("/items/test/", json=good_payload)
    assert response.status_code == 200
    response = client.get("/items/test")
    assert response.status_code == 200 and response.json() == good_payload


# allows to put through many test cases at once. parameter as string
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (5, -1, 4), (3, 3, 6)],
)
def test_addition(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize(
    "payload, http_code,",
    [
        (
            {
                "name": "Chocolate",
                "quantity": 551,
                "serial_num": "5155465",
                "origin": {"country": "Ethiopia", "production_date": "21/05/2038"},
            },
            200,
        ),
        (
            {
                "name": "Chocolate",
                "quantity": 551,
                "serial_num": 54,
                "origin": {"country": "Ethiopia", "production_date": "21/05/2038"},
            },
            422,
        ),
    ],
)
def test_many_put_apis(payload, http_code, client):
    assert client.put("/items/test/", json=payload).status_code == http_code


#parametrize with fixture
@pytest.mark.parametrize(
    "payload, http_code",
    [   ("good_payload", 200),
        ("bad_payload", 422),
    ],
)
def test_many_put_apis_request(payload, http_code, client, request):
    payload_request = request.getfixturevalue(payload)
    assert client.put("/items/test/", json=payload_request).status_code == http_code