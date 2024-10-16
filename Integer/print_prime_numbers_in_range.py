# Write a program to print the prime numbers in given range
lower_range=int(input("Enter the starting range: "))
upper_range=int(input("Enter the ending range: "))

for num in range(lower_range,upper_range+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)