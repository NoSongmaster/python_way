#liuhao
import re
list=[['mac Pro', 13888], ['mac Pro', 13888], ['mac Pro', 13888], ['ipad mini4', 2888], ['ipad mini4', 2888], ['kindle', 799], ['coffe', 38]]
#列表生成式
list1=[n[0] for n in list]
set1=set(list1)
for i in set1:
    print(i,list1.count(i))



