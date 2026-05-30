# Pass hello function to another function.
def hello(name):
    return f"hello,{name}"

def pas1(fun,bela):
    return fun(bela)

reult = pas1(hello,"vedant")
print(reult)