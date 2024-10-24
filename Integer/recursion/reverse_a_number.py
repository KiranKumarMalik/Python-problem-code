# # Write a recursion fuction to reverse a number
# def Reverse(num,res):
#     if num==0:
#         return res
#     return Reverse(num//10,res*10 + num%10)
# number = int(input("Enter number: "))
# # we read number from user and then pass this number to recursive function reverse()
# print(f"Reverse of {number} is {Reverse(number,0)}")


def Reverse(num,pos):
    if num==0:
        return 0
    return (num%10)*pos + Reverse(num//10,pos//10)
num=int(input("Enter a number: "))
print(f"Reverse of {num} is {Reverse(num,10**(len(str(num))-1))}")