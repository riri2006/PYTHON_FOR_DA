# Create a closure that remembers a username.
# def username(name):

#     def remember():
#         print(name)
#     return remember
# user1 = username("Vedantr")
# user2 = username("Rahul")

# user1()
# user2()


# Create a bank balance closure.Functions:deposit,withdraw,check balance
from os import name


def bank_balance(amount):
    def deposit():
        print(amount)
        return deposit
    def withdraw():
        print(amount)
        return withdraw
    def check_balance():
        print(amount)
        return check_balance
user = bank_balance(1000)
user.deposit()
user.withdraw()
user.check_balance()

# Create multiplier closure.
def power(x):
    def side(y):
        return x*y
    return side
double = power(2)
print(double(3))
print(double(4))
print(double(5))
print(double(6))
print(double(7))
print(double(8))
print(double(9))
print(double(10))
print(double(11))
print(double(12))
print(double(13))


# Create greeting closure.
def greeting(name):
        #    return f"hello,{name}"
    def clouser(surname):

     return f"hello {name} {surname}"
    return clouser
hello = greeting("veadnt")
print(hello("kapil"))

# Create tax calculator closure.
def tax(income):
    def calculate(money):
        return (income+money)/100
    return calculate
gst = tax(100)
print(gst(20))

# Create discount closure.
def discount(purchase):
    def calc(amount):
        return purchase - amount
    return calc
tax = discount(100)
print(tax(20))
print(discount(19)(5))
print(tax.__closure__)   # shows closure cells
print(tax.__closure__[0].cell_contents)    

# Create API key manager closure.
def api_manager(initial_key):
    api = initial_key   # outer variable, closure ke andar lock ho gaya

    def get_key():
        return api

    def set_key(new_key):
        nonlocal api     # outer variable ko update karne ke liye
        api = new_key

    def mask_key():
        return "***" + api[-4:]   # sirf last 4 characters dikhaye

    # bundle of functions return kar rahe hain
    return {
        "get": get_key,
        "set": set_key,
        "mask": mask_key
    }

# Example usage
manager = api_manager("ABC123456789")

print(manager["get"]())   # ABC123456789
manager["set"]("XYZ987654321")
print(manager["get"]())   # XYZ987654321
print(manager["mask"]())  # ***4321
