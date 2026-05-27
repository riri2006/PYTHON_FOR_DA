# A class is used to group variables and functions together into one structure.

# class Dog:
#     is_animal = True
#     def bark():
#         print("woof!")

# dog = Dog()
# print(dog.is_animal)
# Dog.bark()





# class Player:
#     def set_info(self, name, score):
#         self.name = name
#         self.score = score

#     def show_status(self):
#         print(self.name, self.score)

# p1 = Player()
# p2 = Player()

# p1.set_info("Alice", 10)
# p2.set_info("Bob", 5)

# p1.show_status()
# p2.show_status()



     


# class car():
#     def __init__(self,brand, model):
#         self.brand = brand
#         self.model = model
# mycar = car("toyota", "camry")
# print(mycar.brand)
# print(mycar.model)


class vehicel():
    color = "yellow"
    model = 1985
    number = 1947

v1 = vehicel()
print(v1.color)
print(v1.model)
print(v1.number)



nums = [1,2,3]

result = list(map(lambda x: x*2, nums))

print(result)


import math
print(vars(math))