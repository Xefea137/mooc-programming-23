# Write your solution here
word = input("Please type in a string: ")
size = len(word)
second = word[1]
second_last = word[size-2]
if second == second_last:
    print(f"The second and the second to last characters are {second}")
else:
    print("The second and the second to last characters are different")