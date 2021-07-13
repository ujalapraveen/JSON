#Write a Python program to convert JSON encoded data into Python objec
import json

j_str='{"ujala":"praveen","gouri":"sharma","srisri":"suman"}'
file_data=json.loads(j_str)
print(file_data)
print(type(file_data))