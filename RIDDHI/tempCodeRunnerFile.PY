print("This is Calc.")
x = int(input("Please Enter The First Number. "))
y = int(input("please enter second sumber,"))
print("the addition is :", x+y)
print("the dff is :", x-y)
print("the product is :", x*y)
try:
    print("the div is :", int(x/y))

except ZeroDivisionError: