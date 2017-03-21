#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import threading
import time
v=10
#1.只能有一个人使用锁
# lock=threading.Lock()   #创建一个锁，只能进去一个线程
# # lock=threading.RLock()  #支持可以上两把锁
# def task(arg):
#     time.sleep(2)
#     #申请使用锁,其它人等待
#     print('启动线程：',arg)
#     lock.acquire()
#     # lock.acquire()     #配合Rlock使用
#     time.sleep(1)
#     global v
#     v-=1
#     print(v)
#     #释放锁
#     lock.release()
#     # lock.release()    #配合Rlock使用
# for i in range(10):
#     t=threading.Thread(target=task,args=(i,))
#     t.start()
'''2.多人同时使用锁'''
#-----规定同时可以有三人使用锁-----
# lock=threading.BoundedSemaphore(3)
# def task(arg):
#     time.sleep(2)
#     #申请使用锁,其它人等待
#     print('启动线程：',arg)
#     lock.acquire()
#     time.sleep(1)
#     global v
#     v-=1
#     print(v)
#     #释放锁
#     lock.release()
#     # lock.release()    #配合Rlock使用
# for i in range(10):
#     t=threading.Thread(target=task,args=(i,))
#     t.start()
'''3.所有的线程解脱锁的限制'''
# #事件锁
# lock=threading.Event()
# def task(arg):
#     time.sleep(1)
#     #申请使用锁,其它人等待
#     print('启动线程：',arg)
#     #锁住所有的线程,全部暂停.等待释放-----
#     lock.wait()
#     print(v)
#
# for i in range(10):
#     t=threading.Thread(target=task,args=(i,))
#     t.start()
# while True:
#     value=input('>>')
#     if value=='1':
#         #local.set() 放开所有被锁住的线程
#         lock.set()  #其实就将wait中的_flag 标签修改成True。并执行_cond.notify_all()
#         #与set()相对的
#         # lock.clear() # self._flag = False 但不执行其它操作
'''4.肆意妄为'''
lock=threading.Condition()      #自定义锁中允许通过的数量，可以实时的传参
#配合地址池使用
def task(arg):
    time.sleep(2)
    #申请使用锁,其它人等待
    print('启动线程：',arg)
    lock.acquire()
    lock.wait()
    print('线程,',arg)
    lock.release()
    # lock.release()    #配合Rlock使用
for i in range(10):
    t=threading.Thread(target=task,args=(i,))
    t.start()
while True:
    value=input('>>>')  #输入要运行线程的数量
    lock.acquire()
    lock.notify(int(value))     #自定义通过锁的线程数量
    lock.release()



