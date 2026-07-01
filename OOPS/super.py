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
