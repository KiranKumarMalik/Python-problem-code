#**********************Using For Loop***************************
# This program calculates the factorial of a number.

n=int(input("Enter an Integer number: "))
factorial=1 # Initialize the factorial to 1

for i in range(n):
    factorial=factorial*(i+1)  # Formula to find the factorial of a number

print(f"The factorial of {n} is {factorial}")