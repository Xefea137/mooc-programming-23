# WRITE YOUR SOLUTION HERE:
def remove_smaller_than(numbers: list, limit: int):
    return [x for x in numbers if x >= limit]

if __name__ == "__main__":
    numbers = [1,65, 32, -6, 9, 11]
    print(remove_smaller_than(numbers, 10))
    print(remove_smaller_than([-4, 7, 8, -100], 0))