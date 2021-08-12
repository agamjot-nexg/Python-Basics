name = input("Please Enter Your Name:")
age = int(input("Please Enter Your Age:"))

if age < 18:
    print("You are a minor! {0}".format(name))
elif age >= 18 and age < 21:
    print("You are an adult and eligible to vote {0}".format(name))
elif age > 21:
    print("You are an adult permitted to vote and drink {0}.".format(name))
