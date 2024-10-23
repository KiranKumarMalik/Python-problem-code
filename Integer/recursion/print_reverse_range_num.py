# Write a python program to print the user input reverse order of range
def Sample(startNum,endNum):
    if startNum==endNum-1:
        return
    print(startNum)
    Sample(startNum-1,endNum)
startNum=int(input("Enter starting number: "))
endNum=int(input("Enter ending number: "))
Sample(startNum,endNum)