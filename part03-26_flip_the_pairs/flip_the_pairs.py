# Write your solution here
number = int(input("Please type in a number: "))
x = 2
while x <= number:
    if x %2 == 0:
        print(x)
        x -= 1
    if x %2 != 0:
        print(x)
        x += 3
if number %2 !=0:
    print(number)