def calc(balance:float,procent:float,srok:int):
    for i in range(srok):
        balance += balance*procent/100
    print(round(balance,2))
calc(1000,5,1)