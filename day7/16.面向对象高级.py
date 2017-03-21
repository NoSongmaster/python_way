#liuhao
#__call__()
# class Foo:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self, *args, **kwargs):    #将实例变成可以调用的。
#         print('------>')
# f=Foo('egon')
# f()
class Foo:
    def __init__(self,name):
        self.name=name

    def __getitem__(self, item):
        print(self.__dict__[item])

    def __setitem__(self, key, value):
        self.__dict__[key]=value
    def __delitem__(self, key):
        print('del obj[key]时,我执行')
        self.__dict__.pop(key)
    def __delattr__(self, item):
        print('del obj.key时,我执行')
        self.__dict__.pop(item)
f=Foo('egon')
print(f['name'])
f['x']=1
print(f.__dict__)
del f.x
#del f['x']







