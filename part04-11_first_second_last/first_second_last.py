# Write your solution here
def first_word(string):
    index = string.find(" ")
    return (string[:index])

def second_word(string):
    index1 = string.find(" ")
    index2 = string[index1+1:].find(" ") + index1 + 1
    if index1 == index2:
        return (string[index1+1:])
    else:
        return (string[index1+1:index2])

def last_word(string):
    index = len(string)-1
    while string[index] != " ":
        index -= 1
    return (string[index+1:])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(second_word("first second"))
    print(second_word("once upon a time there was a programmer"))
    print(last_word(sentence))