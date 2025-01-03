import re
S="We don't want class on Sunday"
print(re.finditer("a",S))
print(list(re.finditer("a",S)))

for ele in re.finditer("a",S):
    print(ele)

print(list(re.finditer("Z",S)))