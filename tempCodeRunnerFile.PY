class Car:
    print("The car names and features are availables below")
    def __init__(self,name , color , number ,model):
        self.name = name
        self.model = model
        self.color = color
        self.number = number

class Me_car_shop(Car):
    pass
obj = Me_car_shop("maruti","white","1234","800") 
print(obj.name)