# Write your solution here
list = []
i = 1
size = int(input("How many items: "))
while i <= size:
    number = int(input(f":Item {i}:"))
    list.append(number)
    i += 1
print(list)