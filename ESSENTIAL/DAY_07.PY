# y = 20
# def function():
#     x = 10
#     print(x)

# print(y)


def myfun():
    b = 20
    def nestedfun():
        nonlocal b
        x = 10 
        b = 30 
        print(x)
        print(b)

    nestedfun()
    print(b)
myfun()


# golbal() variable
x = 10
print(globals())

#  accessing the variable 
print(globals()['x'])


# # local variable
def test():
    a = 10
    b = 20

    print(locals())

test()


# print(dir(str))



# #  example
# var_name = "x"

# x = 10
# print(var_name)
# print(globals()[var_name])
# print(globals())



import builtins

func = builtins.print
 
func("Hello Vedant")


import builtins
builtins.print = lambda x: "Blocked"
print("Hello")

#  packing and unpacking 
# import numbers


# my_list = [1,2,3,4,5]
# print(*my_list)

# my_tuple = (1,2,3,4,5)
# print(*my_tuple)

my_set = {1,2,3,4,5}
print(*my_set)

# my_dict = {"a":1, "b":2, "c":3}
# print(*my_dict)
# for k,v in my_dict.items():
#     print(k,v)




# unpcking
def funsum(a,b,c,d):
    print(a+b+c+d)

my_list = [1,2,3,4]
funsum(*my_list)  

def myfun1(*numbers):
   print(numbers)
   print(sum(numbers))
# myfun1(1,2,3,4,5)

  


# def sum_of_lists(*list):
#    print(sum(list))  

#    list1 = [1,2,3,4,5]
#    list2 = [6,7,8,9,10]
#    list3 = [11,12,13,14,15]
#    list = [*list1,*list2,*list3]


person = {"name": "Daneyal", "age": 25, "city": "Kanpur"}

print("My name is {name}, I am {age} years old, live in {city} city.".format(**person))



