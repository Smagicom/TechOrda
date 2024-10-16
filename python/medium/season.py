date = input("Enter date: ")
if int(date[0])==0:
    if int(date[1]) <= 2:
        print("it is winter")
    elif int(date[1]) <= 5:
        print("it is spring")
    elif int(date[1]) <= 8:
        print("it is summer")
    else:
        print("it is autumn")
else:
    if int(date[1]) <= 1:
        print("it is autumn")
    else:
        print("it is winter") 
        