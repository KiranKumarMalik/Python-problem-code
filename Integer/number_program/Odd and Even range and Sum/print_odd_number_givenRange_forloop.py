# Write a program to print all odd numbers in a range using for loop.

startIndex=int(input("Enter the starting index: "))
endIndex=int(input("Enter the ending index: "))

for i in range(startIndex, endIndex+1): # if range is between 1 to 10, then we have to give startIndex as 1 and endIndex as 11
    if i % 2 != 0: # i % 2 != 0 means i is not divisible by 2 to check if i is odd
        print(i)