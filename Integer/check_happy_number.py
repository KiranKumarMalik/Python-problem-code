# Write a python program to check the number is Happy number or not
#                                     **************************************** ITERATION **************************************************
num=int(input("Enter a number: "))    # num=13
dup=num                               # 1st:                                                     2nd: 
while num>9:                          #     while 13>9: TRUE     
    res=0                             #           res=0
    while num>0:                      #     while 13>0: TRUE                                         while 10>0: TRUE 
        ld=num%10                     #           ld=13%10=3     ld=1%10=1                                 ld=10%10=0     ld=1%10=1
        res=res+ld**2                 #          res=0+3**2=9   res=9+1**2=10                              res=0+0**2=0  res=0+1**2=1
        num=num//10                   #          num=13//10=1   num=1//10=0                                num=10//10=1  num=1//10=0 (iteration stops)
    num=res                           #                         num=res=10(it will be next num)                          num=res=1
if num==1 or num==7:                  #    
    print(f"{dup} is a Happy Number") #********************************** num=1    =)1=1(Happy number) ************************************
else:
    print(f"{dup} is not a Happy Number") 