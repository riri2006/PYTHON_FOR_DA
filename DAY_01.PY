# x = 10
# print(x)
# y= 20
# print(y)
# z = x+y 
# print(z)
# isgreater = z > 31
# print(isgreater)

# if isgreater > 30 :
#     print("z is greater than 30")
# else:    print("z is not greater than 30")


# for i in range (10):
#     if i < 5:
#         print(i)
        
# i = 0 
# while i<10:
#     print (i)
#     i = i+1        

# list = [1,2,3,4,5,6,7,8,9,10]    
# print(list)
# if list[0] == 1:
#     print("the first element is 1")
# else:
#     print("the first element is not 1")


# def add(a,b):
#     return a+b
# result = add(5,10)
# print(result)    

# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# def add(a=0, b=0):
#     return a+b
# result = add(x,y)
# print(result)

# def greet(name="Vedant"):
#     print("Hello", name)

# greet()
# greet("Alice")
# greet("AI Engineer")


# x = 10  # global

# def test():
#     x = 5  # local
#     print(x)

# test()
# print(x)


# import os
# folder_name = "aimlrv"
# print(os.path.abspath(folder_name))
# os.makedirs(folder_name, exist_ok=True)
# print(os.getcwd())

# first_name = "Vedant"
# last_name = "Kapil"

# fullname = f"{first_name} {last_name}"
# print(fullname)

contact_information = {
    "name": "Alfredo",
    "lastname": "Deza",
    "age": 49,
    "height": 1.90
}
for key in contact_information.keys():
    print(key)

for key, value in contact_information.items():
    print(key, value)