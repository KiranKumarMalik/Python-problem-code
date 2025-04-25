# This program replaces all occurrences of a specified character in a string with another character.
# It takes input from the user for the string, the character to be replaced, and the replacement character.

S = input("Enter a String: ")
old_key = input("Enter the character to replace: ")
replace_key = input("Enter the replacement character: ")

# Initialize an empty string to build the result
new_string = ""

for ch in S:
    if ch == old_key:
        new_string += replace_key  # Replace character
    else:
        new_string += ch  # Keep original character

print("Result:", new_string)
