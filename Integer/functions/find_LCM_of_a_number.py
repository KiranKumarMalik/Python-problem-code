def LCM(num1,num2):
    if num1>num2:
        lcm=num1
    else:
        lcm=num2
    while True:
        if lcm % num1==0 and lcm % num2==0:
            return lcm
        else:
            lcm=lcm+1
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print(f"The lCM of {num1} and {num2} is {LCM(num1,num2)}")