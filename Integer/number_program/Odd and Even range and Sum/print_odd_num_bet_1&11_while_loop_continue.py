# Write a program to print all odd numbers between 1 and 11 or given user input by using while continue

numRange=int(input("Enter the number upto end range: "))
startNum=1
while startNum <= numRange:  # startNum is the start range number upto end range number, it will iterate upto end range number
    if startNum % 2==0:
        startNum+=1
        continue  # continue will skip all the even number checking iteration
    print(startNum)
    startNum+=1