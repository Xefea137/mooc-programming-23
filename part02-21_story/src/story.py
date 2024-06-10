# Write your solution here
story = ""
previous_word = ""
while True:
    word = input("Please type in a word: ")
    if previous_word == word:
        break
    elif word == "end":
        break
    previous_word = word
    story = story + word + " "

print(story)