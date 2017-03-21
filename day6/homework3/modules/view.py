#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 新时类 vs 经典类
# SchoolMember.__init__(self,name,age,sex) # 经典类写法
# super(Teacher,self).__init__(name,age,sex) # 新式类写法
import os,sys
path= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
import shelve
from conf import setting
from modules.course_calss import Course
from modules.classes_class import Classes
from modules.teacher_class import Teacher
from modules.student_class import Student

def show_campus():  # 显示校区信息
    school_db = shelve.open(setting.DATABASE['path'])
    for key in school_db:
        print(key)
    school_db.close()

def admin():
    '''管理员视图函数'''
    school_db = shelve.open(setting.DATABASE['path'])
    msg='''
    1.创建课程
    2.创建班级
    3.创建讲师
    4.查看课程
    5.查看班级
    6.查看讲师
    '''
    print(msg)
    choice = input('输入选择：')
    show_campus()
    choice_campus = input('选择校区：')
    if choice_campus in school_db:
        campus_obj = school_db[choice_campus]
        if choice == '1':
            # 创建课程
            course_name = input('输入课程名称：')
            cycle = input('输入课程周期：')
            price = input('输入课程价格：')
            course_obj = Course(course_name,cycle,price)
            campus_obj.creat_course(course_name,course_obj)
            school_db[choice_campus] = campus_obj
            # print(campus_obj.course_dict)
            # print(school_db[choice_campus].course_dict)
        elif choice == '2':
            # 创建班级
            classes_name = input('输入班级名称：')
            start_time = input('输入开课时间：')
            for key in campus_obj.course_dict:
                course_obj=campus_obj.course_dict[key]
                course_msg = '''课程名:[%s]\t周期:[%s]\t学费:[%s]'''\
                             %(course_obj.course_name,course_obj.cycle,course_obj.price)
                print(course_msg)
            classes_obj = Classes(classes_name,start_time)
            course = input('输入要关联的课程名：')
            course_obj = campus_obj.course_dict[course]  # 根据给定的课程名，找到课程实例
            # print(course_obj)
            classes_obj.creat_course(course,course_obj)  # 把课程实例加到班级中
            campus_obj.creat_classes(classes_name, classes_obj)
            # print(campus_obj.classes_dict[classes_name].course_dict)  # 打印班级中的课程表
            school_db[choice_campus] = campus_obj
        elif choice == '3':
            # 创建讲师
            teacher_name = input('输入讲师姓名：')
            teacher_obj = Teacher(teacher_name)
            for key in campus_obj.course_dict:
                course_obj = campus_obj.course_dict[key]
                course_msg = '''课程名:[%s]\t周期:[%s]\t学费:[%s]'''\
                             %(course_obj.course_name,course_obj.cycle,course_obj.price)
                print(course_msg)
            course_name = input('输入讲师所教课程：')
            teacher_obj.creat_course(course_name)
            for key in campus_obj.classes_dict:
                classes_obj = campus_obj.classes_dict[key]
                for i in  classes_obj.course_dict:
                    course_info = i
                classes_msg = '''班级名：%s\t开课时间：%s\t关联的课程名：%s'''\
                              %(classes_obj.classes_name,classes_obj.start_time,course_info)
                print(classes_msg)
            classes_name = input('输入讲师所教班级：')
            classes_obj = campus_obj.classes_dict[classes_name]
            teacher_obj.creat_classes(classes_name,classes_obj)
            campus_obj.creat_teacher(teacher_name,teacher_obj)  # 调用校区(campus) 添加讲师信息
            school_db[choice_campus] = campus_obj
        elif choice == '4':
            for key in campus_obj.course_dict:
                course_obj = campus_obj.course_dict[key]
                course_msg = '''课程名:[%s]\t周期:[%s]\t学费:[%s]'''\
                             %(course_obj.course_name,course_obj.cycle,course_obj.price)
                print(course_msg)
        elif choice == '5':
            for key in campus_obj.classes_dict:
                classes_obj = campus_obj.classes_dict[key]
                for i in  classes_obj.course_dict:
                    course_info = i
                classes_msg = '''班级名：%s\t开课时间：%s\t关联的课程名：%s'''\
                              %(classes_obj.classes_name,classes_obj.start_time,course_info)
                print(classes_msg)
        elif choice == '6':
            for key in campus_obj.teacher_dict:
                teacher_obj = campus_obj.teacher_dict[key]
                teacher_msg = '''讲师名:[%s] 所教课程：%s 所教班级：%s(处理有问题)'''\
                             %(teacher_obj.teacher_name,teacher_obj.course,teacher_obj.classes_dict.keys())
                print(teacher_msg)
        else:
            print('输入选择错误')
    else:
        print('输入学校信息错误')
    school_db.close()


def teacher():
    '''讲师视图函数'''
    school_db = shelve.open(setting.DATABASE['path'])
    msg = '''
        1.选择管理班级
        '''
    print(msg)
    choice = input('输入选择：')
    show_campus()
    choice_campus = input('选择校区：')
    if choice_campus in school_db:
        campus_obj = school_db[choice_campus]
        if choice == '1':
            for key in campus_obj.teacher_dict:
                teacher_obj = campus_obj.teacher_dict[key]
                # print(teacher_obj.__dict__)
                teacher_msg = '''讲师名:[%s] 所教课程：%s 所教班级：%s(处理有问题)'''\
                             %(teacher_obj.teacher_name,teacher_obj.course,teacher_obj.classes_dict.keys())
                print(teacher_msg)
            teacher_name = input('输入你要操作的讲师')
            teacher_obj = campus_obj.teacher_dict[teacher_name]
            for key in teacher_obj.classes_dict:
                classes_obj = teacher_obj.classes_dict[key]
                for i in  classes_obj.course_dict:
                    course_info = i
                classes_msg = '''班级名：%s\t开课时间：%s\t关联的课程名：%s'''\
                              %(classes_obj.classes_name,classes_obj.start_time,course_info)
                print(classes_msg)
            # print(teacher_obj.classes_dict)
            classes_name = input('输入你要查看学生的班级：')  # 有问题。需要修改。------------------------------------------》
            # print(teacher_obj.classes_dict[classes_name])
            # print(teacher_obj.classes_dict[classes_name].student_dict)
            classes_obj = teacher_obj.classes_dict[classes_name]
            for i in classes_obj.student_dict:
                student_msg = '''学生姓名：%s  学生年龄：%s'''%(i,classes_obj.student_dict[i].age)
                print(student_msg)
    school_db.close()

def student():
    '''学生注册'''
    school_db = shelve.open(setting.DATABASE['path'])
    msg='''
    1.学生注册
    '''
    print(msg)
    choice = input('输入选择：')
    if choice == '1':
        show_campus()
        choice_campus = input('选择校区：')
        if choice_campus in school_db:
            campus_obj = school_db[choice_campus]
            for key in campus_obj.teacher_dict:
                teacher_obj = campus_obj.teacher_dict[key]
                # print(teacher_obj.__dict__)
                teacher_msg = '''讲师名:[%s] 所教课程：%s 所教班级：%s(处理有问题)''' \
                              % (teacher_obj.teacher_name, teacher_obj.course, teacher_obj.classes_dict.keys())
                print(teacher_msg)
            teacher_name = input('输入你要选择的老师：')
            teacher_obj = campus_obj.teacher_dict[teacher_name]
            for key in teacher_obj.classes_dict:
                classes_obj = teacher_obj.classes_dict[key]
                for i in classes_obj.course_dict:
                    course_info = i
                classes_msg = '''班级名：%s\t开课时间：%s\t关联的课程名：%s''' \
                              % (classes_obj.classes_name, classes_obj.start_time, course_info)
                print(classes_msg)
            classes_name = input('输入你要加入的班级')
            classes_obj = teacher_obj.classes_dict[classes_name]
            student_name = input('输入学生姓名：')
            student_age = input('输入学生年龄：')
            student_obj = Student(student_name,student_age)
            classes_obj.creat_student(student_name,student_obj)
            school_db[choice_campus] = campus_obj
            print('加入成功')
    school_db.close()



def run():
    while True:
        msg = '''
        1.管理员视图
        2.讲师视图
        3.学生视图
        4.退出
        '''
        print(msg)
        choice = input('输入选择：')
        if choice == '1':
            admin()
        elif choice == '2':
            teacher()
        elif choice == '3':
            student()
        elif choice == '4':
            exit('退出成功')
        else:
            pass
