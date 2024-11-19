from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

global_list = []

@app.get("/sum1n/{n}")
def sum1n(n: int):
    return {"result": sum(range(1, n+1))}

@app.get("/fibo")
def fibo(n: int):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return {"result": fib[n-1]}

@app.post("/reverse")
def reverse(string: str = Header(...)):
    return {"result": string[::-1]}

class Element(BaseModel):
    element: str

@app.put("/list")
def add_to_list(item: Element):
    global_list.append(item.element)
    return {"result": global_list}

@app.get("/list")
def get_list():
    return {"result": global_list}

class Expression(BaseModel):
    expr: str

@app.post("/calculator")
def calculator(expr: Expression):
    try:
        num1, operator, num2 = expr.expr.split(",")
        num1, num2 = int(num1), int(num2)

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise HTTPException(status_code=403, detail="zerodiv")
            result = num1 / num2
        else:
            raise HTTPException(status_code=400, detail="invalid")
        
        return {"result": result}
    except:
        raise HTTPException(status_code=400, detail="invalid")

