my_file=open("Q7.txt","r")
file_data=my_file.read()
print(file_data)
files=file_data.split()
s=iter(files)
u=dict(zip(s,s))
# print(u)
u["Designation"]="CEO Of Navgurukul"
# print(u)
u.pop("of")
print(u)
import json
open_file=open("Q7 data.json","w")
json.dump(u,open_file,indent=4)
open_file.close()


