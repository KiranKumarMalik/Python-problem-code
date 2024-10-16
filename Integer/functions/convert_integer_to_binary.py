# Write a program to convert from integer to binary
def IntToBin(num,pos=1,res=0):
    while num>0:
        rem=num%2
        res=res+(rem*pos)
        pos=pos*10
        num=num//2
    return res
num=int(input("Enter an integer: "))
print(IntToBin(num))