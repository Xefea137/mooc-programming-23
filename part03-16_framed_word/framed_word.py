# Write your solution here
word = input("Word: ")
word_size = len(word)
size = int((28 - len(word)) / 2)
odd_size = size+1
print("*" * 30)
if word_size%2==0:
    print(f"*" + " " * size + word + " " * size + "*")
else:
    print(f"*" + " " * size + word + " " * odd_size + "*")
print("*" * 30)