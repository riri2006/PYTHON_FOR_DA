class New:

    def __init__(self):
        print("WELCOME TO THE JP MORGANS AND CO")

        self.balance = 0
        

        while True:
            self.menu()

    def menu(self):

        user_input = input(
            '''
Hello, how would you like to proceed?

1. Create PIN
2. Deposit
3. Withdraw
4. Check Balance
5. Exit

Enter your choice: '''
        )

        if user_input == "1":
            self.create_pin()

        elif user_input == "2":
            self.deposit()

        elif user_input == "3":
            self.withdraw()

        elif user_input == "4":
            self.check_balance()

        elif user_input == "5":
            print("Thank You")

        else:
            print("Invalid Response")

    def create_pin(self):

        try:

            self.pin = int(input("Enter your 4-digit PIN: "))
            print("PIN created successfully.")

        except ValueError:

            print("PIN must contain only numbers.")

    def deposit(self):


        try:

            temp = int(input("Enter your PIN: "))

            if temp == self.pin:

                money = int(input("Please enter the amount you want to deposit: "))

                self.balance += money

                print("Money deposited successfully.")

            else:
                print("Incorrect PIN")

        except ValueError:

            print("Please enter a valid input.")

    def withdraw(self):

        try:

            temp = int(input("Enter your PIN: "))

            if temp == self.pin:

                withdrawal = int(input("Please enter the amount you want to withdraw: "))

                if withdrawal > self.balance:

                    print("Insufficient Balance")

                else:

                    self.balance -= withdrawal

                    print("Amount withdrawn successfully.")

            else:

                print("Incorrect PIN")

        except ValueError:

            print("Invalid Response")

    def check_balance(self):

        try:

            temp = int(input("Please enter your PIN: "))

            if temp == self.pin:

                print(f"Your Current Balance is ₹{self.balance}")

            else:

                print("Invalid PIN")

        except ValueError:

            print("PIN should contain only numbers.")


obj = New()