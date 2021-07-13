#Write a Python program to convert JSON data to Python object.

import json

json_object='{"maggie":"5","biscuits":"30","maggie":"8","choco":"100"}'
dic_obj=json.loads(json_object)
print(dic_obj)
print(type(dic_obj))