from datetime import datetime,timedelta
now=datetime.now()
print(now)

# dt=datetime(2025,8,1,10,50)
# print(dt)

#  time delta:

# delta=timedelta(days=5,hours=3)
# print(delta)

# future=datetime.now()-timedelta(days=5)
# print(future)

# full date:
print("full date:", now.strftime("%Y-%B-%d"))
# full date and time:
print("date&time:",now.strftime("%Y-%m-%d %H:%M:%S"))

# weekday name and short name:
print("full weekday name:",now.strftime("%A"))

# short weekday name:
print("short weekday name:",now.strftime("%a"))

# month name and short format:
print("month name:",now.strftime("%B"))
print("month number:",now.strftime("%m"))


# task:

import datetime

def get_day(date):
   
    d = datetime.datetime.strptime(date, "%Y-%m-%d")
    
    return d.strftime("%A")


print(get_day("2025-07-01"))  

# task 2:
import datetime

hours = int(input("Enter hours: "))

now = datetime.datetime.now()

later = now + datetime.timedelta(hours=hours)

print("Your next notification will be at:", later.strftime("%I:%M %p on %A"))



