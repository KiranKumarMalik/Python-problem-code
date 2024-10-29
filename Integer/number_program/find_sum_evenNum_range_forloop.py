startIndex=int(input("Enter the starting index(it must be smaller than endIndex): "))
endIndex=int(input("Enter the ending index(it must be greater than startIndex): "))
sum=0
for i in range(startIndex, endIndex+1):
    if i % 2 == 0: # if range is between starting Index=5 to Ending Index=20, then we have to give startIndex as 5 and endIndex as 21
        sum=sum+i # sum 
print(f"The sum of even numbers between {startIndex} and {endIndex} is {sum}")