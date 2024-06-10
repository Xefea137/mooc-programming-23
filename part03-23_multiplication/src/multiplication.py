# Write your solution here
number = int(input("Please type in a number: "))
x = 1
while x <= number:
    i = 1
    while i <= number:
        print(f"{x} x {i} = {x * i}")
        i += 1
    x += 1