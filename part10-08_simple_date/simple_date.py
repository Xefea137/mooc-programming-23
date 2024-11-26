# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, date: int, month: int, year: int):
        self.__date = date
        self.__month = month
        self.__year = year

    def __eq__(self, another: "SimpleDate"):
        return (self.__date == another.__date) and (self.__month == another.__month) and (self.__year == another.__year)

    def __ne__(self, another: "SimpleDate"):
        return (self.__date != another.__date) or (self.__month != another.__month) or (self.__year != another.__year)

    def __gt__(self, another: "SimpleDate"):
        if self.__year > another.__year:
            return True
        elif self.__year == another.__year and self.__month > another.__month:
            return True
        elif self.__year == another.__year and self.__month == another.__month and self.__date > another.__date:
            return True
        else:
            return False

    def __lt__(self, another: "SimpleDate"):
        if self.__year < another.__year:
            return True
        elif self.__year == another.__year and self.__month < another.__month:
            return True
        elif self.__year == another.__year and self.__month == another.__month and self.__date < another.__date:
            return True
        else:
            return False

    def __add__(self, days: int):
        year = days//360
        month = (days%360)//30
        day = days%30

        if self.__date + day >= 30:
            day = (self.__date + day) - 30
            month += 1
        else:
            day = self.__date + day

        if self.__month + month >= 12:
            month = (self.__month + month) - 12
            year += 1
        else:
            month = self.__month + month

        year = self.__year + year
        
        return SimpleDate(day, month, year)

    def __sub__(self, another: "SimpleDate"):
        return abs(((self.__year - another.__year)*360) + ((self.__month - another.__month)*30) + (self.__date - another.__date))

    def __str__(self):
        return f"{self.__date}.{self.__month}.{self.__year}"

if __name__ == "__main__":
    sdate = SimpleDate(1, 5, 1878)

    print(sdate + 30)

class SimpleDate:

    def __init__(self, pv: int, month: int, year: int):
        self.__pv = pv
        self.__month = month
        self.__year = year

    def __str__(self):
        return f'{self.__pv}.{self.__month}.{self.__year}'

    def __value(self):
        return self.__year * 360 + self.__month * 30 + self.__pv

    def __to_date(self, days: int):
        months = days // 30
        years = months // 12
        days -= months * 30
        months -= years * 12
        return SimpleDate(days, months, years)

    def __lt__(self, other: "SimpleDate"):
        return self.__value() < other.__value()

    def __gt__(self, other: "SimpleDate"):
        return self.__value() > other.__value()

    def __eq__(self, other: "SimpleDate"):
        return self.__value() == other.__value()

    def __ne__(self, other: "SimpleDate"):
        return self.__value() != other.__value()

    def __add__(self, days_to_add: int):
        return self.__to_date(self.__value() + days_to_add)

    def __sub__(self, other: "SimpleDate"):
        return abs(self.__value() - other.__value())