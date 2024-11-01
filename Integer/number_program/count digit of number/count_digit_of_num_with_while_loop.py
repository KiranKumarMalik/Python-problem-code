# Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.

num=int(input("Enter the number: "))
convertStr=str(num) # Convert sigle valued datatype to collection datatype that is integer to string
count=0   # count the number of digits
ind=0     # initializing the index position of the string elements
while ind<len(convertStr):
    count=count+1    # increment the count by 1
    ind=ind+1        # increment the index by 1
print(f"{num} is a {count} digit number")