# Write a Python Program to convert binary to integer.
binNum=int(input("Enter a binary number: "))
dup=binNum
power=0
res=0
while binNum>0:
    ld=binNum%10
    res=res+(ld*(2**power))
    power=power+1
    binNum=binNum//10
print(f"{dup} = {res}")