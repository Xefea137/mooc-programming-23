# Write your solution here
list = []
print(f"The list is now {list}")
choice = ""
i = 0
while choice != "x":
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d":
        i += 1
        list.append(i)
        print(f"The list is now {list}")
    elif choice == "r":
        if i == 0:
            continue
        else:
            list.pop(i-1)
            i -= 1
        print(f"The list is now {list}")
print("Bye!")