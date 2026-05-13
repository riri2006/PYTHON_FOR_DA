def myfun(a,b,c,d):
    print(a,b,c,d)

    d = {"a":10, "b":20, "c":30, "d":40}
    myfun(**d)
    print(d)
