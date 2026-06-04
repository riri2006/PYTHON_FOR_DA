class Dog:
    
    def bark(self,x): #Linking the self with d1
        return x +1
d1 = Dog()  #Assigning the d1 as object
print(d1.bark(1))    


class Marks:
    def subject(self,maths):
        print("the marks in maths are mwaah ")
        return maths
mark = Marks()
print(mark.subject(100))

class Practice():
    def __init__(self,name):
        self.name = name
        print(name)
    def nao(self):
        print("yupp")  
nam = Practice("vedant")
print(nam.__init__("hello"))   
nam.nao()


class Method:
    def __init__(self,age,name,subject):
        self.age = age
        self.name = name
        self.subject = subject

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_student(self):
        return self.subject

d1 = Method("vedantriddhi",21,"mwaahh")
print(d1.get_name())
print(d1.get_age())
print(d1.get_student())


class Student:
    pass
s1 = Student
s1.name ="vedant"
s1.age =21        
print(s1.name)
print(s1.age)



class Student:

    def intro(self):
        print("Hello")
Student.intro(Student())        


class Student:
    def into(self,name):
        print(name)
d1 = Student()
print(d1.into("vedant"))


class Student:

    def __init__(self, name):
        self.name = name
d =Student("vedant") 
print(d.name) 


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
d = Student("vedant",21)
print(d.name)
print(d.age)



class Student:

    def __init__(self, name):
        self.name = name

    def intro(self):
        print(self.name)

s = Student("vedantridddhi")
print(s.name)
s.intro()



class Calculator:

    def add(self, a, b):
        print(a + b)
s = Calculator()  
print(s.add(1,14)) 



class Student:

    def intro(self):
        print(self)

s1 = Student()
s2 = Student()
print(type(s1.intro()))  
print(type(s2.intro()))  

class Student:

    school = "ABC"

    def __init__(self,name):
        self.name = name

s1 = Student("Vedant")
s2 = Student("Riddhi")

s1.school = "XYZ"

print(s1.school)
print(s2.school)
print(Student.school)