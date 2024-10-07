num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1>num2:
    gcd=num1
else:
    gcd=num2
while True:
    if num1 % gcd==0 and num2 % gcd==0:
        print(gcd)
        break
    else:
        gcd=gcd-10