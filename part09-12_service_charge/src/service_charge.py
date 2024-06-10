# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name_of_owner: str, account_number: int, balance: float):
        self.__name_of_owner = name_of_owner
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.__balance -= amount
            self.__service_charge()
        return "Insufficient balance"

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance -= (self.__balance/100)

if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)