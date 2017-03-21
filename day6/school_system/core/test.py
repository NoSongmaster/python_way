#liuhao


import shelve
import os,sys,time
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
from core.school_module import School
from core.school_module import Teacher
from core.school_module import Grade
from core.school_module import Course
from core.school_module import Student
school_database=base_dir+r'\db\school_database'
teacher_database=base_dir+r'\db\teacher_database'
student_database=base_dir+'\db\student_database'
grade_database=base_dir+'\db\grade_database'
course_database=base_dir+'\db\course_database'
def save(file_database,obj):    #保存数据
    data=shelve.open(file_database)
    data[obj.name]=obj
def load(file_database,obj_name):   #加载数据,返回一个实例
    data=shelve.open(file_database)

    if obj_name in data:
      return data[obj_name]
    data.close()
    return False

#
t1=Teacher('alex','22','10000')
s1=load(school_database,'aaa')
s1.teacher_dict[t1.name]=t1
print(s1.teacher_dict)
save(teacher_database, t1)
save(school_database, s1)
#
# data=shelve.open(school_database,)
# for i in data:
#     print(data[i],i)
# print(data['老男孩教育'])


