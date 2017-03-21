#liuhao
import getpass
# username="NoSong"
# Password="123456"
# user = input("请输入用户名：")
# pwd = input("请输入密码：")
# print("用户名：%s，密码：%s"%(user,pwd))

list=["alex","oldboy","nosong","noway","nobody","jack"]
numnber=[1,2,3,4,5,6,7,8,9]
#索引
print("索引",list.index("nobody"))
#切片
print("切片",numnber[1:5])
#步长
print("步长",numnber[1:8:2])
#追加
numnber.append(100)
print("追加",numnber)
#插入 （在下标3的位置插入444）
numnber.insert(3,4444)
print("插入",numnber)
#长度：
print("长度",len(numnber))
#循环
for i in list:              #输出value
    print(i)
for k,v in enumerate(list): #带下标输出
    print(k,v)
#包含：
if "alex" in list:
    print("包含:yes")