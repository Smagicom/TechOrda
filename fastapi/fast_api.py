from fastapi import FastAPI, Response, status

app=FastAPI()

@app.get("/sum1n/{item}")
def sum1n(item):
    result = 0
    i = 1
    while i <= int(item):
        result += i
        i += 1
    return {"result": result}

@app.get("/fibo/")
def fibo(n: int = 0):
    fibon = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    return {"result": fibon[int(n)-1]}

@app.post("/reverse")
def reverse(item:str):
    word = item [::-1]
    return {"reversed word":word}

ary = []
@app.put("/list")
def list(item:str):
    ary.append(item)
    return {"result":ary}

@app.get("/list")
def list():
    return {"result":ary}

@app.post("/calculator")
def calc(item:str, response: Response):
    ind = []

    for i in range(len(item)):
        if item[i] == ",":
            ind.append(i)

    num1_arr = ""
    num2_arr = ""
    oper=item[ind[0]+1]

    for i in range(ind[0]):
        num1_arr =num1_arr + item[i]


    for i in range(ind[1]+1, len(item), 1):
        num2_arr = num2_arr + item[i]

    if len(ind) == 2 and num1_arr.isnumeric() == True and num2_arr.isnumeric() == True:
        if oper == "+":
            return {"result":(int(num1_arr)+int(num2_arr))}
        elif oper == "-":
            return {"result":(int(num1_arr)-int(num2_arr))}
        elif oper == "*":
            return {"result":(int(num1_arr)*int(num2_arr))}
        elif oper == "/":
            if int(num2_arr)==0:
                response.status_code = status.HTTP_403_FORBIDDEN
                return{"error": "zerodiv"}
            else:
                return{"result":(int(num1_arr)/int(num2_arr))}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST  
            return{"error": "invalid"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST    
        return{"error":"invalid"}
    
@app.get("/hello")
def hello():
    return {"hello":"world"}

@app.post("/create")
def create(item:int):
    return {"newitem":item}

@app.get("/new/{item}/{item2}")
def new(item,item2):
    return {"new":item,
            "new2":item2}