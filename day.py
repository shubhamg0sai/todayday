from datetime import date
import time
import datetime 
today = date.today()

# Textual month, day and year    
d = today.strftime("%d,%B %Y")

# current weekday
a = datetime.datetime.today().weekday()
if a == 0:
    print("Monday",d)
elif a == 1:
    print("Tuesday",d)
elif a == 2:
    print(" Wednesday",d)
elif a == 3:
    print(" Thursday",d)
elif a ==4:
    print(" Friday",d)
elif a == 5:
    print(" Saturday",d)
elif a == 6:
    print("Sunday",d)
    

