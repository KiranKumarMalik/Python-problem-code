# Write a function to check the number is Disarm or not
def DisArm(num,power,res=0):
    while num>0:
        lastDigit=num%10
        res=res+(lastDigit**power)
        power=power-1
        num=num//10
    return res
num=int(input("Enter a number: "))
if DisArm(num,len(str(num)))==num:
    print(f"{num} is a Disarm number")
else:
    print(f"{num} is not a Disarm number")