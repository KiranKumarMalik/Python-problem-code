S=str(input("Enter a string: "))
for startIndex in range(0,len(S)):
    for endIndex in range(startIndex+1,len(S)+1):
        print(S[startIndex:endIndex])