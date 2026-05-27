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
        