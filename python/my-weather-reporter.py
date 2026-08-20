city = input("Enter the city name: ")
temp = float(input("Enter the temperature in Celsius: "))
if temp > 30:
    print("It's a hot day in", city)
if temp > 25:
    print("It's a golden day in", city)
else:
    print("Grab a jacket before you go outside")
if temp > 35:
    print("Scorching hot day! ")
elif temp > 15:
    print("Cold weather - Stay warm!")

import datetime
import calendar
now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)
print(calendar.calendar(now.year))