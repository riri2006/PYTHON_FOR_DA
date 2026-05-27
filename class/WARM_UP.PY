class Student:
    pass

s1 = Student()
s2 = Student()

print(s1,s2)



class Student:

    def __init__(self, name, age):

        print("Constructor running")

        self.name = name
        self.age = age

s1 = Student("vedant", 21)
print(s1.name)
print(s1.age)


# TASK 1
class mobile:

    def __init__(self, brand, price):
        self.brand = brand 
        self.price = price

phone = mobile("apple",90000)
print(phone.brand)
print(phone.price)

# TASK 2
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = employee("vedant", 1000000000000)
e2 = employee("riddhi" , 1000000000000000000)
print(e1.name, e2.name)

# TASK 3
class car:
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed

r1 = car("black", 120)
print(r1.color, r1.speed)