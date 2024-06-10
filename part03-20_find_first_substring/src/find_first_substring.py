# Write your solution here
string = input("Please type in a word: ")
char = input("Please type in a character: ")

index = string.find(char)
if index != -1 and index+3 <= len(string):
    print(string[index:index+3])