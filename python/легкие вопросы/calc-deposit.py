def calculate_deposit(n, k, b):
    monthly_rate = k / 100
    balance = b
    
    for _ in range(n):
        balance += balance * monthly_rate
    
    return round(balance)

n, k, b = map(int, input().split())

result = calculate_deposit(n, k, b)

print(result)
