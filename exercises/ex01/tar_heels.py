"""An exercise in remainders and boolean logic."""

__author__ = "730310486"


# Begin your solution here...

user_number: int = int(input("Enter an int: "))

if user_number % 2 == 0 and user_number % 7 == 0:
    print("TAR HEELS")
else:
    if user_number % 2 == 0:
        print("TAR")
    if user_number % 7 == 0:
        print("HEELS") 
    else:
        print("CAROLINA")
