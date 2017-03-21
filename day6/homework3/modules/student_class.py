#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import shelve
from modules.get_message_class import Get_message
from conf import setting
class Student(Get_message):  # 学生
    def __init__(self,name,age):
        '''
        学生的基本信息
        :param name:
        :param age:
        '''
        self.name = name
        self.age = age
    #
    # def set_fee(self,num):  # 交费
    #     self.fee += num

    # @staticmethod
    # def set_show():  # 返回当所有学生列表
    #     f = shelve.open(setting.STUDENT_DATABASE['path'])
    #     list=[]
    #     for i in f:
    #         list.append(i)
    #     return list

    #
    # @staticmethod
    # def get_name(name):  # 根据学生姓名关键字返回学生实例
    #     f = shelve.open(setting.STUDENT_DATABASE['path'])
    #     name_obj = f.get(name)
    #     return name_obj

if __name__ == '__main__':

    a = Student.get_name('123')
    print(a.name)