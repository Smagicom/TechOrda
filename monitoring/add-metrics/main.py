from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, Gauge, make_asgi_app
import time

# Инициализация приложения FastAPI
app = FastAPI()

# Определение метрик
http_requests_total = Counter(
    'http_requests_total', 'Number of HTTP requests received', ['method', 'endpoint']
)
http_requests_milliseconds = Histogram(
    'http_requests_milliseconds', 'Duration of HTTP requests in milliseconds', ['method', 'endpoint']
)
last_sum1n = Gauge('last_sum1n', 'Value stores last result of sum1n')
last_fibo = Gauge('last_fibo', 'Value stores last result of fibo')
last_calculator = Gauge('last_calculator', 'Value stores last result of calculator')
errors_calculator_total = Counter(
    'errors_calculator_total', 'Number of errors in calculator'
)

# Middleware для отслеживания запросов
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    method = request.method
    endpoint = request.url.path
    http_requests_total.labels(method=method, endpoint=endpoint).inc()

    try:
        response = await call_next(request)
    except Exception as e:
        if endpoint == "/calculator":
            errors_calculator_total.inc()
        raise e
    finally:
        duration = (time.time() - start_time) * 1000
        http_requests_milliseconds.labels(method=method, endpoint=endpoint).observe(duration)

    return response

# Обработчики запросов
@app.get("/sum1n")
def sum1n(n: int):
    result = sum(range(1, n + 1))
    last_sum1n.set(result)
    return {"result": result}

@app.get("/fibo")
def fibo(n: int):
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    result = fibonacci(n)
    last_fibo.set(result)
    return {"result": result}

@app.get("/calculator")
def calculator(operation: str, a: float, b: float):
    try:
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                raise ZeroDivisionError
            result = a / b
        else:
            raise ValueError("Invalid operation")
        last_calculator.set(result)
        return {"result": result}
    except (ValueError, ZeroDivisionError) as e:
        errors_calculator_total.inc()
        return {"error": str(e)}

# Настройка Prometheus Exporter
from starlette.middleware import Middleware
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)
