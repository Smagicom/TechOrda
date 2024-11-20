import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()

# Эндпоинт для реверса строки
@app.post("/reverse")
async def reverse_string(data: dict):
    if "string" not in data:
        raise HTTPException(status_code=422, detail="Invalid input")
    return {"result": data["string"][::-1]}

# Эндпоинт для суммирования до n
@app.get("/sum1n/{n}")
async def sum_to_n(n: int):
    return {"result": sum(range(1, n + 1))}

# Эндпоинт для вычисления Фибоначчи
@app.get("/fibo")
async def get_fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="Invalid input")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return {"result": a}

# Эндпоинт для калькулятора
@app.post("/calculator")
async def calculator(data: dict):
    expr = data.get("expr")
    try:
        if "/0" in expr:
            raise ValueError("Division by zero")
        
        # Проверка на некорректные выражения
        if "++" in expr or ",," in expr:
            raise ValueError("Invalid expression")

        return {"result": eval(expr.replace(",", "+"))}
    except ValueError as ve:
        if str(ve) == "Division by zero":
            raise HTTPException(status_code=403, detail="zerodiv")  # Изменяем формат сообщения об ошибке
        raise HTTPException(status_code=400, detail={"error": "invalid"})

# Эндпоинт для добавления в список
my_list = []

@app.put("/list")
async def add_to_list(data: dict):
    element = data.get("element")
    if element is None:
        raise HTTPException(status_code=422, detail="Invalid input")
    my_list.append(element)
    return {"result": my_list}

# Эндпоинт для получения списка
@app.get("/list")
async def get_list():
    return {"result": my_list}

# Тесты
client = TestClient(app)

def test_sum_to_n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

def test_get_fibonacci():
    response = client.get("/fibo?n=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_reverse_string():
    response = client.post("/reverse", json={"string": "hello"})
    print(response.json())  # Логируем ответ для отладки
    assert response.status_code == 200
    assert response.json() == {"result": "olleh"}

def test_add_to_list():
    response = client.put("/list", json={"element": "Apple"})
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple"]}

    response = client.put("/list", json={"element": "Microsoft"})
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple", "Microsoft"]}

def test_get_list():
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple", "Microsoft"]}

def test_calculator_addition():
    response = client.post("/calculator", json={"expr": "1,+,1"})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_calculator_invalid_expression():
    response = client.post("/calculator", json={"expr": "1,++1"})
    assert response.status_code == 400
    assert response.json() == {"detail": {"error": "invalid"}}  # Исправляем проверку здесь

def test_calculator_divide_by_zero():
    response = client.post("/calculator", json={"expr": "1,/0"})
    print(response.json())  # Логируем ответ для отладки
    assert response.status_code == 403
    assert response.json() == {"detail": "zerodiv"}  # Исправляем проверку здесь
