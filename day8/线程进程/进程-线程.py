#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import threading
import time

def sayhi(num):
    print('running on number:%s'%num)
    time.sleep(3)
    print('执行完毕:',num)

if __name__ == '__main__':
    t1=threading.Thread(target=sayhi,args=(1,)) #生成一个线程实例
    t2=threading.Thread(target=sayhi,args=(2,)) #生成第二个线程实例
    t1.start()
    t2.start()
    print(threading.active_count()) #获取正在运行的线程总数
    print(t1.getName()) #获取线程名
    print(t2.getName())