def power_factory(ex):
    def power(ba):
        return ba**ex
    return power
square = power_factory(2)
cube = power_factory(3)
riddhi = power_factory(4)
print(square(5))
print(cube(5))
print(riddhi(5))
print(square.__closure__)
print(square.__closure__[0].cell_contents)
print(cube.__closure__)
print(cube.__closure__[0].cell_contents)
print(riddhi.__closure__)
print(riddhi.__closure__[0].cell_contents)




# def power(base, ex):
#     return base ** ex

# print(power(5, 2))
# print(power(5, 3))
# print(power(5, 4))

# def power_factory(ex):
#     def power(ba):
#         return ba ** ex
#     return power

# square = power_factory(2)

# # Function object
# print(square)

# # Closure object
# print(square.__closure__)

# # Value stored in closure
# print(square.__closure__[0].cell_contents)

# # Free variables used
# print(square.__code__.co_freevars)


