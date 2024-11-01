# Write a program to reverse a string using positive indexing
S=str(input("Enter a string: "))
rev_S=""
for ind in range(len(S)-1,-1,-1):
    rev_S=rev_S+S[ind]
print(f"Reverse of {S} is {rev_S}")

#**************************************************** 2nd APPROACH **************************************************
# Write a program to reverse a string using negative indexing
# S=str(input("Enter a string: "))
# rev_S=""
# for ind in range(-1,-len(S)-1,-1):
#     rev_S=rev_S+S[ind]
# print(f"Reverse of {S} is {rev_S}")

#**************************************************** 3rd APPROACH **************************************************
# Write a program to reverse a string without any inbuild method
# S=str(input("Enter a string: "))
# rev_S=""
# for ch in S:
#     rev_S=ch + rev_S
# print(f"Reverse of {S} is {rev_S}")

#**************************************************** 4th APPROACH **************************************************
# # Write a program to reverse a string using While loop of negative indexing
# S=str(input("Enter a string: "))
# rev_S=""
# ind=-1
# while ind!= -(len(S)+1):
#     rev_S=rev_S+S[ind]
#     ind=ind-1
# print(f"Reverse of {S} is {rev_S}")

#**************************************************** 5th APPROACH **************************************************
# Write a program to reverse a string using While loop of positive indexing
# S=str(input("Enter a string: "))
# rev_S=""
# ind=len(S)-1
# while ind != -1:
#     rev_S=rev_S+S[ind]
#     ind=ind-1
# print(f"Reverse of {S} is {rev_S}")