# Write a Python program to find the words which starts with a vowel in a given string.

orgStr=str(input("Enter the original string: "))
vowelWord=[]

split_str=orgStr.split()  # First we have to split the words from the string 
for word in split_str:
    if word[0] in 'aeiouAEIOU':
        vowelWord.append(word)
print(vowelWord)