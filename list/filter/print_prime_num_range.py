def prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return False
        return num
    return False
startIndex=int(input("Enter the starting range: "))
endIndex=int(input("Enter the ending range: "))
print("Prime numbers are: ",list(filter(prime,range(startIndex,endIndex))))