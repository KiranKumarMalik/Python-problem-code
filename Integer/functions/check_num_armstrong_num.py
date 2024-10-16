# Write a function to check the number is Armstrong number or not
def Armstrong(num,res=0):
    dup=num
    power=len(str(num))
    while num>0:
        lastDigit=num%10
        res=res+(lastDigit**power)
        num=num//10
    if dup==res:
        return f"{dup} is an Armstrong Number"
    else:
        return f"{dup} is not an Armstrong Number"
num=int(input("Enter a number: "))
print(Armstrong(num))


#*************SECOND APPROACH************
#def Armstrong(num,power,res=0):
#    while num>0:
#        lastDigit=num%10
#       res=res+(lastDigit**power)
#       num=num//10
#    return res
#num=int(input("Enter a number: "))
#if Armstrong(num, len(str(num)))==num:
#    print(f"{num} is an Armstrong number")
#else:
#    print(f"{num} is not an Armstrong number")

#*************THIRD APPROACH************
#def Armstrong(num,copy,power,res=0):
#    while num>0:
#        lastDigit=num%10
#       res=res+(lastDigit**power)
#       num=num//10
#    return res==copy
#num=int(input("Enter a number: "))
#print('Armstrong' if Armstrong(num,num,len(str(num))) else 'Not Armstrong')