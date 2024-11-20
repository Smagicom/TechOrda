import datetime
now=datetime.datetime.now()
print (now.strftime("%d.%m.%Y"))
def datenow(datein:str):
    if datein[0]+datein[1]==now.strftime("%d") and datein[3]+datein[4]==now.strftime("%m") and datein[6]+datein[7]+datein[8]+datein[9]==now.strftime("%Y"): 
        print ("вы верно ввели текущую дату")
    else:
        print("вы ввели текущую дату НЕ верно")
datenow("15.10.2024")