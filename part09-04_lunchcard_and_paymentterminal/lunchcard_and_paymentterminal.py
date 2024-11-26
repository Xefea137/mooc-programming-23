# WRITE YOUR SOLUTION HERE:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0
        self.regular_price = 2.50
        self.special_price = 4.30

    def eat_lunch(self, payment: float):
        if payment >= self.regular_price:
            self.funds += self.regular_price
            self.lunches += 1
            return payment - self.regular_price
        return payment

    def eat_special(self, payment: float):
        if payment >= self.special_price:
            self.funds += self.special_price
            self.specials += 1
            return payment - self.special_price
        return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(self.regular_price):
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(self.special_price):
            self.specials += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        self.funds += amount
        card.deposit_money(amount)

if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

    #Card balance is 2 euros
    #Payment successful: False
    #Card balance is 102 euros
    #Payment successful: True
    #Card balance is 97.7 euros
    #Funds available at the terminal: 1100
    #Regular lunches sold: 0
    #Special lunches sold: 1

    '''exactum = PaymentTerminal()

    change = exactum.eat_lunch(10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_lunch_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

    #The change returned was 7.5
    #Payment successful: True
    #Payment successful: False
    #Payment successful: True
    #Funds available at the terminal: 1002.5
    #Regular lunches sold: 2
    #Special lunches sold: 1'''

    '''exactum = PaymentTerminal()

    change = exactum.eat_lunch(10)
    print("The change returned was", change)

    change = exactum.eat_lunch(5)
    print("The change returned was", change)

    change = exactum.eat_special(4.3)
    print("The change returned was", change)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

    #The change returned was 7.5
    #The change returned was 2.5
    #The change returned was 0.0
    #Funds available at the terminal: 1009.3
    #Regular lunches sold: 2
    #Special lunches sold: 1'''

    '''card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)

    #Balance 10
    #Payment successful: True
    #Balance 2
    #Payment successful: False
    #Balance 2'''