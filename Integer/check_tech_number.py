# Write a python program to check the number is Tech number or not
# num=2025
# S=str(num)="2025"
# firsthalf=20
# secondhalf=25
# sum=20+25=45
# square=45**2
# check 45**2==num (Teach number otherwise not a tech number)

num=int(input("Enter a number: "))
S=str(num)
firstNum=int(S[:len(S)//2])
secondNum=int(S[len(S)//2:])
sum=firstNum+secondNum
square=sum**2
if square==num:
    print(f"{num} is a Tech number")
else:
    print(f"{num} is not a tech number")