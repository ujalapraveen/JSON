#2. Write a Python program to convert Python object to JSON data.
import json

a={"nam":"ujala","class":12,"age":12}
data=json.dumps(a)
print(data)
print(type(data))