def outer(name):
    def inner():
        print(name)
    return inner()
english = outer("hello")
hindi = outer("namaste")
english()
hindi()