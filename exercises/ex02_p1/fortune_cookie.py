"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730310486"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())

    print("Now, go spread positive vibes!")


# TODO 1: Define your fortune_cookie function here.
def fortune_cookie() -> str:
    fortune = randint(0, 100)
    if fortune <= 25:
        fortune_cookie = "Your future is looking bright"
    else:
        if fortune <= 75:
            fortune_cookie=  "Soon life will become more interesting"
        else:
            fortune_cookie = "Be careful what you wish for. "
    return fortune_cookie
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
