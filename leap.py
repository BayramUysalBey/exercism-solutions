"""Your task is to determine whether a given year is a leap year."""

# My solution
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)