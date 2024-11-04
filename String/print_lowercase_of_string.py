# Write a python program to print only lowercase alphabets from the string

S=str(input("Enter a string: "))
res=''
for ch in S:
    if ('a'<=ch<='z'):
        res=res+ch
print(f"Lowercase letter of {S} is {res}")
