# Write a program to find the factorial of a number using while loop.

num=int(input("Enter an Integer number: "))
factorial=1                         # Initialize the factorial variable to 1, as 0! = 1
i=1                                 # Initialize the counter variable to 1
while i<=num:                       # Check the condition if i is less than or equal to the number because if num=5, then 5!=5*4*3*2*1
    factorial=factorial*i
    i=i+1
print("Factorial of",num,"is",factorial)