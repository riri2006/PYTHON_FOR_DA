
# def decorator(abc):
#     def wrapper():
#         print("Boss ne bola hai ki mujhe pehle print kro")
#         abc()

#     return wrapper    




# def greet():
#     print("hello")

# greet = decorator(greet)

# greet()



import time

def timer(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print("Execution Time:", end - start)

    return wrapper



def test():
    list1 =  [1,2,3,4,5,6,7,8,9,10]
    sum = 0
    for i in list1:
        sum = sum+i
    print(sum)

test = timer(test)


test()