# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self, km: int):
        if km > self.__petrol:
            km = self.__petrol
        self.__odometer += km
        self.__petrol -= km

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"

if __name__ == "__main__":
    car = Car()
    print(car)              #Car: odometer reading 0 km, petrol remaining 0 litres
    car.fill_up()
    print(car)              #Car: odometer reading 0 km, petrol remaining 60 litres
    car.drive(20)
    print(car)              #Car: odometer reading 20 km, petrol remaining 40 litres
    car.drive(50)
    print(car)              #Car: odometer reading 60 km, petrol remaining 0 litres
    car.drive(10)
    print(car)              #Car: odometer reading 60 km, petrol remaining 0 litres
    car.fill_up()
    car.fill_up()
    print(car)              #Car: odometer reading 60 km, petrol remaining 60 litres