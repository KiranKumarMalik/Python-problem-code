S=str(input("Enter a string: "))
res=''
for ch in S:
    if ('0'<=ch<='9'):
        res=res+ch
print(f"Numbers are availabe in {S} is {res}")
