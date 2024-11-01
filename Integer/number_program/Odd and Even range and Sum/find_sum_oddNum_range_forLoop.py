# Write a Python program to find the sum of all odd numbers in a range using for loop.

startIndex=int(input("Enter the starting index(it must be smaller than endIndex): "))
endIndex=int(input("Enter the ending index(it must be greater than startIndex): "))

sum=0
for i in range(startIndex, endIndex+1):
    if i % 2 != 0:
        sum=sum+i
print(f"The sum of odd numbers between {startIndex} and {endIndex} is {sum}")