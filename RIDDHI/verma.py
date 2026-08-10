# try and except and function practice




from sys import exception

from numpy import astype


print("this is my  id card: ")

def id(name,roll_no,age):
    try:
        print("your name is:",name, astype = str)
    except TypeError:
        print("enter only string type")

    try:    
        print("your age is ", age, astype = int)

    except:
        print("enter only numeric value ")

    try:
        print("your roll_no is ", roll_no, astype = str)
    except:
        print("enter only string type ")

naam = str(input("Enter the name: "))
agee = int(input("Enter your age: "))
roll = int(input("Enter your roll number: "))

id(naam, roll, agee)        





print("This is my ID card: ")


def id(name, roll_no, age):

    try:
        print("Your name is:", name, astype = str)
    except Exception as e:
        print("Bhai kya dala hai")

    try:
        print("Your age is:", age, astype = int)
    except Exception as e:
        print(e)

    try:
        print("Your roll_no is:", roll_no, astype = int)
    except Exception as e:
        print("Enter only string type")


naam = str(input("Enter the name: "))
agee = int(input("Enter your age: "))
roll = int(input("Enter your roll number: "))

id(naam, roll, agee)



print("This is my ID card")


def id_card(name, roll_no, age):
    print("Your name is:", name)
    print("Your age is:", age)
    print("Your roll number is:", roll_no)


try:
    naam = str(input("Enter your name: "))
except ValueError:
    print("Please enter a valid name.")


try:
    agee = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number for age.")


try:
    roll = int(input("Enter your roll number: "))
except ValueError:
    print("Please enter a valid number for roll number.")


id_card(naam, roll, agee)