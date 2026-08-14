class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):

        self.amount = amount
        if amount > 0:
            self.__balance += amount


    def withdraw(self, amount):

        if amount > 0 and amount < self.__balance:
            self.__balance -= amount

        

    def get_balance(self):

        return self.__balance


account = BankAccount(5000)

account.deposit(1000)
account.withdraw(2000)

print(account.get_balance())