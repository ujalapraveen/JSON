import json

a={"name": "David",
     "class":"I",
     "age": 6  
 }

mystring = json.dumps(a)
print(mystring)
print(type(mystring))

# file=open("saral.json","w")
# data=json.dump(a,file,indent=2)
# print(data)
# file.close()