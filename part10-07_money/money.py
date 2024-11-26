# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"

    def __eq__(self, another: "Money"):
        return self.__euros + self.__cents == another.__euros + another.__cents

    def __lt__(self, another: "Money"):
        return self.__euros + self.__cents < another.__euros + another.__cents

    def __gt__(self, another: "Money"):
        return self.__euros + self.__cents > another.__euros + another.__cents

    def __nt__(self, another: "Money"):
        return self.__euros + self.__cents != another.__euros + another.__cents

    def __add__(self, another: "Money"):
        return f"{(self.__euros + (self.__cents/100) + another.__euros + (another.__cents/100)):.2f} eur"

    def __sub__(self, another: "Money"):
        if (self.__euros + (self.__cents/100)) - (another.__euros + (another.__cents/100)) <= 0:
            raise ValueError("a negative result is not allowed")
        return f"{(self.__euros + (self.__cents/100)) - (another.__euros + (another.__cents/100)):.2f} eur"

if __name__ == "__main__":
    money1 = Money(4, 5)
    money2 = Money(5, 4)

    print(money1 == money2)