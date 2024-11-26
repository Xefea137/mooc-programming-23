# Write your solution here
word = input("Please type in a string: ")
size = len(word)
while size > 0:
    print(word[size-1])
    size -= 1