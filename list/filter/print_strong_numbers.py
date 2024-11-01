def Factorial(num,fact=1):
    for val in range(1,num+1):
        fact=fact*val
    return fact
def Strong(num,res=0):
    dup=num
    while num>0:
        lastDigit=num%10
        res+=Factorial(lastDigit)
        num=num//10
    return res==dup
startIndex=int(input("Enter the starting range: "))
endIndex=int(input("Enter the ending index: "))
print("Strong numbers are: ",list(filter(Strong,range(startIndex,endIndex))))