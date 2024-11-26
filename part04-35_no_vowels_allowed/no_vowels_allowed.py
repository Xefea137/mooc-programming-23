# Write your solution here
def no_vowels(string: str):
    nstring = ""
    for char in string:
        if char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
            nstring += char
    return nstring

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))