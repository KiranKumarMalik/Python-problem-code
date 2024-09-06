# Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

a=int(input("Enter a input number:"))
if a>0:
    print(f"{a} is a positive number")
elif a<0:
    print(f"{a} is a negative number")
elif a==0:
    print(f"{a} is zero") 