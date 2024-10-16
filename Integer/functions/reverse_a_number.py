# Write a program to reverse a number using function
def Reverse(num,res=0):
    while num>0:
        lastDigit=num%10
        res=res*10+lastDigit
        num=num//10
    return res
num=int(input("Enter a number: "))
print(f"The reverse of {num} is {Reverse(num)}")