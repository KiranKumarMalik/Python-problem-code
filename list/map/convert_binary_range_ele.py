# Write a program to print binary values of given range
def Bin(num,res=0):
    pos=1
    while num>0:
        rem=num%2
        res=res+rem*pos
        pos=pos*10
        num=num//2
    return res

print(list(map(Bin,range(10,21))))