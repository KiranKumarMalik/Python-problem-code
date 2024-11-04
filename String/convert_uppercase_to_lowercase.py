# Write a program to convert uppercase character to lowercase in a string

S=str(input("Enter a string: "))
res=""
for ch in S:
    if 'A'<=ch<='Z':
        res=res+chr(ord(ch)+32) # chr() is used to convert ASCII value to character and ord() is used to convert character to ASCII value
    else:
        res=res+ch
print(f"Lowercase of {S} is {res}")