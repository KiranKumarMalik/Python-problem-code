# Write a program to print the characters present at even index number of string using while loop.

S=str(input("Enter the string: "))
i=0                     # Initialize the index number of string element to 0
while i<len(S):         # Given the condition that index number will be less then length of string upto length of string
    if i % 2 == 0:
        print(S[i])
    i=i+1