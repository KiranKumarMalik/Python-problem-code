L=[4,2,7,5,1]
try:
    res=0
    for ele in L:
        res+=L[ele]
    print(res)
except:
    print('Hello')
finally:
    print('Bye')