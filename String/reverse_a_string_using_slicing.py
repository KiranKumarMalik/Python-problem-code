# Write a Python function to reverse a given string using slicing.

def reverse_string(S):
    return S[::-1] # Return the reverse of the string

S=str(input("Enter a string: "))
print(reverse_string(S))