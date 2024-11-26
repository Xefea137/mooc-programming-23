# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__item_list = []

    def add_item(self, item: Item):
        if (self.__max_weight - item.weight()) >= 0:
            self.__item_list.append(item)
            self.__max_weight -= item.weight()

    def print_items(self):
        for item in self.__item_list:
            print(item)

    def weight(self):
        total_weight = 0
        for item in self.__item_list:
            total_weight += item.weight()
        return total_weight

    def heaviest_item(self):
        weight = 0
        for item in self.__item_list:
            if item.weight() > weight:
                weight = item.weight()
                heaviest_item = item

        return heaviest_item

    def __str__(self):
        if len(self.__item_list) == 1:
            return f"{len(self.__item_list)} item ({self.weight()} kg)"
        return f"{len(self.__item_list)} items ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcase_list = []

    def add_suitcase(self, suitcase_item: Suitcase):
        if self.__max_weight - suitcase_item.weight() >= 0:
            self.__suitcase_list.append(suitcase_item)
            self.__max_weight -= suitcase_item.weight()

    def print_items(self):
        for suitcase in self.__suitcase_list:
            if suitcase.print_items() != None:
                print(suitcase.print_items())

    def __str__(self):
        if len(self.__suitcase_list) == 1:
            return f"{len(self.__suitcase_list)} suitcase, space for {self.__max_weight} kg"    
        return f"{len(self.__suitcase_list)} suitcases, space for {self.__max_weight} kg"

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()