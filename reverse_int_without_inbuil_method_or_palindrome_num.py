# Write a python program to reverse a number without typecasting and slicing

num=int(input("Enter the number: "))
dup=num
digit=len(str(num))
power=10**(digit-1)    # if num=1234 digit of 4 is 1, 3 is 10, 2 is 100, 4 is 1000. 
res=0                    #************************************************ ITERATION *****************************************************************
while num > 0:           # 1st: 1234>0 True                   2nd: num=123 123>0 True      3rd: num=12 12>0            4th: num=1 1>0
    ld = num % 10        #      ld=1234%10=4 (ld= last digit)      ld=123%10=3                  ld=12%10=2                  ld=1%10=1
    res=res + (ld*power) #      res=0+4*1000=4000                  res=4000+3*100=4300          res=4300+2*10=4320          res=4320+1*1=4321
    power=power//10      #      power=1000//10=100                 power=100//10=10             power=10//10=1              power=1//10=0
    num=num//10          #      num=1234//10=123                   num=123//10=12               num=12//10=1                num=1//10=0
print(f"The reverse of {dup} is {res}") #**************************************** 4000+300+20+1=4321 *************************************************
if dup==res:
    print(f"{dup} is a Palindrome Number")
else:
    print(f"{dup} is not a Palindrome Number")