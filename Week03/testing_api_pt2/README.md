Based off homework 1(modules) or 2 (pydantics)

1) Setup your unit testing structure
eg:
- create your 'tests' folder on the same level as your main.py file
- create your 'test_main.py' file to begin testing
- make sure you import 'app' from 'main.py'
-you need to create a test client 'client = TestClient(app)' by import from fastapi.testclient import TestClient'
- for each of the test functions you write, you should follow 'def test_****():'

2) Test your PUT API to give 200 response when you give a correct body input

3) Test your PUT API will give 400 response code when you give an incorrect input body format

4) Test your GET API to return a good body
- first you need to give a PUT API
- then you need to call the GET API
- compare the request body of the PUT API with the response body of GET API
    - either compare casted string of the json()
    - or some other method to compare key value pairs

5) Test your DELETE API
make sure you get 404 to confirm that the Item is not found(deleted)
- put get delete get

6) Test your GET ALL API
