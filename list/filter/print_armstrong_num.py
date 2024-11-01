# Write a ython program to print armstrong numbers in givern range
def Armstrong(num,res=0):
    dup=num
    power=len(str(num))
    while num>0:
        lastDigit=num%10
        res=res+(lastDigit**power)
        num=num//10
    return dup==res
startIndex=int(input("Enter the starting range: "))
endIndex=int(input("Enter the ending range: "))
print("Armstrong numbers are: ",list(filter(Armstrong,range(startIndex,endIndex))))