# Write a program to print all the sub palindrom strings

S=str(input("Enter a string: ")) # input=mama
res=[]   
for startIndex in range(0,len(S)):
    for endIndex in range(startIndex+1,len(S)+1):
        S2=S[startIndex:endIndex]
        if S2==S2[::-1]:
            res.append(S2)
print(res)
