import re
S="abDe85Ko2#28rW"
print(re.findall("[abcdABCD]",S)) # [abcdABCD]: This expression matches the characters a,b,c,d,A,B,C,D in the string.