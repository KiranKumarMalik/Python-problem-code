# Write a python program to find LCM of two number
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1>num2:
    lcm=num1
else:
    lcm=num2
while True:
    if lcm % num1==0 and lcm % num2==0:
        print(lcm)
        break
    else:
        lcm=lcm+1
