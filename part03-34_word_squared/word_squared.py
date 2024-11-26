# Write your solution here
def squared(word, size):
    i = 1
    row = ""
    while i <= size:
        # row = word * size
        row = word * size
        print(row[0:size])
        row = row[size:] * size
        i += 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)