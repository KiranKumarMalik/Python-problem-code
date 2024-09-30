# Write a program to print the words from the string whose length is greater than 3

S="Hello what is your name"
words=S.split()
for i in words:
    if len(i)>3:
        print(i)