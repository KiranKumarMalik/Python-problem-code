#      *
#      * *
#      * * *
#      * *
#      *
#                                             ********************************* ITERATION ***********************************************************************************
num=int(input("Enter the number of rows: ")) # num=5
stars=1                                      # stars=1
for row in range(num):                       # 1st: row=0                       2nd: row=1            3rd: row=2             4th: row=3         5th: row=4
    for star in range(stars):                #      stars=1                          stars=2               stars=3                stars=2            stars=1
        print("*", end=" ")                  #         *                               *                     *                       *                 *    
    print()                                  # controller out from for 1st row         * * out               * *                     * *               * *
    if row<num//2:                           # 0<5//2 True                             1<5//2 True           * * * out               * * *             * * *
        stars+=1                             # stars=1+1=2                            stars=2+1=3            2<5//2 False            * * out           * *
    else:                                    #                                                               else:                   3<5//2 False      *
        stars-=1                             #                                                               stars=3-1               else             4<5//2 False
        #                                                                                                                            stars=2-1         else
        #*************************************************************************************************************************************        stars=0 stop iteration