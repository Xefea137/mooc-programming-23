# Write your solution here
def hash_square(length):
    width = length
    while length > 0:
        print(f"#" * width)
        length -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)