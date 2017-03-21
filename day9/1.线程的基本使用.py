#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import threading
import time
'''
def task(arg):
    time.sleep(1)
    print(arg)
#target 写函数名，args 传入参数，必须是可迭代的
# t=threading.Thread(target=task,args=[13,])
# t.start()       #start 是说准备好了，等待cpu来执行
for i in range(30):
    t=threading.Thread(target=task,args=[i])
    t.setDaemon(True)   #主线程终止，不等待子线程----只能在start之前定义
    t.start()       #start 是说准备好了，等待cpu来执行
    # t.join()        #一直等待子线程执行完成后，执行主线程
    # t.join(1)       #等待最大时间，1s 如果子线程没有执行完就继续执行
print('end')
'''
#继承父类threading.Thread
class MyThread(threading.Thread):
    def __init__(self,func,*args,**kwargs): #重构父类的构造方法
        super(MyThread,self).__init__(*args,**kwargs)   #继承父类的构造方法
        self.func=func  #加入一个参数
    def run(self):  #重构run 方法
        print('子类')
        self.func()

def task():
    time.sleep(1)
    print(1111)
obj=MyThread(func=task)
#这里的start方法其实还是从父类继承过来的。他其实是去调用了self.run() 方法，由于子类重构了run方法
obj.start() #执行了子类中的run() 方法