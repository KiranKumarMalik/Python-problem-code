# Write a program to print the range of elements using for loop and break statement. Also, print the else block of the for loop.

startInd=int(input("Enter the starting index number: "))
endInd=int(input("Enter the ending index number: "))

for i in range(startInd, endInd+1):
    print(i)
    break
else:                       # else block is not executed as the break statement is used in the for loop
    print("Else block is executed") 