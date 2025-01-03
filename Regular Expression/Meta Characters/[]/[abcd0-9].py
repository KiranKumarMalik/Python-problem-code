import re
S="abDe85Ko2#28rW"
print(re.findall("[abcd0-9]",S)) # [abcd0-9]: This expression matches the characters a,b,c,d,0-9 in the string.