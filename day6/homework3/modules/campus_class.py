#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Campus(object,):  # 校区
    def __init__(self,school_name,address):
        self.school_name = school_name  # 学校名称
        self.address = address  # 地址
        self.classes_dict = {}
        self.course_dict = {}
        self.teacher_dict = {}

    def creat_course(self,course_name,course_obj):  # 创建课程
        self.course_dict[course_name] = course_obj

    def creat_classes(self,classes_name,classes_obj):  # 创建班级
        self.classes_dict[classes_name] = classes_obj

    def creat_teacher(self,teacher_name,teacher_obj):  # 创建讲师
        self.teacher_dict[teacher_name] = teacher_obj
