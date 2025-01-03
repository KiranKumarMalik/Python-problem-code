import re
S="We are waiting for final results"
print(re.findall("a",S)) # ['a', 'a', 'a']
print(re.findall("y",S)) # []