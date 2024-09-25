# Write a Python program to print all the programming languages that start with the letter "P" or "p".

lang=["python","java","perl","php","JavaScript","C++","Ruby","Python"]
for language in range(len(lang)):
    if lang[language].startswith('p') or lang[language].startswith('P'):  # startswith() is a built-in function in Python used to check if a string starts with a specific prefix or not.
     print(lang[language])