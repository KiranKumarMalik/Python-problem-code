# loads(): This method is used to convert a JSON data into python data.
# Syntax: json.loads()
# In order to use loads mesthod, we have to read the content from JSON file.

import json
with open('details.json','r') as fobj:
    jcontent = fobj.read()
    pydata = json.loads(jcontent)
    print(pydata)
    print(type(pydata))