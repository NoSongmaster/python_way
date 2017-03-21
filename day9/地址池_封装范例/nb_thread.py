#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import requests
from concurrent.futures import ThreadPoolExecutor
def download(url):
    response=requests.get(url)
    return response

pool = ThreadPoolExecutor(2)
def run(url_list):
    for item in url_list:
        #去连接池中获取连接
        url=item['url']
        call=item['call']
        print('开始请求',url)
        future = pool.submit(download,url)  #执行这个方法返回一个实例
        future.add_done_callback(call)   #通过这个返回的实例，调用传入的方法




