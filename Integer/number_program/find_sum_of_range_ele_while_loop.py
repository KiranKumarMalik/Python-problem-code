# Write a program to find the sum of range elements using while loop.

startNum=int(input("Enter the Starting number: ")) 
endNum=int(input("Enter the Ending number: "))
sum=0

while startNum<endNum: # Given the condition that startNum will be less then endNum upto endNum
    sum=sum+startNum # sum=0+1=1, sum=1+2=3, sum=3+3=6, sum=6+4=10
    startNum=startNum+1 # startNum=1+1=2, startNum=2+1=3, startNum=3+1=4
print("The sum of range element is: ",sum)