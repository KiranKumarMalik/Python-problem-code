import re
S="We don't want class on Sunday"
print(re.subn("o","a",S))
print(re.subn(" ","a",S,3))