"""A vaccination calculator."""

__author__ = "730310486"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target: int = int(input("Target percent vaccinated(chooses 0-100): "))

goal_doses: float = target / 100 * population * 2
goal_doses = goal_doses - doses_admin

days_left = round(goal_doses / doses_per_day)

today: datetime = datetime.today()
one_day: timedelta = timedelta(1)
goal_day: datetime = today + one_day * days_left
goal_day_str: str = goal_day.strftime("%B %d, %Y")


print("We will reach " + str(target) + "% vaccination in " + str(days_left) + " days, which falls on " + goal_day_str)