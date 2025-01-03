import re
S="abDe85Ko2#28rW"
print(re.findall("[a-zA-Z][0-9]",S))
print(re.findall("[a-zA-Z][0-9][0-9]",S))