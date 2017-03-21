#liuhao
class Foo:
    def __init__(self,name):
        self.name=name
    def func(self):
        print('func')

f = Foo('egon')
print(Foo.__dict__)
print(f.__dict__)
#hasattr判断类中是否有这个func的名字
print(hasattr(Foo,'func'))

#判断实例中是否有x这个属性
print(hasattr(f,'x'))
f.x=1
#根据字符串，调用实例中的属性
print(getattr(f,'x'))
#常用组合
if hasattr(f,'func'):
    getattr(f,'func')()
#调用，如果没有，返回None
print(getattr(f,'y',None))
#设置一个属性
#f.y=1
setattr(f,'y',1)
