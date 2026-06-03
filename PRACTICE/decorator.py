
# import exper as exp

# def change(puuchi):
#     def wrapper():
#         print("01")
#         puuchi()
#     return wrapper

# @change
# def printer():
#     print("employee")

# printer()
# @change
# def trip():
#    print("hima")

# trip()


def decor(add):

    def wrapper():

        result = add()

        num3 = int(input("Enter third number: "))

        result = result + num3

        return result

    return wrapper


@decor
def add():

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 + num2

    return result


print("Answer is :", add())

# Before / After decorator.
def devprator(func):
    def wrapper():
        return f"this is after"
    func()

    return wrapper


@devprator
def before():
    print("this is before")
    return f"hello"
result = before()
print(result)


# Decorator for calculator functions.
def before(func):
    def after(x, y):  # ✅ accept arguments
        print("Printing before")
        return func(x, y)  # ✅ call original function here
    return after

@before
def add(x, y):
    return x + y

adx = add(2, 3)
print(adx)