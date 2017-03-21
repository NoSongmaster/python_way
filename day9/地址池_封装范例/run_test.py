#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
#封装线程中地址池的使用方法：
#将url  获取到的结果，通过回调函数来进行处理
#通过回调函数
import nb_thread
def f1(future):
    response=future.result()
    print(response.status_code)
def f2(future):
    response=future.result()
    print(response.url)
def f3(future):
    response=future.result()
    print(response.text)


url_list = [
    {'url':'http://www.baidu.com','call':f1},
    {'url':'http://www.baidu.com','call':f2},
    {'url':'http://www.baidu.com','call':f3},
]

nb_thread.run(url_list)
