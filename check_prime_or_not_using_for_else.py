# Write a program to check whether a number is prime or not using for else loop.

#  if num=10 then possible factors are 1, 2, 5, 10, so it is not a prime number
# As per the rule of prime number it should have only 2 factors, 1 and the number itself.
# So, I check the number having any factor excluding 1 and the number itself. then it is not a prime number.

num=int(input("Enter a number: "))
countFact=0

if num>1:
    for val in range(2, num//2+1):  # check the factors of the number
        if num % val ==0: 
            print("The number is not a prime number")
            break
    else:
        print("The number is a prime number")
else:
    print("The number is not a prime number")