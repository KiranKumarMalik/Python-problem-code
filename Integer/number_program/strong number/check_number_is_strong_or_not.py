# Write a python program to check the input number is Strong or not
#Strong number: num=145 1!+4!+5!=num then it is a strong number

num=int(input("Enter the number: "))
dup=num                            # If num=145
res=0                              #****************************************** ITERATION ******************************************
while num>0:                       #  1st: 145>0 TRUE          
    ld=num%10                      #       ld=145%10=5           (for loop iteration upto range 5(last digit of 145)) 
    fact=1                         #     fact=1                  fact=1        fact=2       fact=6       fact=24         
    for val in range(1,ld+1):      #      val=1                  val=2          val=3        val=4        val=5 (here loop ends)           
        fact=fact*val              #      fact=1*1=1             fact=1*2=2    fact=2*3=6   fact=6*4=24  fact=24*5=120
    res=res+fact                   #                                                                      res=0+120=120
    num=num//10                             #                                                             num=145//10=14
if dup==res:                                #  2nd: ld=14%10=4 (for loop iteration upto range 4(last digit of 14))
    print(f"{dup} is a strong number")      #       fact=1        fact=1       fact=2       fact=6
else:                                       #        val=1         val=2        val=3        val=4 (here loop ends)
    print(f"{dup} is not a strong number")  #       fact=1*1=1    fact=1*2=2   fact=2*3=6   fact=6*4=24
#                                                                                            res=120+24=144
#                                                                                            num=14//10=1                                             
# 3rd: ld=1%10=1  (for loop iteration upto range 1(last digit of 1))
#      fact=1
#       val=1  (Here iteration totaly terminates)
#      fact=1*1=1
#       res=144+1=145
#       num=1//14=0