def Square(num,res=0):
    while num>0:
        lastDigit=num%10
        res=res+lastDigit**2
        num=num//10
    return res
def Happy(num):
    while num>9:
        num=Square(num)
    return num==1 or num==7
startIndex=int(input("Enter the starting range: "))
endIndex=int(input("Enter the ending index: "))
print("Happy numbers are: ",list(filter(Happy,range(startIndex,endIndex+1))))