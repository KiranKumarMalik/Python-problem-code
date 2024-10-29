# Write a python program to check an input number is wheather armstrong number or not
#armstrong: num=153, so digit is 3 then (1)**3, (5)**3, (3)**3
num=int(input("Enter the number: "))
copy=num         # storing the value of num in a duplicate variable
res=0                                #******************************************** ITERATION **********************************************
power=len(str(num))                  # if num=153 then number of digit=3, so (1)**3, (5)**3, (3)**3
while num>0:                         #iteration:  1st: num=153               2nd: num=15                3rd: num=1
    lastdigit=num%10                 #                 lastdigit=153%10=3         lastdigit=15%10=5          lastdigit=1%10=1
    res=res+(lastdigit**power)       #                 res=0+(3**3)=27            res=27+(5**3)=152          res=152+(1**3)=153
    num=num//10                      #                 num=153//10=15             num=15//10=1               num=1//10=0
if copy==res:                        #*****************************************153= ((1)**3)+((5)**3)+((3)**3) ****************************
    print(f"{copy} is an Armstrong Number")
else:
    print(f"{copy} is not an Armstrong Number")