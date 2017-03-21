#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
#协程
# from greenlet import greenlet
# def f1():
#     print('A+')
#     g2.switch()
#     print('B+')
#     g2.switch()
# def f2():
#     print('A-')
#     g1.switch()
#     print('B-')
#     g1.switch()
# g1= greenlet(f1)
# g2= greenlet(f2)
# g1.switch()

# 根据协程二次开发:协程+IO
from gevent import monkey;monkey.patch_all()
import gevent
import requests
def f(url):
    response=requests.get(url)
    print(response.url,response.status_code)

gevent.joinall([
    gevent.spawn(f,'http://www.baidu.com/'),
    gevent.spawn(f,'http://www.taobao.com/'),
    gevent.spawn(f,'http://www.jingdong.com/'),
])

