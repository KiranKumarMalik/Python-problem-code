with open('sunday.txt','r') as fobj:
    countwords=0
    for line in fobj:
        countwords += len(line.split())
    print(f"Number of words in file: {countwords}")


#*************************************** Way 2 ***************************************
# with open('sunday.txt','r') as fobj:
#     countwords = len(fobj.read().split())
#     print(f"Number of words in file: {countwords}")

#*************************************** Way 3 ***************************************
# with open('sunday.txt','r') as fobj:
#     countwords=0
#     for line in fobj.readlines():
#         countwords += len(line.split())
#     print(f"Number of words in file: {countwords}")


#*************************************** Way 4 ***************************************
# with open('sunday.txt','r') as fobj:
#     countwords=0
#     for line in fobj:
#         line=line.strip()
#         for word in line.split():
#             countwords += 1
#     print(f"Number of words in file: {countwords}")