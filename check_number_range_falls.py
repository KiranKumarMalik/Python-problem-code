# Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 
# 0-50, 51-100, 101-150, or above 150.

def check_number_range_falls():
    if num in range(0,51):
        print("The number falls in the range 0-50")
    elif num in range(51,101):
        print("The number falls in the range 51-100")
    elif num in range(101,151):
        print("The number falls in the range 101-150")
    elif num>150:
        print("The number falls above 150")
    elif num<0:
        print("The number is negative")

num=int(input("Enter the number: "))
check_number_range_falls()