#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

#创建两个函数
def init(self,name,age):
    self.name=name
    self.age=age
def sayhi(self):
    print('hello',self.name)
#使用type方法创建类
Test=type('Test',(object,),{'sayhi':sayhi,'__init__':init})
#生成实例
test_obj=Test('liuhao','22')
#调用实例方法
test_obj.sayhi()
