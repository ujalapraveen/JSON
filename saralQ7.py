
import json

dict={}
with  open("Q7.txt","r")  as file_data:
    for i in file_data:
        key,value=i.strip().split(None,1)
        print(key)
        print(value)

        dict[key]=value.strip()
print(dict)
file=open("saral7.json","w")
json.dump(dict,file,indent=4)
file.close()












