# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.all_persons = []

    def add(self, person: Person):
        self.all_persons.append(person)

    def is_empty(self):
        if len(self.all_persons) > 0:
            return False
        return True

    def print_contents(self):
        total_hight = 0
        for item in self.all_persons:
            total_hight += item.height
        print(f"There are {len(self.all_persons)} persons in the room, and their combined height is {total_hight} cm")
        for item in self.all_persons:
            print(f"{item.name} ({item.height} cm)")

    def shortest(self):
        if self.is_empty():
            return None
        short_hight = self.all_persons[0]
        for item in self.all_persons:
            if short_hight.height > item.height:
                short_hight = item
        return short_hight

    def remove_shortest(self):
        if self.is_empty():
            return None
        shortest_person = self.shortest()
        self.all_persons.remove(shortest_person)
        return shortest_person
            
if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()

    #There are 4 persons in the room, and their combined height is 683 cm
    #Lea (183 cm)
    #Kenya (172 cm)
    #Nina (162 cm)
    #Ally (166 cm)

    #Removed from room: Nina

    #There are 3 persons in the room, and their combined height is 521 cm
    #Lea (183 cm)
    #Kenya (172 cm)
    #Ally (166 cm)

    '''room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()

    #Is the room empty? True
    #Shortest: None

    #Is the room empty? False
    #Shortest: Nina

    #There are 4 persons in the room, and their combined height is 683 cm
    #Lea (183 cm)
    #Kenya (172 cm)
    #Nina (162 cm)
    #Ally (166 cm)'''

    '''room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()

    #Is the room empty? True
    #Is the room empty? False
    #There are 5 persons in the room, and their combined height is 838 cm
    #Lea (183 cm)
    #Kenya (172 cm)
    #Ally (166 cm)
    #Nina (162 cm)
    #Dorothy (155 cm)'''