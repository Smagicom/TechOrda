date = input("Enter date: ")
if date[2] == "." and date[5] == "." and int(date[0])*10+int(date[1]) <=31 and (int(date[3])*10+int(date[4])) <= 12 and int(date[6])*1000+int(date[7])*100+int(date[8])*10+int(date[9]) <= 2024:
   print("You entered correct date")
else:
   print("You entered incorrect date")
