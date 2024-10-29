# Write a Python function to check if a given string is a palindrome or not.

def check_palindrome(S):
    if S == S[::-1]: # chek if the string is equal to its reverse
        print (f"{S} is a palindrome")
    else:
        print (f"{S} is not a palindrome")

S=str(input("Enter a String:"))
check_palindrome(S)
