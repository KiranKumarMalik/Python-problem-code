words=['JAVA', 'MOM', 'DAD', 'sister', 'php']

# Start with empty list
palindromes = []

# Iterate over each word
for word in words:
    # Check if word is equal to same word in reverse order
    is_palindrome = (word == word[::-1])

    # Append to results if needed
    if is_palindrome:
        palindromes.append(word)

print(palindromes)