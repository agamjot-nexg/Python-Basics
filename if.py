# name = input("Enter name:")
# age = input("How old are you {0}?:".format(name))
# # print("You are {0} years old {1}".format(age, name))

# Take input as int to avoid decimal value in line 15
age = int(input("Please enter your age:"))
if age >= 18:
    print("You are of legal age")
    print("Become a responsible Citizen")
else:
    print("You are too young!")

print("*****************Line Break*******************")

if age >= 18:
    print("You are eligible to vote.")
    print("Vote Responsibly")
else:
    print("Please come back in {0} years".format(18-age))
