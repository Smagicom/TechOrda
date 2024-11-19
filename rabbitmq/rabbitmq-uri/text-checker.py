SOL=[
    "amqp://app-developer:9cDtdMTj@localhost:5672/application",
    "amqp://app-developer:9cDtdMTj@localhost/application",
]
def check(reply):
    return reply in SOL
