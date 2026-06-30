class Costumer:
    
    def __init__(self,name,gender):
      self.name = name
      self.gender = gender

def greet(Costumer):
     
    if Costumer.gender == "male":
      print("Hello",Costumer.name,"master jiii")
    else:
       print("HELO",Costumer.name,"madam jiii")  

count = Costumer("vedant","female")    

greet(count)




def var(x):
   print(x,id(x))
   x = 15
   print(x,id(x))

x =10
var(x)
print(x,id(x))


def var(x):
   print(x,id(x))
   x.append(4)
   print(x,id(x))

x = [1,2,3]   
var(x)
print(x,id(x))


