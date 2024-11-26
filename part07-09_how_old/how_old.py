# Write your solution here
from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
age = (datetime(1999, 12, 31) - datetime(year, month, day)).days

if age >= 0:
    print(f"You were {age} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")