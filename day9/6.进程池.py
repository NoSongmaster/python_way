#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
'''进程池--方式一：直接调用'''
# from concurrent.futures import ProcessPoolExecutor
#
# def task(arg):
#     print(arg)
# if __name__ == '__main__':
#     pool= ProcessPoolExecutor(5)
#     for i in range(10):
#         pool.submit(task,i)

#方式二: 分布进行
from concurrent.futures import ProcessPoolExecutor

def call(arg):
    data=arg.result()
    print(data)
def task(arg):
    print(arg)
    return arg+100
if __name__ == '__main__':
    pool= ProcessPoolExecutor(5)
    for i in range(10):
        obj=pool.submit(task,i)
        obj.add_done_callback(call)
