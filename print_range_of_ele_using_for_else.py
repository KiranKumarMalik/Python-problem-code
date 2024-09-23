# Write a program to print the range of elements using for loop and else block

startInd=int(input("Enter the starting index number:"))
endInd=int(input("Enter the ending index number:"))

for i in range(startInd, endInd+1):
    print(i, end=" ") # Print the range of elements, end=" " is used to print the elements in the same line
else:
    print("Else block is executed") # Print this statement after the for loop is executed