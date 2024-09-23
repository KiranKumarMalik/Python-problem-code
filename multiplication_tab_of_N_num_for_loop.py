# Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.

num=int(input("Enter the number: "))
MultiUpto=int(input("Enter the number upto which you want to print the multiplication table: "))
product=0

for val in range(1, MultiUpto+1): # Print the multiplication table of the number upto the given number
    product=num*val   # Calculate the multiplication table of the number
    print(f"{num} * {val} = {product}")