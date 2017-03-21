#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

class WupeiqiException(Exception):

    def __init__(self, msg):
        self.message = msg
try:
    raise WupeiqiException('我的异常')
except WupeiqiException as e:
    print (e)
