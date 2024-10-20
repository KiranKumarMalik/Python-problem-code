# Write a function given number is a strong number or not
def Strong(num,res=0):
    while num>0:
        fact=1
        lastDigit=num%10
        for val in range(1,lastDigit+1):
            fact=fact*val
        res=res+fact
        num=num//10
    return res
num=int(input("Enter the number: "))
if num==Strong(num):
    print(f"{num} is a Strong number")
else:
    print(f"{num} is not a Strong number")



# def Factorial(num,fact=1):
#     for val in range(1,num+1):
#         fact=fact*val
#     return fact
# def Strong(num,res=0):
#     while num>0:
#         lastDigit=num%10
#         res+=Factorial(lastDigit)
#         num=num//10
#     return res

# num=int(input("Enter a number: "))
# if num==Strong(num):
#     print(f"{num} is a Strong number")
# else:
#     print(f"{num} is not a Strong number")