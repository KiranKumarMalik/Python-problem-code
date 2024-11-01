# def EMIRP(num,dup,res=0):
#     while num > 0:
#         ld=num%10
#         res=res*10+ld
#         num=num//10
#     if res!=dup:
#         if dup>1:
#             for val in range(2, dup//2+1):
#                 if dup%val==0:
#                     return False
#             else:
#                 if res>1:
#                     for val in range(2,res//2+1):
#                         if res%val==0:
#                             return False
#                     else:
#                         return True
#                 else:
#                     return False
#         else:
#             return False
#     else:
#         return False
# num=int(input("Enter a number: "))
# print(f"{num} is an EMIRP number" if EMIRP(num,num)==True else f"{num} is not an EMIRP number")

def isPrime(num):
    if num<=1:
        return False
    for val in range(2,num):
        if num % val==0:
            return False
    return True

def isEmirp(num,res=0):
    dup=num
    if isPrime(num)==False:
        return False
    while num>0:
        lastDigit=num%10
        res=res*10+lastDigit
        num=num//10
    return dup != res and isPrime(res)
num=int(input("Enter a number: "))
if isEmirp(num):
    print(f"{num} is EMIRP number")
else:
    print(f"{num} is not EMIRP number")