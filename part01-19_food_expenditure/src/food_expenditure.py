# Write your solution here
cafeteria = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
groceries = float(input("How much money do you spend on groceries in a week? "))

weekly = ((cafeteria*price)+groceries)
daily = weekly/7

print("Average food expenditure: ")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")