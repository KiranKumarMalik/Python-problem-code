def Fibonacci(pos,first=0,second=1):
    for add in range(pos):
        return first
    nextEle=first+second
    first,second=second,nextEle
pos=int(input("Enter the position upto the sequence will generate: "))
print(Fibonacci(pos))