#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import os
# import sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)


class Teacher(object):  # 老师
    def __init__(self,teacher_name):
        self.teacher_name = teacher_name
        self.classes_dict = {}  # 老师对应多个班级  但是由于实力会重新生成，所以只能在admin管理下只能存放一个。


    def creat_course(self,course):  # 老师对应一个课程（关联课程）
        self.course = course

    def creat_classes(self,classes_name,classes_obj): # 关联班级
        self.classes_dict[classes_name] = classes_obj




    # def chioce_student(self,student):  # 关联学生
    #     f = shelve.open(setting.STUDENT_DATABASE['path'])
    #     student_obj = f.get(student)
    #     if student_obj:
    #         self.student_dict[student]=student_obj
    #     else:
    #         print('学生不存在')
    #
    # @staticmethod
    # def set_show():  # 返回当所有老师列表
    #     f = shelve.open(setting.STUDENT_DATABASE['path'])
    #     list=[]
    #     for i in f:
    #         list.append(i)
    #     return list
    # @staticmethod
    # def set_name(name):  # 根据老师姓名返回学生信息
    #     # print(setting.TEACHER_DATABASE['path'])
    #     f = shelve.open(setting.TEACHER_DATABASE['path'])
    #     date = f.get(name)
    #     return date



