"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730310486"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says...")
fortune = randint(1, 100)
print(fortune)
if fortune <= 25:
    print("Your future is looking bright")
else:
    if fortune <= 75:
        print("Soon life will become more interesting.")
    else:
        print("Be careful what you wish for.")





print("Now, go spread positive vibes!")
