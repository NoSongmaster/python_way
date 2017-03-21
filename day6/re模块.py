#liuhao

#re.search()    全局匹配
#re.match()     从头开始查找
'''
>>> re.split("\W+","192.168.0.1")
['192', '168', '0', '1']
>>> re.findall("\W+","192.168.0.1")
['.', '.', '.']
'''
import re
a=re.sub("\d{4}",'1995','i was born in 1992-01-01')    #替换
print(a)

