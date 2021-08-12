# Take Name of Player
name = input("Please Enter Your Name:")
answer = 7

# Take Choice
choice = input(
    "Do you want to play a simple game?\nPlease answer in either 'Yes' or 'No'\t")

# Check Choice
if choice == 'Yes' or choice == 'YES':
    print("Great! Brace Up For Fun {0}!".format(name))
    guess = int(input("Guess a number from 1 to 10:"))
    if guess < answer:
        print("Guess A Little Higher")
    elif guess > answer:
        print("Guess a little lower")
    else:
        print("Thats Correct!! Whoopie")
else:
    print("Okay {0}! Come back when you want to play!".format(name))
