# Write a Python program to find the factorial of a number using negative indexing and for loop.

num=int(input("Enter an Integer number: "))
factorial=1

for i in range(num, 0, -1): # -1 is used to print the numbers in reverse order using slicing concept
    factorial=factorial*i # factorial=1*5=5, factorial=5*4=20, factorial=20*3=60, factorial=60*2=120, factorial=120*1=120
print(f"The factorial of {num} is {factorial}")
