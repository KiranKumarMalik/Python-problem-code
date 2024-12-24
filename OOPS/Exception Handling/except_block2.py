L=[4,2,5,7,1]
try:
    res=0
    for ele in L:
        res+=L[ele]
    print(res)
except IndexError as msg:
    print(f'Error Occurred: {msg}')
except NameError as msg:
    print(f'Error Occurred: {msg}')
except ValueError as msg:
    print(f'Error Occurred: {msg}')