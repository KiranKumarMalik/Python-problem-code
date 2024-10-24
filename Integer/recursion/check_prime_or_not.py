# Write a recursion fuction to check the number is Prime number or not

def Prime(num, val=1):
    if val==num+1:
        return 0
    if num%val==0:
        return 1 + Prime(num,val+1)
    return 0 + Prime(num,val+1)

number=int(input("Enter a number: "))
print(f"{number} is a Prime number" if Prime(number)==2 else f"{number} is not a Prime number")


#********************************************* SECOND APPROACH **********************************************
# def Prime(num,val=2):
#     if num <= 1:
#         return False
#     if val==num//2+1:
#         return True
#     if num % val==0:
#         return False
#     return Prime(num, val+1)
# number=int(input("Enter a number: "))
# print(f"{number} is a Prime number" if Prime(number)==True else f"{number} is not a Prime number")

#******************************************** THIRD APPROACH **************************************************
# def Prime(num,val=2):
#     if val==num//2+1:
#         return True
#     if num % val==0 or num < 2:
#         return False
#     return Prime(num, val+1)
# number=int(input("Enter a number: "))
# print(f"{number} is a Prime number" if Prime(number)==True else f"{number} is not a Prime number")

#******************************************** FORTH APPROACH ************************************************
# def Prime(num,val=2):
#     if num > 1:
#         if val==num//2+1:
#            return True
#         if num % val==0:
#            return False
#         return Prime(num, val+1)
#     return False
# number=int(input("Enter a number: "))
# print(f"{number} is a Prime number" if Prime(number)==True else f"{number} is not a Prime number")