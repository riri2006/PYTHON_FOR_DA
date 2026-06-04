class employee:
    def __init__(self,sal,ag):
        self.salary = sal
        self.age = ag
    def display(self):
        print("the salary{self.sal} and thr age is {self.age}")    

e1=employee(23000,32)  
e2 =employee(230000000,32)  

print(e1.salary)
print(e2.salary,e2.age)