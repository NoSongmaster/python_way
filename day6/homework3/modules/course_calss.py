#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Course(object):  # 课程
    def __init__(self,course_name,cycle,price):
        self.course_name = course_name  #课程名称
        self.cycle = cycle  # 周期
        self.price = price  # 价格

        