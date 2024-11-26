# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.number = 0
        self.even = 0
        self.odd = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.number += number
        if number %2 == 0:
            self.even += number
        else:
            self.odd += number
        
    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        if self.numbers == 0:
            return 0
        return self.number

    def average(self):
        if self.numbers == 0:
            return 0
        return self.number/self.numbers

stats = NumberStats()
while True:
    number = int(input("Please type in integer numbers: "))
    if number == -1:
        break
    stats.add_number(number)

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {stats.even}")
print(f"Sum of odd numbers: {stats.odd}")


class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if not self.numbers:
            return 0.0
        else:
            return self.get_sum() / self.count_numbers()

stats = NumberStats()
even = NumberStats()
odd = NumberStats()
while True:
    number = int(input("Give a number: "))
    if number == -1:
        break

    stats.add_number(number)
    if number % 2 == 0:
        even.add_number(number)
    else:
        odd.add_number(number)

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())