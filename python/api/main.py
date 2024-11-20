from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
elements: List[str] = []
class Element(BaseModel):
    element: str
class Expression(BaseModel):
    expr: str
@app.get("/sum1n/{n}")
async def sum_to_n(n: int):
    result = sum(range(1, n + 1))
    return {"result": result}

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@app.get("/fibo")
async def get_fibonacci(n: int):
    result = fibonacci(n)
    return {"result": result}

@app.post("/reverse")
async def reverse_string(string: str):
    reversed_string = string[::-1]
    return {"result": reversed_string}

@app.api_route("/list", methods=["GET", "PUT"])
async def handle_list(element: Element = None):
    if element:
        elements.append(element.element)  
        return {"result": elements}
    return {"result": elements}  

def calculate_expression(expression: str):
    try:
        num1, operator, num2 = expression.split(',')
        num1 = float(num1)
        num2 = float(num2)
        
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError
            return num1 / num2
        else:
            raise ValueError("Invalid operator")
    except ValueError:
        raise ValueError("Invalid expression format")

@app.post("/calculator")
async def calculator(expression: Expression):
    try:
        result = calculate_expression(expression.expr)
        return {"result": result}
    except ValueError:
        raise HTTPException(status_code=400, detail={"error": "invalid"})
    except ZeroDivisionError:
        raise HTTPException(status_code=403, detail={"error": "zerodiv"})
