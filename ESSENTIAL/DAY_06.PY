# # def add(*numbers):
# #      print(numbers)

# #      print(sum(numbers))


# # add(1, 2, 3)
# # add(1, 2, 3, 4)
# # add(0,0,0)


# # def myfun(a,b,c,d):
# #     print(a,b,c,d)

# # d = {"a":10, "b":20, "c":30, "d":40}
# # myfun(**d)
    
# # def addnumbers(*args):
# #     print(args)
# #     print(sum(args))

# # addnumbers(1,2,3)
# # addnumbers(1,2,3,4)





# def func(*ip):
#     return tuple(i ** 2 for i in ip)

# result = func(1,2,3,4,5)
# print(result)




# # for mwaaah in range(5):
# #     print(mwaaah**2)



# def id(vedant,riddhi,ved,keshu):
#     print("vedant",vedant,"riddhi",riddhi,"ved",ved,"keshu",keshu)  

# d = {"vedant":10,"riddhi":12,"ved":12,"keshu":34}
# d = {10,34,23,56}
# id(**d)


# args 

def args(*num): # it will accept the as touple 
    print(num)

args(10,2,3,4,5)
args(34,53,24,5)


def numbers(a, b, c):
    print(a, b, c)

values = {10, 20, 30}

numbers(*values)


# kwargs 

# def kwargs(**details): # as a dictonary
#     print(details)

# kwargs(name = "vedant", age = 21, love = "riddhi")    

# def kwargs(name,age,love):
#     print("name: ",name,"age:",age,"love: ",love)
# bag={"name":"Riddhi", "age":21, "love":"vedant"}
# kwargs(**bag)


def new(name):
    print("hola omigo!")

def neo(new):
        