def outer(func):
    def wrapper():
        print("Calling Function Add")
        func()
    return wrapper
@outer
def first():
    print("i m the first")
first()    


# request 
def counter(limit):
    count = 0
    def wrap():
        nonlocal count
        if count < limit:
            count +=1
            print("allowed")   
        else:
            print("blocked")     

    return wrap
result = counter(3) 
result()
result()
result()
result()
result()



# TASK 2 — TIMER
import time
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Finished in",end-start)

    return wrapper
@timer
def hello():
    print("hello bhai")
hello()    

logged_in = True

def login_required(func):

    def wrapper():

        if logged_in:
            func()

        else:
            print("Access Denied")

    return wrapper


@login_required
def dashboard():
    print("Dashboard Open")


dashboard()


# API Usage Tracker (Closure)

def traker():
    count = 0
    def request():
        nonlocal count
        count += 1
        print(count)
    return request 

api_request = traker()
api_request()