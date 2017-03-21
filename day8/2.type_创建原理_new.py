#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

'''__new__：object继承到的方法：用途是生成实例对象'''
class Foo(object):
    def __init__(self,name):
        self.name=name
        print('Foo__init__')
    #__new__:生成实例的方法
    def __new__(cls, *args, **kwargs):  #覆盖了object中的new
        '''这里负责调用实例化,事实：就是将类的内存地址复制一份,开辟一块新的内存空间，打算给实例用
            这里就是生成实例对象的内存地址，并且返回
        '''
        print('Foo __new__')
        #object.__new__(cls)        #实例化后的内存地址
        obj=object.__new__(cls)
        print('obj',dir(obj))
        print(obj)
        return obj      #返回obj这个内存空间

f=Foo('alex')
print(dir(f))
print(f)
print(f.name)
