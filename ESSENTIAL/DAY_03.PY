# for method in dir(tuple()):

#     if method.startswith("__"):
#         continue

#     print(method)


    # LIST
students_list = ["Vedant", "Raj", "Amit", "Vedant"]

print("LIST:")
print(students_list)
print("First Student:", students_list[0])

students_list.append("Rahul")

print("After Append:", students_list)

print()


# TUPLE
students_tuple = ("Vedant", "Raj", "Amit", "Vedant")

print("TUPLE:")
print(students_tuple)
print("First Student:", students_tuple[0])

# students_tuple.append("Rahul") ❌ Error
# Tuple cannot be modified

print()


# SET
students_set = {"Vedant", "Raj", "Amit", "Vedant"}

print("SET:")
print(students_set)

students_set.add("Rahul")

print("After Add:", students_set)

print()


# DICTIONARY
student_dict = {
    "name": "Vedant",
    "age": 20,
    "city": "Boisar"
}

print("DICTIONARY:")
print(student_dict)

print("Name:", student_dict["name"])

student_dict["age"] = 21

print("Updated Dictionary:", student_dict)