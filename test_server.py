from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_multiplication():
    response = client.get("http://127.0.0.1:8000/multiplication/{Num1}/{Num2}?num1=3&num2=4")
    assert response.status_code == 200
    assert response.json() == {"value1": 3, "value2": 4, "operation": "multiplication", "result": "12"}

def test_division():
    response = client.get("http://127.0.0.1:8000/division/{Num1}/{Num2}?num1=14&num2=-7")
    assert response.status_code == 200
    assert response.json() == {"value1": 14, "value2": -7, "operation": "division", "result": "-2.0"}

def test_multi_large_numbers():
    response = client.get("http://127.0.0.1:8000/multiplication/{Num1}/{Num2}?num1=2000000&num2=2")
    assert response.status_code == 400
    assert response.json() == {"detail": "Bad request. Numbers are too large."}

def test_division_by_zero():
    response = client.get("http://127.0.0.1:8000/division/{Num1}/{Num2}?num1=1&num2=0")
    assert response.status_code == 500
    assert response.json() == {"message": "Division by zero is not possible."}

def test_wrong_path():
    response = client.get("http://127.0.0.1:8000/divisionnnnnnnnn/{Num1}/{Num2}?num1=1&num2=1")
    assert response.status_code == 404
    assert response.json() == {"message": "Not found. The requested resource does not exist."}

def test_wrong_numbers():
    response = client.get("http://127.0.0.1:8000/division/{Num1}/{Num2}?num1=i&num2=1")
    assert response.status_code == 422
    assert response.json() == {"message": "Invalid numbers. The values must be an integer."}