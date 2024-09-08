# Right angled trinagle pattern
#     *
#     * * 
#     * * *
#     * * * *


n=int(input("Enter the number of rows: "))
i=0   # intializing the number of rows from 0
while i<n:      # i is the number of rows upto n
    j=0
    while j<i+1: # j is the column number upto i+1(When i=0 then j=i+1 column=1)
        print("*", end=" ")
        j+=1  # j=j+1 incrementing the column numbaer
    i+=1  #i=i+1 incrementing the row number
    print()