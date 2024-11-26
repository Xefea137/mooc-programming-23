# Write your solution here
number = 1
total = 1
calculation = "The consecutive sum: 1"
limit = int(input("Limit"))
while total < limit:
    number += 1
    calculation += f" + {number}"
    total += number

calculation += f" = {total}"
print(calculation)