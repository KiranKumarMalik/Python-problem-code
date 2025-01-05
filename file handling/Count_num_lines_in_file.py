with open('sunday.txt','r') as fobj:
    countlines=0
    for line in fobj:
        countlines += 1
    print(f"Number of lines in file: {countlines}")


# Way 2
# with open('sunday.txt','r') as fobj:
#     countlines = len(fobj.readlines())
#     print(f"Number of lines in file: {countlines}")