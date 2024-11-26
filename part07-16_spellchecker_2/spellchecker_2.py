# Write your solution here
from difflib import get_close_matches
def main():
    word_list = []

    with open("wordlist.txt") as file:
        for word in file:
            word_list.append(word.strip())

    text = input("Write text: ")
    error = []
    for word in text.split():
        if word.lower() in word_list:
            print(f"{word}", end=" ")
        else:
            print(f"*{word}*", end=" ")
            error.append(word)
    
    print("\nsuggestions:", end="")
    for word in error:
        print(f"\n{word}: {','.join(get_close_matches(word, word_list))}", end="")

main()