#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

class C(object):
    def __call__(self, *args, **kwargs):
        print('is call')

a=C()
a()
#通过实例加()调用__call__()


