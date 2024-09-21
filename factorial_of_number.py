#**********************Using For Loop***************************
# This program calculates the factorial of a number.

n=int(input("Enter an Integer number: "))
factorial=1 # Initialize the factorial to 1

for i in range(n): # n is the ending index, upto n
    factorial=factorial*(i+1)  # factorial=1*1=1, factorial=1*2=2, factorial=2*3=6, factorial=6*4=24, factorial=24*5=120

print(f"The factorial of {n} is {factorial}")