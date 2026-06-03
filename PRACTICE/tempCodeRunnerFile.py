def locker(api):
    def key():
        return api
    return key
check = locker(123123)
print(check(1234))