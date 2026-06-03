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