# Write a recursion functions to print all even numbers in a given range
def Sample(startNum,endNum):
    if startNum==endNum+1:
        return
    if startNum%2==0:
       print(startNum)
    Sample(startNum+1,endNum)
startNum=int(input("Enter starting number: "))
endNum=int(input("Enter ending number: "))
Sample(startNum,endNum)