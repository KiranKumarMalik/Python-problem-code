dictvar={'a':1, 'b':3, 'c':5}
new_dict={}
for k, v in dictvar.items():
    new_dict[v]=k
print(new_dict)