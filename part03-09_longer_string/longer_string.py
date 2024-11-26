# Write your solution here
word1 = input("Please type in string 1: ")
word2 = input("Please type in string 2: ")
length1 = len(word1)
length2 = len(word2)
if length1 > length2:
    print(f"{word1} is longer")
elif length2 > length1:
    print(f"{word2} is longer")
else:
    print("The strings are equally long")