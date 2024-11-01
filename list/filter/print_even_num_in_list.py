# Write a python program to print the even numbers in given range using filter function
def Even(num):
    if num%2==0:
        return num
startIndex=int(input("Enter the starting range: "))
endIndex=int(input("Enter the ending index: "))
print(list(filter(Even,range(startIndex,endIndex))))