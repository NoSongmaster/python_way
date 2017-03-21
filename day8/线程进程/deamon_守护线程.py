#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao


import threading
import time
def sayhi(num):

    print('running on number:%s'%num)
    time.sleep(0.001)
    print('执行完毕:',num)
if __name__ == '__main__':
    thread_list=[]
    for i in range(10):
        t1=threading.Thread(target=sayhi,args=(i,))    #生成一个线程实例
        t1.setDaemon(True)
        t1.start()
        #thread_list.append(t1)

print('--------主线程------------')
