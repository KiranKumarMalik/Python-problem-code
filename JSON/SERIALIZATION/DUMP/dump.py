# dump(): This method is used to convert the python data into JSON format and save it into .json file.
# Syntax: json.dump(data, file_object, indent)
# data: The python data which has to be converted into JSON format.
# file_object: The file object where the converted JSON data has to be saved.
# indent: It is an optional parameter which is used to define the number of indents to be used in the JSON file.

import json
D={"name":"Kiran", "age":25, "city":"Bangalore", "state":"Karnataka"}
with open("data.json", "w") as fobj:
    json.dump(D, fobj, indent=4)