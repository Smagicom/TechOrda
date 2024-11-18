from fastapi import FastAPI
from fastapi import Header, HTTPException
from pydantic import BaseModel
app=FastAPI()

elements = []

class Element_in(BaseModel):
    element:str

class Expression(BaseModel):
    expr: str  

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sum1n/{item}")
def sum_array(item:int):
    sum=0
    for i in range(item+1):
        sum+=i
    return {sum}

@app.get("/fibo/{number}")
def fibo(number:int):
    fib1, fib2 = 0, 1  
    for i in range(number - 1):  
        fib1, fib2 = fib2, fib1 + fib2
    return {fib2}

@app.post("/reverse")
def reverse_string(string:str=Header(...)):
    rev_str=string[::-1]
    return {rev_str}

@app.put("/list")
def add_element(item:Element_in):
    elements.append(item.element)

@app.get("/list")
def get_element():
    return {elements}

@app.post("/calculator")
def calculator(expression: Expression):
    try:
        num1, operator, num2 = expression.expr.split(',')
        num1, num2 = float(num1), float(num2)
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise HTTPException(status_code=403, detail="zerodiv")
            result = num1 / num2
        else:
            raise HTTPException(status_code=400, detail="invalid")
        
        return {"result": result}
    
    except ValueError:
        raise HTTPException(status_code=400, detail="invalid")
