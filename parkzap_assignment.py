import urllib.request,urllib.parse,urllib.error
import time
import itertools
import re
start=time.time()
pair_of_id_integer=dict()
fhand=urllib.request.urlopen('http://demo4657392.mockable.io/list-tag-ids')
for line in fhand:
    to_search_for_pair=line.decode().strip()
    student_id=re.findall('"([0-9]+)":',to_search_for_pair)
    string=re.findall(':"([a-z A-z 0-9]+)"}',to_search_for_pair)
    for (i,j) in zip(student_id,string):
        pair_of_id_integer[j]=i
find=input('Enter the string:')
try:
    print(pair_of_id_integer[find])
except:
    print("Input not found,Check your input")
end=time.time()
print("Runtime-",(end-start)*1000,"msec")


