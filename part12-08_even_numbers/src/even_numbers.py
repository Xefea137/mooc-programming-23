# Write your solution here
def even_numbers(beginning: int, maximum: int):
    for item in range(beginning, maximum+1):
        if item %2 == 0:
            yield item

if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)

    print()

    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)