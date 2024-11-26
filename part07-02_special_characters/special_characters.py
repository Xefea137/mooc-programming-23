# Write your solution here
import string
def separate_characters(my_string: str):
    tup = ()
    asci = ""
    punct = ""
    other = ""
    for letter in range(len(my_string)):
        if my_string[letter] in string.ascii_letters:
            asci += my_string[letter]
        elif my_string[letter] in string.punctuation:
            punct += my_string[letter]
        else:
            other += my_string[letter]
    
    tup = (asci, punct, other)
    return tup

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])