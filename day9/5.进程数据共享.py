#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

'''
#验证进程之间数据不共享
from multiprocessing import Process
from threading import Thread
def task(num,li):
    li.append(num)
    print(li)
if __name__ == '__main__':
    v=[]
    for i in range(10):
        p = Thread(target=task, args=(i, v,)) #演示线程的数据共享
        # p=Process(target=task,args=(i,v,))
        p.start()
'''
'''
方式一:
#进程之间通过特殊的数据类型进行数据共享----C语言中的Array 数组
from multiprocessing import Process,Array
def task(num,li):
    li[num]=1
    print('进程：',num,list(li))
if __name__ == '__main__':
    # v=Array('数据类型','长度')
    v=Array('i',100)   #C语言中数组,
    for i in range(100):
        p=Process(target=task,args=(i,v,))
        p.start()
'''
from multiprocessing import Process,Manager
def task(num,li):
    li.append(num)
    print('进程：',num,li)
if __name__ == '__main__':
    # dic=Manager().dict()
    v=Manager().list()

    for i in range(10):
        p=Process(target=task,args=(i,v,))
        p.start()
        #会有报错-原因:进程之间建立socket连接进行通讯，
        #主进程关闭，socket连接意外断开---
        # p.join()    #两种模拟解决方式---提倡用进程池
    input('>>>')



