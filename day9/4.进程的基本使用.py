#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
from multiprocessing import Process
import time

def task(arg):
    time.sleep(arg)
    print(arg)

if __name__ == '__main__':#windows中必须这样写，才能执行
    for i in range(10):
        p=Process(target=task,args=(i,))
        p.daemon=True   #主进程不等待子进程执行完毕，
        # p.daemon = False    #默认是False
        p.start()
        p.join(1)
    print('主进程中的主线程执行到最后......')
