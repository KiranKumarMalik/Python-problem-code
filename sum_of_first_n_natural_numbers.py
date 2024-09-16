#*****************Using for loop*****************
#  Sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, 
# where N is taken as input from the user.

n=int(input("Enter a natural number:"))

for i in range(n):
    sum=(n*(n+1))//2 # Formula of arithmetic progression to find the sum of first n natural numbers (n(n+1))/2

print(f"The sum of first {n} natural number is {sum}")