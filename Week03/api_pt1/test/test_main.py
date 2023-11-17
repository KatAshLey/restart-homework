#pytest
#looks for test_*.py files, and the functions that are test_*()
#unitests for tests with code, integration test for whole container testing

from fastapi.testclient import TestClient
from main import app

#unitest
def test_basic_example():
    assert True
    
client = TestClient(app)

def test_put_api():
    response = client.put("/items/jjn536156154",  json={
        "name": "Chewies",
        "quantity": 54351,
        "serial_num": "jjn536156154",
        "origin": {
            "country": "Ethiopia",
            "production_date": "16/09/1343"
        }
    })
    assert response.status_code==200