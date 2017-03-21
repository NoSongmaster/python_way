#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

import threading
import time
def sayhi(num):
    print('running on number:%s'%num)
    time.sleep(1)
    print('执行完毕:',num)
if __name__ == '__main__':
    thread_list=[]
    for i in range(10):
        t1=threading.Thread(target=sayhi,args=(i,))    #生成一个线程实例
        t1.start()
        thread_list.append(t1)
for r in thread_list:
    r.join()    #t1.wait()  #等待线程执行完毕，再去执行主线程
#t1.join()  主程序会等待他执行完毕再去执行

print('-------主线程-------')