class New:
 def __init__(self):
        print("WELCOME TO THE JP MORGANS AND CO")
        self.menu()

 def menu(self):
    user_input = input(
            '''Hello how would you like to processed 
            1.Create pin
            2.Deposit
            3.Withdraw
            4.Check balance
            5.exit : '''
        )

    if user_input == "1":
        self.create_pin()
    elif user_input == "2":
        self.deposit()
    elif user_input == "3":
        self.withdraw()
    elif user_input == "4":
        print("Check Your Balance")    
    elif user_input == "5":
        print("Thank You")     
    else:
        print("Invalid response")

 def create_pin(self):

    try:
        self.pin = int(input("Enter your 4-digit PIN: "))
        print("PIN created successfully.")

    except ValueError:
        print("PIN must contain only numbers.")

 def deposit(self):
        
    try:
        self.money = int(input("please enter the amount you want to deposit : "))
        print("the money is deposited succesfully ")    
    except ValueError:
        print("please enter the valid input ")
   
 def withdraw(self):
     self.withdwral = int(input("please enter the amount you want to withdraw"))
     print("the amount you enterd is deposeted succesfully")

obj = New()