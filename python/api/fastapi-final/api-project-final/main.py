from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/sum1n/{n}")
async def read_root(n):
    n = int(n)
    res = 0
    for i in range(n):
        res += i
    return {"result": res}


@app.get("/fibo")
async def fibnums(n):
    n = int(n)
    if n <= 0:
        return "Please enter the number bigger 0!"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range (2, n):
            a, b = b, a + b
        return JSONResponse(content={"result": b})
    


@app.post("/reverse")
async def revers_word(string: str = Header(...)):
    return {"result": string[::-1]}



element_list = []
# Pydantic model
class ElementItem(BaseModel):
    element: str

@app.put("/list/")
async def create_item(item: ElementItem):
    element_list.append(item.element)
    return {"message": f"Item '{item.element}' updated successfully!"}

@app.get("/list/")
async def get_list():
    return {"result": element_list}
    




class ElementItem(BaseModel):
    expr: str

@app.post("/calculator/")
async def calc(item: ElementItem):
    operands = item.expr.split(",")
    num1 = float(operands[0])  
    operator = operands[1]  
    num2 = float(operands[2])
    
    match operator:
        case "+":
            res = num1 + num2
        case "-":
            res = num1 - num2
        case "/":
            if num2 == 0:
                return "Division by zero is not allowed." 
            res = num1 / num2
        case "*":
            res = num1 * num2
        
    return { "result": res } 