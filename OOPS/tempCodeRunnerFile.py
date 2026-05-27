class dog:
    def __init__(self,name , breed):
        self.name = name 
        self.breed = breed

    def bark(self):
        print("{name} is barking")

do = dog("luci","musi")
dog.bark(do)