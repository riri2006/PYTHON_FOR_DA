class fan:
    def __init__(self,brand , speed):
        self.brand =  brand
        self.speed = speed

    def increase_speed(self,more_speed):
        self.speed += more_speed
        print(f"{self.speed}, {self.brand}")

    def dec_speed(self, less_speed):
        self.speed -= less_speed  
        print(f"{self.speed}")  

    def show_speed(self):
        print(self.speed)    

s1 = fan("usha", 120)
s1.increase_speed(100)
s1.dec_speed(90)
s1.show_speed()