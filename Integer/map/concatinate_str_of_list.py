def Concat(ch1,ch2):
    return ch1+ch2
for ele in map(Concat,['a','b','c'],['x','y','z']):
    print(ele)