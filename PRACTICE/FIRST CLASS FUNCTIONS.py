# def naam(name="vedant", age=21):

#     new_name = input("Enter name (press enter for default): ")
#     new_age = input("Enter age (press enter for default): ")

#     if new_name:
#         name = new_name

#     if new_age:
#         age = int(new_age)

#     print(name)
#     print(age)

#     return name, age


# print(naam())



# Create a function using keyword arguments.

# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # Calling the function with keyword arguments
# student_info(name="Rahul", age=21, roll_no = 122, course="Python")


# def greet(greeting, **kwargs):
#     print(greeting)
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")

# greet("Hello", name="Amit", city="Mumbai")


# def hum(vedrid , **kwargs):
#     print(vedrid)
#     for k, c in kwargs.items():
#         print(f"{k} = {c}")

# hum("vedant", name ="vedant", rollno = 36, age = 21, course = "python")



# def calcate(*args):
#     total = 0
#     for i in args:
#         total = total + i
        
#     return total
        
# print(calcate(1,2,3,4,5,6,7,8,9))
# print(calcate(1,2,3))
# print(calcate(1,2))
# print(calcate(1))


# # Create a function using **kwargs Print all student details.
# def pra(**kwargs):
#     for k , v in kwargs.items():
#         print(f"{k} = {v}")

# pra(name = "vedant", age = 21, course = "python")




# Create a function using both *args and **kwargs
# def mojmasti(*args,**kwargs):
#     for i in args:
#         print(i)
#     for k , v in kwargs.items():
#         print(f"{k} = {v}")

        
# mojmasti(1,2,3,4,5, name = "vedant", age = 21, course = "python")
       

# # Pass hello function to another function.
# def hello(name):
#     return f"hello,{name}"

# def pas1(fun,bela):
#     return fun(bela)

# reult = pas1(hello,"vedant")
# print(reult)


# LEVEL 1
# def outer(name):
    
#     def inner():
#         print(f"Hello {name}")
    
#     return inner

# x = outer("vedant")

# x()


# def outer():
#     def inner():
#         print("Hello from inner!")
#     return inner

# outer()() 

# # next
# def task(func):
#     def wrapper():
#         func()
#         print("vedant")
#     return wrapper    
# @task
# def inner():
#     print("hello")

# inner()
  

# # LEVEL 4 TASK Now create TWO functions
# def outer(name):
#     def inner():
#         print(name)
#     return inner
# english = outer("hello")
# hindi = outer("namaste")
# english()
# hindi()

# Score Generator Fail at 45 Pass at 90
from re import sub


def marks(n):
    
    def status():
    

       if n < 45:
        print("fail")          # agar n 45 se chhota hai
       elif n > 90:
        print("pass")          # agar n 90 se bada hai
       else:
        print("average")       # agar n 45–90 ke beech hai


    return status
check = marks(45) 
wow = marks(90)
check()
wow()


# Multiplier Machine . Double
def machine(x):
  def multi(y):
    return y*x
  return multi
double = machine(2)

print(double(10))


# Triple
def machine(x):
  def multi(y):
    return y*x
  return multi
double = machine(2)
triple = machine(3)

print(triple(5))


# LEVEL 8 and 9 TASK Create a power machine
def power(x):
  def expo(y):
    return y**x
  return expo
square = power(2)
cube = power(3)
print(square(4))
print(cube(3))

def outer():

    x = 100

    def inner():
        print(x)

    return inner

a = outer()

a()


def counter():
    count = 0
    def counting():
      nonlocal count
      
      count += 1
      return count
    return counting
a = counter()
print(a())
print(a())
print(a())
print(a())
print(a())
print(a())
print(a())
print(a())
print(a())
print(a())


def bank(balance):

    def account(amount):

        nonlocal balance

        balance += amount

        return balance

    return account

user1 = bank(1000)

print(user1(500))
print(user1(-200))
print(user1(100))


# Store add() function in a variable and call it.
def add():
   x = int(input("PLEASE ENTER THE NUMBER "))
   y = int(input("PLEASE ENTER THE NUMBER "))
   sum = x + y
   return sum
x = add
print(x())

# Pass add() into another function:
def adding(x,y):
    return x+y
def passing(g,a,b):
    return g(a,b)
add = passing(adding, 4,5)
print(add)  

# Store functions in dictionary:
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# Dictionary mapping operators to functions
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator(op, a, b):
    return operations[op](a, b)

# Example usage
print(calculator("+", 2, 2))  # 4
print(calculator("-", 4, 2))  # 2
print(calculator("*", 6, 2))  # 12
print(calculator("/", 8, 2))  # 4.0



# function selector
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# Dictionary mapping operators to functions
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div 
}

user = input("Please Enter The Opeartion ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if user in operations:
  result = operations[user](a,b)
  print("result = ",result)
else:
   print("invalid user input")  


# Create pipeline:
def clean():
   print("pipe 1")
def validate():
   print("pipe 2") 
def save():
   print("pipe 3")     

list1 = [clean(), validate(),save()]
for i in list1:
    print(list1)

# Build mini command system:
def help_command():
    print("Available commands: help, exit, greet")

def exit_command():
    print("Exiting program... Goodbye!")
    

def greet_command():
    print("Hello Vedant! 👋 Welcome to the mini command system.")

# Dictionary mapping command names to functions
commands = {
    "help": help_command,
    "exit": exit_command,
    "greet": greet_command
}

# Example usage
commands["help"]()   # Calls help_command
commands["greet"]()  # Calls greet_command
commands["exit"]() # Uncomment to exit program


# baby mood command system
def mood():
   print("meri jaanu ka mood kaisa hai jaano ")
def happy():
   print("meri kehsu ka mood ekdm ok hai ")   
def romantic():   
   print("aaj hum khana khaynge ❤️❤️❤️")

commands = {
   "hello":mood(),
   "mwaah":romantic(),
   "puuchi":happy()
}

commands["hello"]
commands["mwaah"]
commands["puuchi"]