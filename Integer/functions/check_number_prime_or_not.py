# Write a python program to check the number is Prime Number or not using function
def prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return f"{num} is not a Prime number"
        return f"{num} is a Prime number"
    return f"{num} is not a Prime"
print(prime(17))