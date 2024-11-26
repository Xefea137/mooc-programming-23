# Write your solution here
word = input("Please type in a string: ")
size = len(word)
while size > 0:
    size -= 1
    print(word[size:])