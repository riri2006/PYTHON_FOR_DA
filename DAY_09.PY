# def square(x):
#     return x*x
# def calculate(func, n):
#     return func(n) 
# print(calculate(square, 10))



# words = ["apple", "banana", "cherry", "date", "elderberry"]
# uppercase_words = map(str.upper, words)
# print(list(uppercase_words))





# # for l in list:
# #     length.append(len(l))

# # print(length)
# list = ["apple", "banana", "chwwwrry"]

# length = tuple(map(len, list))

# print(length)



# list1 = [1,2,3,4]

# filter1 = list(filter(lambda a: a%2 == 0, list1))
# print(filter1)


# words = ["apple", "banana", "cherry", "date", "elderberry"]

# filter1 = filter(lambda word : "a" in word , words)
# print(list(filter1))


# marks = [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100]

# filter2 = filter(lambda mark : mark > 30 , marks)
# print(list(filter2))


# employee = [
#   {'name':'rajnath','age':50},
#   {'name':'raj','age':53},
#   {'name':'nath','age':34},
#   {'name':'raja','age':23}
# ]
# age_filter = filter(lambda age : age['age'] > 30 , employee)
# print(list(age_filter))


# reduce finction --> find the longest word in the given list.
from functools import reduce 
name = [ "Apple", "Banana", "Cherry", "Date", "Elderberry"]
# print(max(name, key=len))
# maxi = reduce(lambda x,y:x if len(x) > len(y) else y, name)
# print(maxi)

largest = []

for word in name:

    if len(word) > len(largest):
        largest = word

print(largest)  