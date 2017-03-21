#liuhao
import shelve
d=shelve.open('shelve_test')

#生成序列化的文件，3个，不需要管理
info = {'age':22,'job':'it'}    #持久化字典
name = ['alex','oldboy','testsss'] #持久化列表
class Test(object):
    def __init__(self,n):
        self.n = n
t1=Test('sss')
d['obj']=t1
d['dict']=name
d['list']=info
d.close()
#读取key
d=shelve.open('shelve_test')
for i in d:
    print(i)
print(d['dict'])


