# Write your solution here
number = int(input("Please type in a number: "))
first = 1
last = number
while last > first:
    print(first)
    first += 1
    print(last)
    last -= 1

if last == first:
    print(last)