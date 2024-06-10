# Write your solution here
string = input("Please type in a word: ")
sub_string = input("Please type in a substring: : ")
index = 0
occur = 0

while index < len(string) and occur < 2:
    if string[index:len(string)].find(sub_string) != -1:
        index += string[index:len(string)].find(sub_string)
        if index != -1:
            occur += 1
            index += len(sub_string)
    else:
        index += 1

if occur < 2:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {index-len(sub_string)}.")