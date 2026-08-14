class Animal:
    def __init__(self, name):
        self.name = name

class Child(Animal):
    pass

dog = Child("bruno")
print(dog.name)
