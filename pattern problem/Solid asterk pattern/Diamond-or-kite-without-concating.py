num = 5
spaces = num // 2
stars = 1
for row in range(num):
    for sp in range(spaces):
        print(' ',end = ' ')
    for st in range(stars):
        if st % 2 == 0:
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()
    if row < num // 2:
        spaces -= 1
        stars += 2
    else:
        spaces += 1
        stars -= 2