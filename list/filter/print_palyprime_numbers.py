# Write a program to print palyprime numbers in a given range using filter condition
def Prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return False
        return True
def Palindrome(num,res=0):
    dup=num
    while num != 0:
        lastDigit=num%10
        res=res*10+lastDigit
        num=num//10
    return res==dup
def palyprime(num):
    return Prime(num) and Palindrome(num)
startIndex=int(input("Enter the starting range: "))
endIndex=int(input("Enter the ending index: "))
print("Palyprime numbers are:",list(filter(palyprime,range(startIndex,endIndex))))