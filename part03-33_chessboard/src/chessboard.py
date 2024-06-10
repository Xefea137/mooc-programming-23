# Write your solution here
def chessboard(size):
    length = size
    i = 1
    while length > 0:
        width = size
        while width > 0:
            if i%2 != 0:
                print(1, end="")
            if i%2 == 0:
                print(0, end="")
            width -= 1
            i += 1
        if size %2 != 0:
            i += 2 
        else:
            i += 1
        print()
        length -= 1
# Testing the function
if __name__ == "__main__":
    chessboard(3)

'''
i = 1
while i <= size:
    if i %2 == 1:
        x = "10" * size
    else:
        x = "01" * size
    i += 1
    print(x[:size])
'''