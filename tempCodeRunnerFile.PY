x = 10  # global

def test():
    x = 5  # local
    print(x)

test()
print(x)