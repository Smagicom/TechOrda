from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sum1n():
    n = 5
    response = client.get(f"/sum1n/{n}")
    assert response.status_code == 200
    assert response.json() == {"result": 10}

def test_fibo():
    n = 5
    response = client.get(f"/fibo?n={n}")
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_reverse():
    w = "hello"
    response = client.post(f"/reverse", headers={"string": w})
    assert response.status_code == 200
    assert response.json() == {"result": "olleh"}

def test_list_add():
    json_data = {"element": "Apple"}
    response = client.put(f"/list", json=json_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Item 'Apple' updated successfully!"}

def test_list_show():
    response = client.get(f"/list")
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

def test_calculator():
    json_data = {"expr": "1,+,1"}
    response = client.post(f"/calculator", json=json_data)
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}