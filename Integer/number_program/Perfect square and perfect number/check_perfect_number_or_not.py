# Write a python program to check the number wheather it is perfect number or not
# Exp: num = 6 => 1+2+3=6 => 6 is a perfect number 
num=int(input("Enter the number: "))    #******************************************* ITERATION **********************************************************
sum=0                                   # num=6
for val in range(1,num):                # 1st: val=1           val=2          val=3      val=4           val=5                     out from the for loop
    if num % val==0:                    #      6 % 1==0 True   6 % 2==0 True  6 % 3==0   6 % 4==0 False  6 % 5==0 False            _
        sum=sum+val                     #      sum=0+1=1       sum=1+2=3      sum=3+3=6                  out from the if condition _
if sum==num:                            #                                                                                          sum==num 6=6
    print("The number is Perfect number")#                                                                                         Perfect number
else:                                    #***************************************************************************************************************
    print("The number is not Perfect number")