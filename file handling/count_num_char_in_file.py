# Write a program to count the number of characters in a file.
with open('sunday.txt','r') as fobj:
    countchar=0
    for line in fobj:
        line=line.strip('\n')
        countchar += len(line)
    print(f"Number of characters in file: {countchar}")

