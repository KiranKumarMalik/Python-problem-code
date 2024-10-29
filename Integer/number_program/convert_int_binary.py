# Write a python program to convert interger into the binary number
num=int(input("Enter the Integer number: "))
pos=1                    #******************************************* ITERATION ************************************************
res=0                    # if num=21
while num>0:             # 1st: 21>0 TRUE     10>0             5>0
    rem=num%2            #     rem=21%2=1     rem=10%2=0       rem=5%2=1
    res=res+rem*pos      #     res=0+1*1=1    res=1+0*10=1     
    pos=pos*10           #     pos=1*10=10    pos=10*10=100
    num=num//2           #     num=21//2=10   num=10//2=5
print(res)