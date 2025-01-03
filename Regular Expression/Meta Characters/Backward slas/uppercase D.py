import re
S="a@$b1 2AB_# 42R"
print(re.findall("\D",S))  # \D: This expression matches any non-digit character.