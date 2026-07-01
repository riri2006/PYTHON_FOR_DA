class Phone:
    def __init__ (self,camera, brand, price):
        self.brand =  brand 
        self.price = price
        self.camera = camera

class Smartphone(Phone):
    def __init__ (self,camera, brand, price, os , ram):
        super().__init__ (camera, brand, price)
        self.os = os
        self.ram = ram

obj = Smartphone("48MP","Apple","50000","Bionic","4GB")
print(obj.brand)
print(obj.os)



# WE CANNOT ACCESS THE NUM

class Parents:
    def __init__(self,num):
        self.num = num

    def get_num(self):
        return self.num    

class Child(Parents):
    def __init__(self,var,num):
        self.var = var

    def get_var(self):
        return self.var

obj = Child(100,10)
print(obj.get_num())

# USING SUPER 

class Parents:
    def __init__(self,num):
        self.num = num

    def get_num(self):
        return self.num    

class Child(Parents):
    def __init__(self,var,num):
        super().__init__(num)
        self.var = var

    def get_var(self):
        return self.var

obj = Child(100,10)
print(obj.get_num(),obj.get_var())
