# Write a program to print first N natural number in reverse order.
num=int(input("Enter the number of natural number: "))

for i in range(num, 0, -1): # num is the ending index, upto num, -1 is the decrement value
    print(i)