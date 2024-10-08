#                                    Number of rows=5  Row    Spaces    Stars
#            *                 1st:          *          0        2        1
#          * * *                           * * *        1        1        3
#        * * * * *                       * * * * *      2        0        5                       Row    Spaces    Stars
#          * * *                              spaces=5//2=2                               * * *    3        1        3  
#            *                           if row<num//2=5<2 means half of the diamond        *      4        2        1
#                                            after one iteration spaces=space-1                   if row<num//2=3<5//2 False means second inverted triangle
#                                                stars=stars+2=1+2=3                               after first half iteration spaces=spaces+1   
#                                            at end iteration stars=5                                      stars=stars-2=5-2=3
num=int(input("Enter the number of row(Odd number): "))
stars=1
spaces=num//2
for row in range(num):
    for space in range(spaces):
        print(" ", end=" ")
    for star in range(stars):
        print("*", end=" ")
    print()
    if row<num//2:
        spaces-=1
        stars+=2
    else:
        spaces+=1
        stars-=2