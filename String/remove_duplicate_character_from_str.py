S=str(input("Enter a string: "))
res=""
for ch in S:
    if ch not in res:
        res=res+ch
print(f"After removing duplicate character {res}")