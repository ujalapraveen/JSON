import json
d={'4':5,'5':7,'3':9,'1':11,'2':13}
a=json.dumps(d,sort_keys= True,indent=4)
print(a)
print(type(a))



# import json
# d=["4.6","7.8","12.9","15.8"]
# a=json.dumps(d,)
# print(a)
# print(type(a))