# def Happy(num):
#     while num>9:
#         res=0
#         while num>0:
#             lastDigit=num%10
#             res=res+lastDigit**2
#             num=num//10
#         num=res
#     if num==1 or num==7:
#         return True
#     else:
#         return False   
# num=int(input("Enter the number: "))
# print(f"{num} is a Happy number" if Happy(num)==True else f"{num} is not a Happy number")


#************************************ SECOND APPROACH **************************************
def Square(num,res=0):
    while num>0:
        lastDigit=num%10
        res=res+lastDigit**2
        num=num//10
    return res
def Happy(num):
    while num>9:
        num=Square(num)
    if num==1 or num==7:
        return True
    else:
        return False
num=int(input("Enter the number: "))
print(f"{num} is a Happy number" if Happy(num)==True else f"{num} is not a Happy number")