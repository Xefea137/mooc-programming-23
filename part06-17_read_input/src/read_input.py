# Write your solution here
def read_input(r_i: str, n1: int, n2: int):
    while True:
        try:
            number = int(input(r_i))
            if number >= n1 and number <= n2:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {n1} and {n2}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)