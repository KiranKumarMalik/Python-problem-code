# Write a Python program to check whether a number is Composite or not using for loop.

num=int(input("Enter an Integer number: "))
countfactor=0

for i in range(1, num+1):
    if num % i == 0: # 10 % 1=0 factor=1, 10 % 2=0 factor=2, 10 % 5=0 factor=5, 10 % 10=0 factor=10
        countfactor=countfactor+1 # count the factors of the number
if countfactor > 2: # countfactor>2 means the number is divisible by more than 2 numbers
    print(f"{num} is a Composite number")
else:
    print(f"{num} is not a Composite number")


# num = int(input("Enter a number: "))
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1
# if count > 2:
#     print(f"{num} is a Composite Number")
# elif count == 2:
#     print(f"{num} is a Prime Number")
# else:
#     print(f"{num} is not a Prime or Composite Number")
