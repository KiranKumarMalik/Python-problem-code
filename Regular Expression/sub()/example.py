import re
S="We are waiting for final results"
print(re.sub(" ","@",S))
print(re.sub("3","5",S))
print(re.sub(" ","@",S,3))