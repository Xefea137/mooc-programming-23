# Write your solution here
list = []
number = 1
while True:
    number = int(input("New item: "))
    if number == 0:
        break
    else:
        list.append(number)
        print(f"The list now: {list}")
        print(f"The list in order: {sorted(list)}")
print("Bye!")