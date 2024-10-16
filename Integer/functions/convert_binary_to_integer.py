# Write a program to convert binary number to integer using function
def BinToInt(binNum,power=0,res=0):
    while binNum>0:
        lastDigit=binNum%10
        res=res+(lastDigit*(2**power))
        power=power+1
        binNum=binNum//10
    return res
binNum=int(input("Enter Binary number: "))
print(BinToInt(binNum))