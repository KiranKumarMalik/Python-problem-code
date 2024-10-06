# Write a program to check the number is perfect square or not
# Exp: 49 beacuse 7*7=49 like that 2*2=4, 3*3=9, 4*4=16, 5*5=25, etc. 
num=int(input("Enter a number: "))            #******************************** ITERATION ******************************************    
val=0                                         #  num=4
while val*val<=num:                           # 1st: 0*0<=4 True           2nd:1*1<=4 True              3rd: 2*2=4 True
    if val * val==num:                        #      0*0==4 False              1*1==4 False                  2*2==4 True
        print(f"{num} is a Perfect Square")   #      Not execute Perfect num   Not execute Perfect num       Execute Perfect number
        break                                 #      out of the if condition   out of the if condition     Stop the execution
    val=val+1                                 #    val=0+1=1                 val=1+1=2                     
else:                                         # ************************************************************************************
    print(f"{num} is not a Perfect Square")