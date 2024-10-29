# Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

year=int(input("Enter a year: "))
is_leap_year(year)