# Write a Python program to print the factors of a given number using for loop
num=int(input("Enter an Interger number: "))

for i in range (1, num+1): # if num=10 then the factors may be in range of 1 to 10, so we take increment as num+1=11
    if num % i == 0: # 10 % 1=0 factor=1, 10 % 2=0 factor=2, 10 % 5=0 factor=5, 10 % 10=0 factor=10
        print(i) # print the factors of the number