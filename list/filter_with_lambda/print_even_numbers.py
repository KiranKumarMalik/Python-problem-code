# Write a program to print even numbers in a given range using filter function
startIndex=int(input("Enter the starting range: "))
endIndex=int(input("Enter the ending index: "))
print(list(filter(lambda num:num % 2 == 0,range(startIndex,endIndex+1))))

# print(list(filter(lambda num:True if num % 2==0 else False,range(startIndex,endIndex+1))))