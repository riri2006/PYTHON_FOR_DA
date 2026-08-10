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