l5 =[]
#k=""
data = {'abh':'ram','k2':{'k3':767,'k4':{'ram':[45,{'abhay':67}]}}}
def get_all_key_value_pair(data,k):
    if type(data) == dict:
        all_keys = list(data.keys())
        print(all_keys)
        for i in all_keys:
            k = k+"[{}]".format(i)
            print(k)
            get_all_key_value_pair(data[i],k)

    elif type(data) == list:
        for j in range(len(data)):
            k=k+"[{}]".format(j)
            print(k)
            get_all_key_value_pair(data[j],k)
    else:
        d={k:data}
        k=""
        l5.append(d)
        print(l5)
        print(k)

get_all_key_value_pair(data,k="")
print(l5)