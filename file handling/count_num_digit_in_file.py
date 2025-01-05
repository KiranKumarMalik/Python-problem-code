with open('sunday.txt','r') as fobj:
    countdigit=0
    for line in fobj:
        line=line.strip('\n')
        for digit in line:
            if '0' <= digit <= '9':
                countdigit += 1
print(f"Number of characters in file: {countdigit}")