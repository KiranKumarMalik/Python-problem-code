# Write a Python program to print odd numbers in reverse order in a given range.

startIndex=int(input("Enter the starting index(it must be the greater than endIndex): "))
endIndex=int(input("Enter the ending index(it must be the smaller than startIndex): "))

for i in range(startIndex, endIndex, -1): # -1 is used to print the numbers in reverse order using slicing concept
    if i % 2 != 0: 
        print(i)