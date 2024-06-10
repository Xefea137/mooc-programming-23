# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        max = 0
        for number in new_file:
            if int(number) > max:
                max = int(number)
    return max

if __name__ == "__main__":
    largest()