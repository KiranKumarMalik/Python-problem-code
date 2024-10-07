# Write a program that uses a while loop to print every character of a string, one character per line.
S=str(input("Enter a string: "))
i=0                       # Initialize the index number of string element to 0
while i<len(S):           # Given the condition that index number will be less then length of string upto length of string
    print(S[i])
    i=i+1