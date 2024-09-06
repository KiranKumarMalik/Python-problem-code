# Right angled trinagle pattern
#     *
#     * * 
#     * * *
#     * * * *

n= int(input("Enter the number of rows: "))

for i in range(n):   # i is the row number upto n (in range if n=5 then i=0,1,2,3,4 because range is exclusive)
    for j in range(i+1):   # j is the column number upto i+1(When i=0 then j=i+1 column=1)
        print("*", end=" ") # end=" " is used to print in the same line
    print()