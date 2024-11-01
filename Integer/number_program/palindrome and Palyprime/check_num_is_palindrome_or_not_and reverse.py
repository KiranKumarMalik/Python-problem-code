# Write a python program to find the reverse if an integer and check wheather number is palindrome or not
#  If num=123  3 is in 1 place, 2 is in 10th place, 1 is in 100th place. if we reverse then we have to make 3 in 100th place, 2 in 10th place and 1 in 1 place
num=int(input("Enter the number: "))
dup=num
res=0                                          #************************* ITERATION *********************************
while num>0:                                   # 1st: num=171          2nd: num=17           3rd: num=1
    ld=num%10                                  #       ld=171%10=1           ld=17%10=7            ld=1%10=1
    res=res*10+ld                              #      res=0*10+1=1           res=1*10+7=17        res=17*10+1=171
    num=num//10                                #      num=171//10=17         num=17//10=1         num=1//10=0
print(f"Reverse of {dup} is {res}")            #*********************************************************************
if dup==res:
    print(f"{dup} is a Palindrome number")
else:
    print(f"{dup} is not a Palindrome number")