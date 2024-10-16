# Write a program to find the factorial of a number using function
def Factorial(num, fact=1):
    for i in range(1,num+1):
        fact=fact*i
    return fact
num=int(input("Enter an Integer: "))
print(f"Factorial of {num} is {Factorial(num)}")