#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Classes(object):  # 班级
    def __init__(self,classes_name,start_time):
        self.classes_name = classes_name  # 班级名
        self.start_time = start_time  # 开课时间
        self.teacher_dict = {}  # 存放老师实例
        self.student_dict = {}  # 存放学生实例
        self.course_dict = {}  # 存放课程实例


    def creat_course(self,course_name,course_obj):  # 关联课程
        self.course_dict[course_name] = course_obj
    #
    def creat_teacher(self,teacher_name,teacher_obj):  # 关联讲师
        self.teacher_dict[teacher_name] = teacher_obj

    def creat_student(self,student_name,student_obj):  # 关联学生
        self.student_dict[student_name] = student_obj


