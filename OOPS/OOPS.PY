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




class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)


# Creating an object
my_tesla = ElectricCar('tesla', 'model s', 2016)

# Calling a method
print(my_tesla.get_descriptive_name())

