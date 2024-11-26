# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_lunch(self):
        if (self.balance - 2.60) >= 0:
            self.balance -= 2.60

    def eat_special (self):
        if (self.balance - 4.60) >= 0:
            self.balance -= 4.60

    def deposit_money(self, deposit: int):
        if deposit <= 0:
            raise ValueError("You cannot deposit an amount of money less than zero")
        self.balance += deposit

    def __str__(self):
        return f"The balance is {self.balance:.01f} euros"

Peter = LunchCard(20)
Grace = LunchCard(30)
Peter.eat_special()
Grace.eat_lunch()
print(f"Peter: {Peter}")
print(f"Grace: {Grace}")
Peter.deposit_money(20)
Grace.eat_special()
print(f"Peter: {Peter}")
print(f"Grace: {Grace}")
Peter.eat_lunch()
Peter.eat_lunch()
Grace.deposit_money(50)
print(f"Peter: {Peter}")
print(f"Grace: {Grace}")