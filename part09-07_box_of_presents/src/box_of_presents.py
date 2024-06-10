# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight})"

class Box:
    def __init__(self):
        self.gifts = []

    def add_present(self, present: Present):
        self.gifts.append(present)

    def total_weight(self):
        total = 0
        for gift in self.gifts:
            total += gift.weight
        return total

if __name__ == "__main__":
    '''book = Present("ABC Book", 2)

    print("The name of the present:", book.name)        #The name of the present: ABC Book
    print("The weight of the present:", book.weight)    #The weight of the present: 2
    print("Present:", book)                             #Present: ABC Book (2 kg)  '''

    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())