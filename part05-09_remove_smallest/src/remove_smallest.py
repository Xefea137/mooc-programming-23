# Write your solution here
def remove_smallest(numbers: list):
    small = sorted(numbers)     #smallest = min(numbers)
    numbers.remove(small[0])    #numbers.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)