 # Write a python program to print only uppercase alphabets from the string
S=str(input("Enter a string: "))
res=''
for ch in S:
    if ('A'<=ch<='Z'):
        res=res+ch
print(f"Uppercase letter of {S} is {res}")

