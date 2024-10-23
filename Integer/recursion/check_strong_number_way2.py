# Write a program to check a number is Strong number or not Using Recursion
#Strong number: num=145 1!+4!+5!=num then it is a strong number
def Factorial(num):
    if num==0 or num==1: 
        return 1 
    else:
        return num*Factorial(num-1)

def Strong(num):
    if num==0:
        return num
    else:
        rem=num%10
        return Factorial(rem)+Strong(num//10)
num=int(input("Enter a number: "))
print(f"{num} is a Strong number" if Strong(num)==num else f"{num} is not a Strong number")