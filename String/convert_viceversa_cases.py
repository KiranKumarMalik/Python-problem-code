# Write a program to convert the upppercase character to lowercase and lowercase to uppercase in a string.

S=str(input("Enter a string: "))
res=""
for ch in S:
    if 'A'<=ch<='Z':
        res=res+chr(ord(ch)+32) # chr() is used to convert ASCII value to character and ord() is used to convert character to ASCII value
    elif 'a'<=ch<='z':
        res=res+chr(ord(ch)-32)
    else:
        res=res+ch
print(res)