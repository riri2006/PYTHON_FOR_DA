def bank(balance):

    def account(amount):

        nonlocal balance

        balance += amount

        

    return account

user1 = bank(1000)

print(user1(500))
print(user1(-200))
print(user1(100))