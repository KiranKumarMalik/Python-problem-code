# Write a function to check the number is Palyprime number or not
# Palyprime: Palindrome and also Prime

def Palyprime(num,dup,val=1,count=0,res=0):
    dup=num
    while val<=num:
        if num%val==0:
            count=count+1
        val=val+1
    if count==2:
        while num>0:
            lastDigit=num%10
            res=res*10+lastDigit
            num=num//10
        if dup==res:
           return True
        else:
            return False
    else:
        return False
num=int(input("Enter a number: "))
print(f"{num} is a Palyprime number" if Palyprime(num,num)==True else f"{num} is not a Palyprime number")



#********************************** SECOND APPROACH ***********************************************
# def Prime(num):
#     if num>1:
#         for val in range(2,num//2+1):
#             if num%val==0:
#                 return False
#             return True
# def Reverse(num,res=0):
#     while num != 0:
#         lastDigit=num%10
#         res=res*10+lastDigit
#         num=num//10
#     return res
# num=int(input("Enter a number: "))
# print(f"{num} is a Palyprime number" if (Prime(num) and Reverse(num)==num) else f"{num} is not a Palyprime")