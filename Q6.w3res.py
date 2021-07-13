

#Write a Python program to create a new JSON file from an existing JSON fil#



import json
a={"name":"dangal","language":"hindi","acting":"drama","hero":"VarunDhawan","character":"willion"}
with open('movie.json','w')as file:
    json.dump(a,file,indent=6)