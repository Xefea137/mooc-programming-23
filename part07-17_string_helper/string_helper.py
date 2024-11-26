# Write your solution here
from string import ascii_letters, whitespace, digits
def change_case(orig_string: str):
    new = ""
    for letter in orig_string:
        if letter.isupper():
            new += letter.lower()
        elif letter.islower():
            new += letter.upper()
        else:
            new += letter

    return new

def split_in_half(orig_string: str):
    p1 = orig_string[:len(orig_string)//2]
    p2 = orig_string[len(orig_string)//2:]

    return p1, p2

def remove_special_characters(orig_string: str):
    new = ""
    for letter in orig_string:
        if letter in ascii_letters or letter in whitespace or letter in digits:
            new += letter

    return new

if __name__ == "__main__":
    #my_string  = "Well hello there!"
    #my_string  = "This is a test, lets see how it goes!!!11!"
    my_string  = "Thi§ is a test: test?"
    print(change_case(my_string))
    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)
    print(remove_special_characters(my_string))