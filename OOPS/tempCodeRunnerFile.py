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