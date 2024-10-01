num=int(input("Enter the number: "))
dup=num
val=1
count=0
res=0
power=len(str(num))
while val<=num:
    if num%val==0:
        count=count+1
    val=val+1
if count==2:
    while num>0:
        ld=num%10
        res=res*10+ld
        num=num//10
    if dup==res:
        print (f"{dup} is a Polyprime Number")
    else:
        print(f"{dup} is not a Polyprime Number")