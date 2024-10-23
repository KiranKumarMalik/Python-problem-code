# Write a recursion fuction to check the number is Happy number is not
def Square(num):
    if num<=0:
        return 0
    return (num%10)**2+Square(num//10)
def Happy(num):
    if num<10:
        return num==1 or num==7
    return Happy(Square(num))
num=int(input("Enter a number: "))
print(f"{num} is a Happy number" if Happy(num) else f"{num} is not a Happy number")


#************************************************** SECOND APPROACH ****************************************************
# def Square(num):
#     if num<=0:
#         return 0
#     return (num%10)**2+Square(num//10)
# def Happy(num):
#     if num<10:
#         return num
#     return Happy(Square(num))
# num=int(input("Enter a number: "))
# ans=Happy(num)
# if ans==1 or ans==7:
#     print(f"{num} is a Happy number")
# else:
#     print(f"{num} is not a Happy number")
