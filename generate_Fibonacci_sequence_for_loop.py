pos=int(input("Enter the number of postion upto you have to generate series: "))
first=0
second=1
for add in range(pos):
    print(first, end=" ")
    nextEle=first+second
    first,second=second,nextEle