# Wtite a program to find HCF of two number
def HCF(num1,num2):
    if num1>num2:
        hcf=num1
    else:
        hcf=num2
    while True:
        if num1 % hcf==0 and num2 % hcf==0:
            return hcf
        else:
            hcf=hcf-10
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print(f"The HCF is {HCF(num1,num2)}")