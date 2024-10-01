# Write a python program to check the number is disarm number or not. means: 135=(1)**1 + (3)**2 + (5)**3

num=int(input("Enter the number: "))
dup=num
res=0                           #**************************************** ITERATION **************************************#
power=len(str(num))             # if num=135 then number of digit=3, so power=3                                           #
while num>0:                    #iteration:  1st: num=135               2nd: num=13                3rd: num=1             #
    ld=num%10                   #        ld=lastdigit=135%10=5               ld=13%10=3                 ld=1%10=1         #
    res=res+(ld**power)         #                 res=0+5**3=125             res=125+3**2=134           res=134+1**1      #
    power=power-1               #                 power=3-1=2                power=2-1=1                power=1-1=0       #
    num=num//10                 #                 num=135//10=13             num=13//10=1               num=1//10=0       #
if dup==res:                    #******************************** 135=(1)**1 + (3)**2 + (5)**3 ***************************#
    print(f"{dup} is a disarm number")
else:
    print(f"{dup} is not a disarm number")