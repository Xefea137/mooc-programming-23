# Write your solution here
from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    pool = list(range(lower,upper+1))
    return sorted(sample(pool,amount))

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)