#liuhao
import time
print(time.time())  #时间戳，从计算机开始的秒数。1970-1-1 开始
print(time.altzone/60/60,)   #返回时间与utc时间的时间差，以秒计算
print(time.asctime())
t=time.localtime()  #返回本地时间：struct time对象格式
print(t.tm_year,t.tm_mon)
print(time.gmtime(time.time() - 800000))  # 返回utc时间的struc时间对象格式

#自定义时间展示格式：当前时间
print(time.strftime("%Y-%m-%d"))
#前一天的时间展示
struct_time=time.localtime(time.time()+10*365*86400)
print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time))

#将字符串转成时间;
time_str='2017-02-18 15:27:23'
#1、转换成时间对象
struct_time=time.strptime(time_str,"%Y-%m-%d %H:%M:%S")
print(struct_time)
#2、把一个时间对象转换成时间戳
print(time.mktime(struct_time))
#有一个图可

import datetime
#打印当前时间
print(datetime.datetime.now())
#将时间戳直接转换成字符串
print(datetime.datetime.fromtimestamp(time.time()))
#直接加减天数，默认是days. 参数：hours minutes
print(datetime.datetime.now()+datetime.timedelta(days=3650))
print(datetime.datetime.now()-datetime.timedelta(hours=2,minutes=30))
#时间的替换
print(datetime.datetime.now().replace(year=2016,month=3))

