# Write  a python program to print only alphabets from a string

S=str(input("Enter a string: "))
res=""
for ch in S:
    if ('A'<=ch<='Z') or ('a'<=ch<='z'):
        res=res+ch
print(f"Alphabets in {S} is {res}")