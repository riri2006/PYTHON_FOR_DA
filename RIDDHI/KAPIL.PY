# print("This is Calc.")
# x = int(input("Please Enter The First Number. "))
# y = int(input("please enter second sumber,"))
# print("the addition is :", x+y)
# print("the dff is :", x-y)
# print("the product is :", x*y)
# print("the div is :", int(x/y))



# x = int(input("Enter Hours  "))
# y = float(input("Enter Rate  "))

# rate = x*y

# print("Pay", rate)

# print("123" + "abc")


# LOOPS 

# colour = input("Enter The colour: ")

# if colour == "red" :
#     print("the fuit is apple :")
#     print("hello")

# elif colour == "orange":
#     print("the fruit is orange")
# else:
#     print("baki sb toh aam hai:")    


# num = int(input("enter the number : "))    
# if num < 1:
#     print("number is less then 1 :")

# elif num < 100:
#     print("number is less than 100") 

# else:
#     print("numeer is greater than 100")



# from sys import exception


# print("This is Calc.")
# x = int(input("Please Enter The First Number. "))
# y = int(input("please enter second sumber,"))
# print("the addition is :", x+y)
# print("the dff is :", x-y)
# print("the product is :", x*y)
# try:
#     print("the div is :", int(x/y))

# except Exception as e:
#     print(e)
    
    

while True:
    user = input("enter ohh:  ")
    if user in ["bye","phatt"]:
        break
    try:
        a = int(input("Enter Your Pin: "))
        print("You Enterd the pin Succesfully")
        b = int(input("Enter another number: "))

        print(a / b)

    except ValueError:
        print("Please enter numbers only")

    except ZeroDivisionError:
        print("Cannot divide by zero")

