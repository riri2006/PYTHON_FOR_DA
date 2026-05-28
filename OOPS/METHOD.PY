from tkinter import Y


class Student:

    def __init__(self, name):

        self.name = name

    def intro(self):

        print("My name is", self.name)

s1 = Student("riddhikapil")
Student.intro(s1)
s1.intro()

# TASK 1
class dog:
    def __init__(self,name , breed):
        self.name = name 
        self.breed = breed

    def bark(self):
        print("{name} is barking")

do = dog("luci","musi")
dog.bark(do)

# TASK 2
class Calculator:

    def add(self, x, y):

        print("Addition:", x + y)

    def subtract(self, x, y):

        print("Subtraction:", x - y)


c1 = Calculator()

c1.add(10, 20)

c1.subtract(50, 10)


# 
class Calculator:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def add(self):

        print(self.x + self.y)

    def subtract(self):

        print(self.x - self.y)


c1 = Calculator(10, 20)

c1.add()

c1.subtract()

# RETASK

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, kharcha):
        self.balance = self.balance - kharcha
        print(f"{self.balance}, {self.name}")
    
    def withdraw(self, amount):
        print(f"{self.balance}")
    
    def check_balance(self):
        print(f"{self.balance}")

s1 = BankAccount("heera", 1000)
s1.deposit(200000)
s1.withdraw(300000)
s1.check_balance()

# task of day 2
class fan:
    def __init__(self,brand , speed):
        self.brand =  brand
        self.speed = speed

    def increase_speed(self,more_speed):
        self.speed += more_speed
        print(f"{self.speed}, {self.brand}")

    def dec_speed(self, less_speed):
        self.speed -= less_speed  
        print(f"{self.speed}")  

    def show_speed(self):
        print(self.speed)    

s1 = fan("usha", 120)
s1.increase_speed(100)
s1.dec_speed(90)
s1.show_speed()


# TASK 2 — LIGHT SYSTEM 💡

class light:
    def __init__(self,brightness):
        self.brightness = brightness

    def increase_brightness(self,increase):
        self.brightness += increase
        print(f"the increased brightness is, {self.brightness}")

    def decrease_brightness(self, decrease):
        self.brightness -= decrease
        print(f"the decreased brightness is {self.brightness}")

    def show_brightness(self):
        print(self.brightness)

l1 = light(1000)
l1.increase_brightness(200)
l1.decrease_brightness(300)
l1.show_brightness()


# TASK 3 — YOUTUBE VIDEO ▶️
class video:
    def __init__(self, title, likes):
        self.title = title
        self.likes = likes

    # Renamed this method from 'likes' to 'add_likes'
    def add_likes(self, likees):
        self.likes += likees
        print(self.likes, self.title)

    def dislike(self, dislike):
        self.likes -= dislike
        print(f"{self.likes}, aaya mja")  

    def show_likes(self):
        print(f"all likes are, {self.likes}")

y = video("billionare", 100000)
y.add_likes(5000)     # Updated method call here
y.dislike(50000)
y.show_likes()

# TASK 4 — INSTAGRAM ACCOUNT 📸

class insta:
    def __init__(self,username, followers):
        self.username = username
        self.followers = followers

    def gain_followers(self, gained):
        self.followers += gained
        print(self.followers)

    def lose_followers(self, lose):
        self.followers -= lose
        print(self.followers)  

    def show_followers(self):  
        print(self.followers) 

m = insta("vedant", 2000)
m.gain_followers(1000)
m.lose_followers(1500)  
m.show_followers()  

