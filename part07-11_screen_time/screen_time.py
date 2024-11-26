# Write your solution here
from datetime import datetime, timedelta

file_name = input("Filename: ")
start = input("Starting date: ")
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")

user_date = datetime.strptime(start, "%d.%m.%Y")
user_date.strftime("%d.%m.%Y")

data_dict = {}
one_day = timedelta(days=1)
total_mins = 0

for i in range(days):
    data = input((f"Screen time {(user_date + i * one_day).strftime('%d.%m.%Y')}: "))
    data_dict[(user_date + i * one_day).strftime('%d.%m.%Y')] = data.split()

for key, value in data_dict.items():
    for items in value:
        total_mins += int(items)

with open(file_name, "w") as file:
    file.write(f"Time period: {user_date.strftime('%d.%m.%Y')}-{(user_date + (days-1) * one_day).strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total_mins}\n")
    file.write(f"Average minutes: {total_mins/days}\n")
    for key, value in data_dict.items():
        file.write(f"{key}: {value[0]}/{value[1]}/{value[2]}\n")

print("Data stored in file late_june.txt")