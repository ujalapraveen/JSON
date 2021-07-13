# Write a Python program to convert Python objects into JSON strings. Print all the values.

import json
python_dict={"name":"ujala","age":18,"class":12}
python_list=["red","green","blue","pink"]
python_str="ujala parveen"
python_int=(1234)
python_float=(36.43)
python_T=(True)
pyhthon_F=(False)
python_N=(None)

json_dict=json.dumps(python_dict)
json_list=json.dumps(python_list)
json_str=json.dumps(python_str)
json_int=json.dumps(python_int)
json_float=json.dumps(python_float)
json_t=json.dumps(python_T)
json_F=json.dumps(pyhthon_F)
json_N=json.dumps(python_N)


print(json_dict)
print(json_list)
print(json_str)
print(json_int)
print(json_float)
print(json_t)
print(json_F)
print(json_N)