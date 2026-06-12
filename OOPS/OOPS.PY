class Fraction:
    def __init__(self,x,y):
     self.num = x
     self.den = y
    
    def __str__(self):
      return '{}/{}'.format(self.num,self.den)   
    
    def __add__(self,other):
     new_number = self.num*other.den + self.den*other.num
     new_den = self.den*other.den
     return '{}/{}'.format(new_number, new_den)   

    #  return Fraction(new_number, new_den)
      

obj = Fraction(1,2)
obj1 = Fraction(1,2)
result = obj + obj1
print(result)




class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'india':
      print('Namaste',self.name)
    else:
      print('Hello',self.name)

# how to access attributes
p = Person('nitish','india')
