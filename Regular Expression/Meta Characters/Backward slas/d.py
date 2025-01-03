import re
S="a@$b1 2AB_# 42R"
print(re.findall("\d",S))  # \d: This expression matches the digit in the string.