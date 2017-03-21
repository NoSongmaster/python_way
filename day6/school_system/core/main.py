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
    print(obj)
    print(obj.name)

    data[obj.name]=obj
    data.close()
def load(file_database,obj_name):   #加载数据,返回一个实例
    data=shelve.open(file_database)
    if obj_name in data:
        data_new=data[obj_name]
        data.close()
        return data_new
    return False
def all_load(file_database):
    data = shelve.open(file_database)
    return data

def add_teacher(school_name):
    teacher_name=input('create teacher name :')
    teacher_age=input('teacher age : ')
    teacher_salary=input('teacher salary: ')
    t1=Teacher(teacher_name,teacher_age,teacher_salary)
    s1=load(school_database,school_name)
    s1.teacher_dict[t1.name]=t1
    save(teacher_database, t1)
    save(school_database,s1)

    save(teacher_database, t1)

def add_course(school_name):
    course_name=input('course name: ')
    course_mouth=input('course mouth: ')
    course_money=input('course moeny')
    c1=Course(course_name,course_mouth,course_money)
    s1=load(school_database,school_name)
    c1.school_name = {school_name:s1}

    s1.course_dict[c1.name]=c1

    save(course_database, c1)
    save(school_database,s1)
def add_grades(school_name):
    grade_name=input('grade name : ')
    grade_start_data=log_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    g1=Grade(grade_name,grade_start_data)
    s1=load(school_database,school_name)
    g1.school_name = {school_name:s1}
    s1.grade_dict[g1.name]=g1
    save(grade_database, g1)
    save(school_database,s1)
def show_school():
    data=all_load(school_database)
    for i in data:
        print('学校名称:%s ,地址:%s'%(data[i].name,data[i].addr))
def show_course():
    data=all_load(course_database)
    for i in data:
        print('课程名：%s ,课程周期：%s ,课程学费：%s'%(data[i].name,data[i].course_mouth,data[i].course_money))
def show_grade():
    data=all_load(grade_database)
    for i in data:
        print('班级名称：%s ,班级开始时间：%s'%(data[i].name,data[i].grade_start_date))
def show_teacher():
    data=all_load(teacher_database)
    for i in data:
        print('老师：%s , 年龄：%s , 工资：%s'%(data[i].name,data[i].teacher_age,data[i].teacher_salary) )
def admin_view():
    while True:
        data = shelve.open(school_database)
        for i in data:
            #print(data[i])
            print('''
            学校名称:%s
            地址:%s
            现有老师:%s
 ''' % (data[i].name, data[i].addr,data[i].teacher_dict))
            #,data[i].course_dict.keys(),data[i].grade_dict.keys(),data[i].student_dict.keys()

        school_name=input('输入学校的名称:')
        if school_name=='q':break
        elif school_name in data:
            while True:
                print('''
                1.添加课程
                2.添加班级
                3.添加讲师
                4.查看课程
                5.查看班级
                6.查看讲师
                q.退出
                ''')
                choice=input('enter your choice: ')
                if choice =='1':
                    add_course(school_name)
                elif choice=='2':
                    add_grades(school_name)
                elif choice=='3':
                    t1 = Teacher('alex', '22', '10000')
                    s1 = load(school_database, 'aaa')
                    s1.teacher_dict[t1.name] = t1
                    print(s1.teacher_dict)
                    save(teacher_database, t1)
                    save(school_database, s1)
                elif choice=='4':
                    show_course()
                elif choice=='5':
                    show_grade()
                elif choice=='6':
                    show_teacher()
                else: break
            data.close()
        else:print('你输入的学校名称不存在')

def teacher_view():
    print('''
    1.关联班级
    2.关联课程
    3.查看基本信息
    ''')
def student_view():
    print('''
    1.注册
    2.交学费
    3.选择班级
    ''')
def run():
    while True:
        choice = input('''
                    1.管理视图
                    2.讲师视图
                    3.学生视图
                    q.退出选课系统
            ''')
        if choice == '1':
            admin_view()
        elif choice=='2':
            teacher_name=input('enter teacher name:')
            if load(teacher_database,teacher_name) is not False:
                teacher_view()
            else:print("老师 %s 不存在"%teacher_name)
        elif choice=='3':
            student_view()
        elif choice=='q':

            print("正在退出选课系统！")
            break

#add_teacher('老男孩教育')
run()

