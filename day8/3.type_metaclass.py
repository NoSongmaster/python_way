#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

class MyType(type):
    def __init__(self,*args,**kwargs):
        print('MyType  __init__',self,*args,**kwargs)
    def __new__(cls, *args, **kwargs):
        print('MyType __new__',cls,*args,**kwargs)
        obj=type.__new__(cls,*args,**kwargs)
        return obj
    def __call__(self, *args, **kwargs):    #在f=Foo('Alex') 时调用   self =Foo    *args = 'Alex'
        #这里传入的self 是已经执行完成MyType中__init__ 和 __new__ 的。 执行完的过程  __new__ 返回了obj = type.__new__(cls)  这个时候  self 中__new__ 其实就是 type.__new__
        print('MyType __call__',self,*args,**kwargs)
        # print(self.__new__)
        obj=self.__new__(self)      #这里执行的是object中继承的.__new__(cls)
        self.__init__(obj,*args,**kwargs)       #Foo 中的__init__已经重写
        obj.age=22
        return obj
class Foo(object,metaclass=MyType):
    def __init__(self,name):
        self.name=name
        print('Foo __init__ ')
   # print(__init__)
#下面全部注释状态下
'''
会通过MyType生成 Foo这个类：对于MyType来说也是一个对象
先执行Mype__new__()
再执行Mype__init__()
MyType __new__ <class '__main__.MyType'> Foo (<class 'object'>,) {'__init__': <function Foo.__init__ at 0x0000020EDCCF98C8>, '__qualname__': 'Foo', '__module__': '__main__'}
MyType  __init__ <class '__main__.Foo'> Foo (<class 'object'>,) {'__init__': <function Foo.__init__ at 0x0000020EDCCF98C8>, '__qualname__': 'Foo', '__module__': '__main__'}
'''
#相当于为Foo加() 默认会执行 __call__() 这里的Foo = MyType 中 __new__返回的内存地址
f=Foo('Alex')
'''
生成实例f ：Foo加上()
执行MyType中的__call__()
'''
print(Foo.__module__)
# print(f.name)