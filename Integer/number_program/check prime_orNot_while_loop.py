# Write a program to check whether a number is prime or not using while loop.

num=int(input("Enter the number: "))
i=1              # Initialize the counter variable to 1, factors of a number are always greater than 1
countfactor=0    # Initialize the countfactor variable to 0, store increment of the countfactor if the number is divisible by i
while i<=num+1:   # if num=10, then the factors are 1,2,5,10 so the loop should run upto num+1=11
    if num % i == 0:
        countfactor = countfactor + 1  # increment the countfactor if the number is divisible by i
    i=i+1            # increment the counter variable
if countfactor==2:   # if the countfactor is 2, then the number is prime
    print("The number is prime")
else:
    print("The number is not prime")