# Count Digits in a Number: Write a Python program using a for loop to count the number of digits in a given integer N.

num=int(input("Enter the number: "))
converStr=str(num)
count=0
for i in converStr:
    count=count+1
print(f"{num} is a {count} digit number")