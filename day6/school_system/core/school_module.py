#liuhao
import shelve
import os
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
school_database=base_dir+r'\db\school_database'
teacher_database=base_dir+r'\db\teacher_database'
student_database=base_dir+'\db\student_database'
grade_database=base_dir+'\db\grade_database'
course_database=base_dir+'\db\course_database'
class School(object):
    def __init__(self,school_name,addr):
        self.school_dict={}
        self.name=school_name
        self.addr=addr
        self.teacher_dict = {}
        self.course_dict = {}
        self.grade_dict = {}
        self.student_dict = {}
class Teacher(object):
    def __init__(self,teacher_name,teacher_age,teacher_salary):
        self.name=teacher_name
        self.teacher_age=teacher_age
        self.teacher_salary=teacher_salary
        self.teacher_grade={}
class Grade(object):
    def __init__(self,grade_name,grade_start_date):
        self.name=grade_name
        self.grade_start_date=grade_start_date
class Course(object):
    def __init__(self,course_name,course_mouth,course_money):
        self.name = course_name
        self.course_mouth = course_mouth
        self.course_money = course_money
class Student(object):
    def __init__(self,student_name,student_age):
        self.student_name=student_name
        self.student_age=student_age
    def add_grade(self,grade_obj):
        self.grade_dict={}
        self.grade_dict[grade_obj.name]=grade_obj



#保存数据
# c1=course('linux','12','12000','人生苦短，我用linux')# c1.create()
# c1.save()
#调用
def save(file_database,obj):
    data=shelve.open(file_database)
    print(obj.name)
    data[obj.name]=obj
# c1=course('python','12','12000','人生苦短，我用linux')
# save(course_database,c1)
def load(file_database,obj_name):   #加载数据
    data=shelve.open(file_database)
    if obj_name in data:
      return data[obj_name]
    return False

# a=load(course_database,'python')
# print(a.teacher)
# a.teacher='alex'
# save(course_database,a)
if __name__ == '__main__':

    school1=School('aaa','北京市')
    school2=School('达内教育','上海')
    save(school_database,school1)
    save(school_database,school2)
    #推荐加载的写法
      # data=load(school_database,'老男孩教育')
      # print(data.course_dict)
      #c1=Course('py','12','1000')
      # data.course_dict[c1.name]=c1
      # print(data.course_dict)
      # save(school_database,data)
              #    #print(load(school_database,'老男孩教育').teacher_dict)
