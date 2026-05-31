def task(func):
    def wrapper():
        func()
        print("vedant")
    return wrapper    
@task
def inner():
    print("hello")

inner()
  