#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

from concurrent.futures import ThreadPoolExecutor
import time
# def task(arg):
#     time.sleep(0.5)
#     print(arg)
#
# pool = ThreadPoolExecutor(5)
#
# for i in range(100):
#     #去连接池中获取连接 --去执行
#     pool.submit(task,i)
#C:\Users\liuhao\AppData\Local\Programs\Python\Python35\Scripts
#pip3 install requests
'''
import requests
def task(url):
    response = requests.get(url)
    print('得到结果:',url,len(response.content))
pool = ThreadPoolExecutor(2)
url_list=[
    'http://www.baidu.com',
    'http://www.taobao.com',
    'http://www.jingdong.com'
]
for url in url_list:
    print('开始请求',url)
    #去连接池中获取连接 --去执行
    pool.submit(task,url)
'''
import requests
def txt(future):    #根据add_done_callbak 回调函数 执行下列操作
    download_response=future.result()   #获取download函数返回的结果
    print('处理中',download_response.url,download_response.status_code,len(download_response.text))

def download(url):
    response=requests.get(url)
    return response #response 包含里下载的所有内容

pool = ThreadPoolExecutor(2)
url_list = [
    'http://www.jingdong.com',
    'http://www.baidu.com',
    'http://www.taobao.com',
]
for url in url_list:
    #去连接池中获取连接
    print('开始请求',url)
    future = pool.submit(download,url)  #执行这个方法返回一个实例
    future.add_done_callback(txt)   #通过这个返回的实例，调用传入的方法







