# Write your solution here
number = int(input("Please type in a number: "))
new_number = number
if number < 0:
    new_number = number*-1
print(f"The absolute value of this number is {new_number}")