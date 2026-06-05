class Car:
    def __init__(self,windows, engine, model):
        self.windows = windows
        self.engine = engine
        self.model = model
    def self_driving(self):
        print("This is a self driving car")   
# d = Car(4,"v8","audiq7")
# print(d.self_driving())
# print(d.windows)
# print(d.engine)
# print(d.model)

class Audi(Car):
    def __init__(self,windows,engine,model,milage):
        super().__init__(windows, engine, model)
        self.windows = windows
        self.engine = engine
        self.model = model
        self.milage = milage

    def driving_school(self):
        print("Driving from hamarpur")   

d1 = Audi(4,"v8","audiq7",100)
d1.driving_school()
print(d1.windows)
print(d1.engine)
print(d1.model) 
print(d1.milage)
d1.self_driving()    
