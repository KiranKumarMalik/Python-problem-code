# To filter the palindrome words from the list

# Create a list 'texts' containing strings
texts = ['JAVA', 'MOM', 'DAD', 'sister', 'php']

# Display a message indicating that the following output will show the original list of strings
print("Orginal list of strings:")
print(texts)  # Print the contents of the 'texts' list

# Use the 'filter()' function with a lambda function to filter palindromes from the list
# Filter elements from 'texts' using the lambda function to keep strings that are palindromes
# The lambda function checks if a string is equal to its reverse by joining its characters in reverse order
result = list(filter(lambda x: (x == "".join(reversed(x))), texts))

# Display the list of palindromes obtained from the original list of strings
print("\nList of palindromes:")
print(result)  # Print the filtered 'result' list 