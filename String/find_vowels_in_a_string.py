# Write a python program to print the vowels in a string

S=str(input("Enter a string: "))
for ch in S:
    if ch in "aeiouAEIOU":
        print(ch,end="")


# S=str(input("Enter a string: "))
# res=""
# for ch in S:
#     if ch in "aeiouAEIOU":
#         res=res+ch
# print(res)
