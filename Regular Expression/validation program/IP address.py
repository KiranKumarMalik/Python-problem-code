import re
S="255.0.25.42"
if re.match('((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])[.]){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$',S):
    print("Valid IP Address")
else:
    print("Invalid IP Address")