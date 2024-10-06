
pos=int(input("Enter a position: "))
first=0
second=1
if pos==1 or pos==2:
    print(pos-1)
else:
    for add in range(pos-2):
        nextEle=first+second
        first,second=second,nextEle
    print(nextEle)