# Write a program to print all the sub-strings without slicing

S=str(input("Enter a string: "))
for startIndex in range(0,len(S)):
    for endIndex in range(startIndex+1,len(S)+1):
        for ind in range(startIndex,endIndex):
            print(S[ind],end="")
        print()


# S=str(input("Enter a string: "))
# for startIndex in range(0,len(S)):
#     for endIndex in range(startIndex+1,len(S)+1):
#         var=''
#         for ind in range(startIndex,endIndex):
#             var=var+S[ind]
#         print(var)