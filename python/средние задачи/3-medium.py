def prost(number:int):
    i=2
    while i<number:
        if number%i==0:
            print("chislo NE prostoe")
            break   
        else:
            i+=1
    else:
        print("Chislo PROSTOE")

prost(257)