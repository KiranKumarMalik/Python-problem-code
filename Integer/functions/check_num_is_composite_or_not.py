def Composite(num,countfactor=0):
    for i in range(1, num+1):
        if num % i == 0: # 10 % 1=0 factor=1, 10 % 2=0 factor=2, 10 % 5=0 factor=5, 10 % 10=0 factor=10
            countfactor=countfactor+1 # count the factors of the number
    if countfactor > 2: # countfactor>2 means the number is divisible by more than 2 numbers
        return True
    else:
        return False
num=int(input("Enter a number: "))
print(f"{num} is a Composite number" if Composite(num)==True else f"{num} is not a Composite number")