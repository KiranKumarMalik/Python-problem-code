# Write a program to check whether a number is prime or not using while else loop.

# if num=10 then possible factors are 1, 2, 5, 10, so it is not a prime number
# As per the rule of prime number it should have only 2 factors, 1 and the number itself.
# So, I check the number having any factor excluding 1 and the number itself. then it is not a prime number.

num=int(input("Enter the number: "))
val=2

if num>1:
    while val < num//2+1: # check the factors of the number
        if num % val ==0:
            print("The number is not a prime number")
            break
        val+=1
    else:
        print("The number is a prime number")
else:
    print("The number is not a prime number")        