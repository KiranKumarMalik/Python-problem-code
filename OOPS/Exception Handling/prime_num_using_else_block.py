num=int(input("Enter a number: "))
try:
    if num > 1:
        for val in range(2, num//2+1):
            if num%val==0:
                raise Exception
    else:
        raise Exception
except:
    print("Not a Prime Number")
else:
    print("Prime Number")
finally:
    print("Execution Completed")