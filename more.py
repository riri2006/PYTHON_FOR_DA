class Person:
    def __init__(self,name,gender):
     self.name = name
     self.gender = gender

#out side the class this is not the method

def greeting(Person):
        print(f"My name is {Person.name} and My Gender is {Person.gender}")

obj = Person("vedant","male")
greeting(obj)

