# class Car:
#     def __init__(self,windows, engine, model):
#         self.windows = windows
#         self.engine = engine
#         self.model = model
#     def self_driving(self):
#         print("This is a self driving car")   
# # d = Car(4,"v8","audiq7")
# # print(d.self_driving())
# # print(d.windows)
# # print(d.engine)
# # print(d.model)

# class Audi(Car):
#     def __init__(self,windows,engine,model,milage):
#         super().__init__(windows, engine, model)
#         self.windows = windows
#         self.engine = engine
#         self.model = model
#         self.milage = milage

#     def driving_school(self):
#         print("Driving from hamarpur")   

# d1 = Audi(4,"v8","audiq7",100)
# d1.driving_school()
# print(d1.windows)
# print(d1.engine)
# print(d1.model) 
# print(d1.milage)
# d1.self_driving()    
# print(dir(Audi))
# print(dir(Car))




class User:
    def __init__(self):
        self.name = 'hello'
        print("Welocme")

    def login():
        print("you have loggined")

class Student(User):
    # def __init__(self):
    #     self.roll = 20
    #     print("WELCOME again")

    def register():
        print("you have been registerd")     

class Inveglator(User):
    def __init__(self):
        print("welcome students i'm your invigelator")
        

    def hello():
        print("yeeee")



a = User()
b = Student()
c = Inveglator()

print(b.name)



class A:

    def m1(self):
        return 20

class B(A):

    def m1(self):
        val=super().m1()+30
        return val

class C(B):
  
    def m1(self):
        val=super().m1()+20
        return val
obj=C()
print(obj.m1())



from sys import exception


print("This is Calc.")
x = int(input("Please Enter The First Number. "))
y = int(input("please enter second sumber,"))
print("the addition is :", x+y)
print("the dff is :", x-y)
print("the product is :", x*y)
try:
    print("the div is :", int(x/y))

except Exception as e:
    print(e)
    