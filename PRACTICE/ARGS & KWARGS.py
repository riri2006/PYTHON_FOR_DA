def test(*args):
    print(args)

test(1,2,3)
def test(**kwargs):
    print(kwargs)

test(name="Vedant", age=20)

# Q3  Create function: using *args.
def add_all(*args):
    total = 0 
    for i in args:
        total += i
    return total
print(add_all(1,2,3,4,5))

# Q4  Create function that prints all key-value pairs using **kwargs.
import pandas as pd

def pri(**kwargs):
    # Instead of printing, we RETURN the kwargs dictionary 
    # so other parts of your code (like pandas) can use it.
    return kwargs

# 1. Run the function and save the returned dictionary to a variable
my_data = pri(name="veadnt", age=21)

# 2. Give that data to pandas!
# Note: Because our data is just single values (scalars), 
# pandas likes it wrapped in a list: [my_data]
dfg = pd.DataFrame([my_data])

print(dfg)


def test(a,*args):
    print(a,args)

test(10,20,30,40)

def a():
    return b()

def b():
    return 10

print(a())

# .........
def test():
    return print("Hello")

x = test()

print(x)

# .........
def say_hello():
    return "Hello there!"

def get_machine():
    # Returning the function object itself
    return say_hello 

# We run get_machine(), and save what it gives us into 'my_tool'
my_tool = get_machine() 

print(my_tool())    # Output: <function say_hello at 0x...>
print(my_tool())  # Output: "Hello there!" (We have to turn the machine on!)