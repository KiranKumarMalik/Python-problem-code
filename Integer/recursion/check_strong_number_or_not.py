# Write a program to check a number is Strong number or not Using Recursion
#Strong number: num=145 1!+4!+5!=num then it is a strong number
def Factorial(num):
    if num==0 or num==1: 
        return 1 
    else:
        return num*Factorial(num-1)
sum=0 

def check_StrongNumber(num): 
    global sum 
    if (num>0):
        fact = 1
        rem = num % 10
        check_StrongNumber(num // 10)
        fact = Factorial(rem)
        sum+=fact
    return sum
num=int(input("Enter a number: "))
if (check_StrongNumber(num) == num):
    print(f"{num} is a strong Number.")
else:
    print(f"{num} is not a strong Number.")