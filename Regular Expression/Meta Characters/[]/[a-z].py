import re
S="abDe85Ko2#28rW"
print(re.findall("[a-z]",S))  # [a-z]: This expression matches the lowercase alphabets in the string.
print(re.findall("[A-Z]",S))  # [A-Z]: This expression matches the uppercase alphabets in the string.