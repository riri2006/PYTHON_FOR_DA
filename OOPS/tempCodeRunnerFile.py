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