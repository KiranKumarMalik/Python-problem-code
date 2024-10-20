def PerfectSquare(num,val=0):
    while val*val<=num:
        if val*val==num:
            return True
        val=val+1
    else:
        return False
num=int(input("Enter a number: "))
print(f"{num} is a Perfect number" if PerfectSquare(num)==True else f"{num} is not a Perfect number")