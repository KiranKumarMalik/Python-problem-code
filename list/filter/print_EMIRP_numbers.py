def isPrime(num):
    if num<=1:
        return False
    for val in range(2,num):
        if num % val==0:
            return False
    return True

def isEmirp(num,res=0):
    dup=num
    if isPrime(num)==False:
        return False
    while num>0:
        lastDigit=num%10
        res=res*10+lastDigit
        num=num//10
    return dup != res and isPrime(res)
startIndex=int(input("Enter the starting range: "))
endIndex=int(input("Enter the ending index: "))
print("EMIRP numbers are: ",list(filter(isEmirp,range(startIndex,endIndex))))