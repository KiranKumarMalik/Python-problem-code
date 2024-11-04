
S=str(input("Enter a string: "))
res=''
for ch in S:
    if ('A'<=ch<='Z') or ('a'<=ch<='z') or ('0'<=ch<='9'):
        pass
    else:
        res=res+ch
print(f"Uppercase letter of {S} is {res}")

# S=str(input("Enter a string: "))
# res=''
# for ch in S:
#     if not('A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9'):
#         res=res+ch
# print(f"Uppercase letter of {S} is {res}")

