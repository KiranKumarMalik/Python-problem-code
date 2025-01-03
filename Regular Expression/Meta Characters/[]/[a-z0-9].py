import re
S="abDe85Ko2#28rW"
print(re.findall("[a-z0-9]",S)) # [a-z0-9]: This expression matches the lowercase alphabets and digits in the string.