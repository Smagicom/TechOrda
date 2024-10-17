def fibonachi(number:int):
    fib1=1
    fib2=1
    fibsum=1
    i=1
    while i<number:
        if fibsum==number:
            print("Данное число является числом из последовательности Фибоначчи")
            break
        elif fibsum<number:
            fibsum=fib1+fib2
            fib1=fib2
            fib2=fibsum
            i+=1
        else:
            print("Данное число НЕ является числом из последовательности Фибоначчи")
            break

fibonachi(13)