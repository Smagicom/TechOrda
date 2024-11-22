from main import FastAPI, Response, status
from prometheus_client import Counter, Histogram, Gauge, generate_latest, REGISTRY
from prometheus_client.exposition import basic_auth_handler
import time

app=FastAPI()

REQUESTS = Counter('http_requests_total', 'Number of HTTP requests received', ['endpoint', 'method'])

REQUEST_LATENCY = Histogram('http_requests_milliseconds', 'Duration of HTTP requests in milliseconds', ['endpoint', 'method'], buckets=[0.1, 0.3, 0.5, 1, 2, 5, 10])

LAST_VALUE_SUM1N = Gauge('last_sum1n', 'Value stores last result of sum1n')

LAST_VALUE_FIBO = Gauge('last_fibo', 'Value stores last result of fibo')

LAST_SIZE = Gauge('last_size', 'Value stores current list size')

LAST_CALCULATOR = Gauge('last_calculator', 'Value stores last result of calculator')

ERRORS_CALCULATOR = Counter('errors_calculator_total', 'Number of errors in calculator')

@app.get("/")
async def root():
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/', method='HTTP').inc()
    return {"message": duration}

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(REGISTRY), media_type="text/plain")

@app.get("/sum1n/{item}")
def sum1n(item):
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/sum1n', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/sum1n', method='HTTP').inc()
    result = 0
    i = 1
    while i <= int(item):
        result += i
        i += 1
    LAST_VALUE_SUM1N.set(result)
    return {"result": result}

@app.get("/fibo/")
def fibo(n: int = 0):
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/fibo', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/fibo', method='HTTP').inc()
    fibon = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    LAST_VALUE_FIBO.set(fibon[int(n)-1])
    return {"result": fibon[int(n)-1]}

@app.post("/reverse")
def reverse(item:str):
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/reverse', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/reverse', method='HTTP').inc()
    word = item [::-1]
    return {"reversed word":word}

ary = []
@app.put("/list")
def list(item:str):
    ary.append(item)
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/list', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/list', method='HTTP').inc()
    LAST_SIZE.set(len(ary))
    return {"result":ary}

@app.get("/list")
def list():
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/list', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/list', method='HTTP').inc()
    return {"result":ary}

@app.post("/calculator")
def calc(item:str, response: Response):
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/calculator', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/hello', method='HTTP').inc()
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
            LAST_CALCULATOR.set(int(num1_arr)+int(num2_arr))
            return {"result":(int(num1_arr)+int(num2_arr))}
        elif oper == "-":
            LAST_CALCULATOR.set(int(num1_arr)-int(num2_arr))
            return {"result":(int(num1_arr)-int(num2_arr))}
        elif oper == "*":
            LAST_CALCULATOR.set(int(num1_arr)*int(num2_arr))
            return {"result":(int(num1_arr)*int(num2_arr))}
        elif oper == "/":
            if int(num2_arr)==0:
                response.status_code = status.HTTP_403_FORBIDDEN
                ERRORS_CALCULATOR.inc()
                return{"error": "zerodiv"}
            else:
                LAST_CALCULATOR.set(int(num1_arr)/int(num2_arr))
                return{"result":(int(num1_arr)/int(num2_arr))}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            ERRORS_CALCULATOR.inc()  
            return{"error": "invalid"}
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
        ERRORS_CALCULATOR.inc()    
        return{"error":"invalid"}
    
@app.get("/hello")
def hello():
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/hello', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/hello', method='HTTP').inc()
    return {"hello":"world"}

@app.post("/create")
def create(item:int):
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/create', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/create', method='HTTP').inc()
    return {"newitem":item}

@app.get("/new/{item}/{item2}")
def new(item,item2):
    start_time = time.time()
    duration = start_time/1000000000
    REQUEST_LATENCY.labels(endpoint='/new', method='HTTP').observe(duration)
    REQUESTS.labels(endpoint='/new', method='HTTP').inc()
    return {"new":item,
            "new2":item2}