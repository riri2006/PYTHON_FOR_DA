
def decorator(abc):
    def wrapper():
        print("Boss ne bola hai ki mujhe pehle print kro")
        abc()

    return wrapper    




def greet():
    print("hello")

greet = decorator(greet)

greet()
