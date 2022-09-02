import re
import requests
from bs4 import BeautifulSoup as bs
import json
url="https://www.youtube.com/user/krishnaik06/videos"
p=requests.get(url)
#print(requests.get(url).text)
s = bs(p.text,"html.parser")
#print(s)
data = re.search("var ytInitialData = ({.*});",str(s.prettify())).group(1)
#print(data)
json_data = json.loads(data)
#print((json_data).keys())
#print(json_data['contents'])
#print((json_data['header']['c4TabbedHeaderRenderer']))
#ch_name = json_data['header']['c4TabbedHeaderRenderer']['title']
#print(ch_name)
#print(type(json_data))
data = {'abh':'ram','k2':{'k3':767,'k4':{'ram':[45,{'abhay':67}]}}}
input_value =list(data.keys())
#print(input_value)

l5 =[]
k=""
count=0
def get_all_key_value_pair(data, k, count):
    p, c = (k, count)
    if type(data) == dict:
        all_keys = list(data.keys())
        for i in all_keys:
            p = k + "[{}]".format(i)
            c = count + 1
            get_all_key_value_pair(data[i], p, c)

    elif (type(data) == list) or (type(data) == tuple):
        for j in range(len(data)):
            p = k + "[{}]".format(j)
            c = count + 1
            get_all_key_value_pair(data[j], p, c)
    else:
        d = {p: data}
        p = ""
        #if(c<15):
        l5.append(d)
        c = 0

get_all_key_value_pair(json_data,k,count)
for i in l5:
    print(i)