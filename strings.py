# Print Some Basic Strings

print("Today is a good day")
print("Python is fun")
print("It's easy to learn")
print('We can use "double quotes" in python too')

# Print Concatinated Strings

print("hello"+" world")

# Use String Variables

a = "How are you doing?"
print(a)

# Concatinated variables in strings

greet = "Good Morning"
name = "Agamjot Singh"
print(greet + ' - ' + name)

# Take input and then print
greet2 = "Good Afternoon"
name2 = input("Please enter your name.\n")
print(greet2 + " - " + name2)
print("1\t2\t3\t4\t5")


# Print '\' and avoid exit character

print("The location is C\\Users\\Hello\\Desktop")  # Recommended
print(r"The location is C\users\tello\nesktop")  # Not Recommended


# Print Specific Character in a String

parrot = "Norwegian Blue"

print(parrot)
print(parrot[0])
print(parrot[-4])


# Slice Strings

print(parrot[0:9])
print(parrot[-4:-2])


# Use Steps in a slice

print(parrot[0:9:2])
