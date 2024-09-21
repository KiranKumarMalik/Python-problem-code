# Write a Python program to print even numbers in reverse order in a given range using for loop.

startIndex=int(input("Enter the starting index (it must greater than endIndex): "))
endIndex=int(input("Enter the ending index (it must smaller than endIndex): "))

for i in range(startIndex, endIndex, -1): # -1 is used to print the numbers in reverse order using slicing concept
    if i % 2 ==0:
        print(i)