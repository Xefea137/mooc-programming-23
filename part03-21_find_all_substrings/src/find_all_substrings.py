# Write your solution here
string = input("Please type in a word: ")
char = input("Please type in a character: ")

index = 0
while index < len(string):
    if string[index] == char and index+3 <= len(string):
        print(string[index:index+3])
    index += 1