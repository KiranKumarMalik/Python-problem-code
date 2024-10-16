# Write a python program to check the number is Prime or not by using function
def Prime(num, count=0):
    for val in range(1, num+1):
        if num%val==0:
            count=count+1
    if count==2:
        return f"{num} is a Prime number"
    else:
        return f"{num} is not a Prime number"
num=int(input("Enter a number: "))
print(Prime(num))


