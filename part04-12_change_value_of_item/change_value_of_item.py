# Write your solution here
index = 0
list = [1,2,3,4,5]
while True:
    index = int(input("Index: "))
    if index == -1:
        break
    if index < 0 or index >= len(list):
        continue
    else:
        value = int(input("New value: "))
        list[index] = value
        print(list)