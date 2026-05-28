
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, kharcha):
        self.balance = self.balance - kharcha
        print(f"{self.balance}, {self.name}")
    
    def withdraw(self, amount):
        print(f"{self.balance}")
    
    def check_balance(self):
        print(f"{self.balance}")

s1 = BankAccount("heera", 1000)
s1.deposit(200000)
s1.withdraw(300000)
s1.check_balance()
