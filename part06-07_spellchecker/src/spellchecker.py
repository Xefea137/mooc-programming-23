# write your solution here
def main():
    text = input("Write text: ")
    # text = "We use ptython to make a spell checker"
    # text = "This is acually a good and usefull program"

    word_list = []
    with open("wordlist.txt") as file:
        for word in file:
            word_list.append(word.strip())

    text_list = []
    start = 0
    for item in range(len(text)):
        if text[item] == " " or item == len(text)-1:
            end = item
            text_list.append(text[start:end+1].strip())
            start = end+1

    for word in text_list:
        if word.lower() in word_list:
            print(word, end=" ")
        else:
            print(f"*{word}*", end=" ")
    
main()