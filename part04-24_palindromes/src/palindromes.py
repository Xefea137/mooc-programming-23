# Write your solution here
def palindromes(string: str):
    rev_string = string[::-1]
    return string == rev_string

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
while True:
    string = input("Please type in a palindrome: ")
    x = palindromes(string)
    if x == True:
        print(f"{string} is a palindrome!")
        break
    print("that wasn't a palindrome")
# block!