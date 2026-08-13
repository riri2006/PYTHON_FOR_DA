class Fruits:

    def __init__(self,price,colour,weight,location):
        self.weight = weight
        self.location = location
        self.price = price
        self.colour = colour    
        print("hellow") 
        self.mango("Kesar") 
        self.apple()  

    def mango(self,variety):
        self.variety = variety
        print(self.variety)
        print(self.price) 
        print(self.colour)

    def apple(self):

        print(self.weight)
        print(self.location)   

object = Fruits(1200,"yellow",120,"Himachal")


