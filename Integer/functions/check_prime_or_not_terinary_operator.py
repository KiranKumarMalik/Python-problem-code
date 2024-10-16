def prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return False
        return True
    return False
num=int(input("Enter a number"))
print(f"{num} is a Prime number" if prime(num) else f"{num} is not a Prime number")