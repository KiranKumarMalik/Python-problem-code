# Write a python program to check the number is wheather the number is Palyprime or not.
# Palyprine: the number which is both the prime number and palindrome number
num=int(input("Enter the number: "))
dup=num
val=1
count=0
res=0
while val<=num:
    if num%val==0:      # Checking prime or not condition
        count=count+1
    val=val+1
if count==2:                #*********************** ITERATION ***********************************
    while num>0:            # 1st: num=313           2nd: num=31           3rd: num=3            #
        ld=num%10           #       ld=313%10=3            ld=31%10=1            ld=3%10=3       # ld=last Digit
        res=res*10+ld       #      res=0*10+3=3           res=3*10+1=31         res=31*10+3=313  #
        num=num//10         #      num=313//10=31         num=31//10=3          num=3//10=0      #
    if dup==res:            #************************** dup=res 313=313 **************************
        print (f"{dup} is a Palyprime Number")
    else:
        print(f"{dup} is not a Palyprime Number")
else:
    print(f"{dup} is not a Palyprime Number")