# Write your solution here
sentence = input("Please type in a sentence: ")
index = 0
sentence = " " + sentence
while index < len(sentence):
    if sentence[index] == " ":
        print(sentence[index+1:index+2])
    index += 1