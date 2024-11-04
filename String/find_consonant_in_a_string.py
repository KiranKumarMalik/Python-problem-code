# Write a python program to print the consonants from the string.

# S=str(input("Enter a string: "))
# for ch in S:
#     if ch not in "aeiouAEIOU ":
#         print(ch,end="")

S=str(input("Enter a string: "))
res=""
for ch in S:
    if ('A'<=ch<='Z') or ('a'<=ch<='z'):
        if ch not in "aeiouAEIOU":
            res=res+ch
print(f"Consonants in {S} is {res}")