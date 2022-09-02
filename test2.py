l5 =[]
key=""
count =0

data = {'k1':'ram','k2':{'k3':767,'k4':{'k5':[45,{'k6':67}]}},'k7':(56,'avg',{'k8':['up',100]})}


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
        l5.append(d)
        c = 0



get_all_key_value_pair(data,key,count)
for i in l5:
    print(i)
