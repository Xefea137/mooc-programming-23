# Write your solution here
import string
from random import shuffle
def generate_password(length: int):
    pwd = ""
    letters = list(string.ascii_lowercase)
    shuffle(letters)
    for item in range(length):
        pwd += letters[item]
    return pwd

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))