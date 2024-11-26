# Write your solution here
while True:
    number = int(input("Please type in a number: : "))
    factorial = 1
    x = number
    if number <= 0:
        break
    while number > 0:
        factorial *= number
        number -= 1 
    print(f"The factorial of the number {x} is {factorial}")
print("Thanks and bye!")