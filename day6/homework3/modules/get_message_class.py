#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 公共类
class Get_message(object):
    def show(self):
        '''
        显示信息
        :return:
        '''
        print('------- info -------')
        for k,v in self.__dict__.items():
            print(k,'\t',v)
        print('------- end  -------')
