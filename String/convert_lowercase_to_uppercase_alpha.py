# Write a program to convert lowercase character to uppercase in a string

S=str(input("Enter a string: "))
res=""
for ch in S:
    if 'a'<=ch<='z':
        res=res+chr(ord(ch)-32) # chr() is used to convert ASCII value to character and ord() is used to convert character to ASCII value
    else:
        res=res+ch
print(f"Uppercase of {S} is {res}")