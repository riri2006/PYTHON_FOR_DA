def traker():
    count = 0
    def request():
        nonlocal count
        count += 1
        print(count)
    return request 

api_request = traker()
api_request()