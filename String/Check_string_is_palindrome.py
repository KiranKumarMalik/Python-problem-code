# Write a program to check a given string is palindrome or not with less iterations using for loop
S=str(input("Enter a string: "))
for ind in range(0,len(S)//2):
    if S[ind] != S[-ind-1]:
        print(f"{S} is not a Palindrome String")
        break
    else:
        print(f"{S} is a Palindrome String")


# Write a program to check a given string is palindrome or not with less iterations using while loop
S=str(input("Enter a string: "))
ind=0
while ind != len(S)//2:
    if S[ind] != S[-ind-1]:
        print(f"{S} is not a Palindrome String")
        break
    ind=ind+1
else:
    print(f"{S} is a Palindrome String")