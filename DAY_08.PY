def sum1(*numbers):
   print(numbers)   
   print(sum(numbers))

   
numbe = (1,2,3,4,5)

sum1(*numbe)

a = int()
b = int(7)
c = int("12")

total = a + b + c
print(total)

def show_long_names(*members):
    for person in members:
        if len(person) > 3:
            print(person)

show_long_names("Ana", "Luis", "Eve", "Carla")




# COURSERA EXCERCISE



# Create a function that prints some output based on input.

# Define a function that returns a random number.

# Implement a function that calculates the area of various shapes depending on arguments.

# Write a reusable greeting function that takes a name input.

# Write a function to convert temperatures from Fahrenheit to Celsius.

def converter(cel):
    fer = (0.45 * cel)
    return fer

temp = float(input("please enter the temperature::"))
print(temp)

    
result = converter(temp)
print(result)



def converter(cel):
    # Multiply by 1.8 and add 32
    fer = (cel * 1.8) + 32
    return fer

# Get user input and convert it to a floating-point number
temp_input = float(input("Please enter the temperature in Celsius: "))

# Call the function with the user input
result = converter(temp_input)

# Print the final result
print(f"{temp_input}°C is equal to {result}°F")
