import re
s = '''abhay  56 abhayyadav yadavabhay 5.
<h1> sdhdfk dsfjhsd sdhf dskhf skfdh </h1>
dfsd sdhf PV SINDHU kfhs skdfh skf  dskf sdkf'''

#pattern = "<html>"
#pattern = "</html>"d
#  ., \w, \d, ? , \s, ^, \$, \A, \Z, \d\d, \d{2}, \S{2}, \S{2,6}, \S{3,}, S*, d+
pattern = "\<h1>(.*?)</h1>"
p = re.findall(pattern,s)


print(p)

"""data = re.search(r"var ytInitialPlayerResponse = ({.*?});",str(s.prettify())).group(1)
[videoDetails][videoId]': 'HZ9MUzCRlzI'}
{'[videoDetails][title]': 'Implementing Machine Learninng Pipelines USsing Sklearn And Python'}
{'[videoDetails][lengthSeconds]': '1606'}
[videoDetails][viewCount]': '8512'}
{'[microformat][playerMicroformatRenderer][publishDate]': '2022-09-01'}
{'[microformat][playerMicroformatRenderer][uploadDate]': '2022-09-01'}
Shoer discription of video"""

