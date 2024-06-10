# Write your solution here
list = []
while True:
    word = input("Word: ")
    list.append(word)
    if word in list[:len(list)-1]:
        break
print(f"You typed in {len(list)-1} different words")