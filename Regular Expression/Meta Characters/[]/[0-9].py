import re
S="abDe85Ko2#28rW"
print(re.findall("[0-9]",S)) # [0-9]: This expression matches the digits in the string.
print(re.findall("[3-9]",S)) # [3-9]: This expression matches the digits 3 to 9 in the string.