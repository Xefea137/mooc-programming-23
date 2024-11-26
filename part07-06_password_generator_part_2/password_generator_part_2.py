# Write your solution here
import string
from random import choice
def generate_strong_password(length: int, n: bool, s: bool):
    special = "!?=+-()#"

    pwd = choice(string.ascii_lowercase)
    all = string.ascii_lowercase

    if n:
        pwd += choice(string.digits)
        all += string.digits

    if s:
        pwd += choice(special)
        all += special

    while len(pwd) < length:
        pwd += choice(all)

    return pwd

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(7, True, True))