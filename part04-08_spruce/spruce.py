# Write your solution here
def spruce(size):
    print("a spruce!")
    i = 1
    n = size - 1
    while n >= 0:
        print (" " * n + "*" * i)
        i += 2
        n -= 1
    print(" " * (size - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)