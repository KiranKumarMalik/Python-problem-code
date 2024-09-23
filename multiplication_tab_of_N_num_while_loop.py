# Table of a Number: Write a Python program using a while loop to print the multiplication table of a given number N.

num=int(input("Enter the number: "))
MultiUpto=int(input("Enter the number upto which you want to print the multiplication table: "))
val=1    # Initialize the value of val
product=0

while val<MultiUpto+1:
    product=num*val
    print(f"{num} * {val} = {product}")
    val=val+1