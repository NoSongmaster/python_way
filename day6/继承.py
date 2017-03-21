#liuhao

#多继承演示
class Course(object):   #多继承时候，不应该都写构造方法
    course_name='Python 自动化'
    period='7m'
    outline='www.baidu.com'
    print('in course')      #演示继承顺序
class SchoolMember(object):
    member=0                            #统计学校注册成员
    print('in SchoolMember')          #演示继承顺序
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        SchoolMember.member+=1  #统计所有的学校成员
        print('初始化了一个新学校成员',self.name)
    def tell(self):
        info = '''
        -----info of {name} -----
        name:{name}
        age:{age}
        sex:{sex}
        '''.format(name=self.name,age=self.age ,sex=self.sex)
        print(info)
    def __del__(self):                  #析构方法   #实例销毁时自动执行
            print("%s被开除了"%self.name) #
            SchoolMember.member -= 1
class Teacher(SchoolMember):                #继承父类
    def __init__(self,name,age,sex,salary):         #这里相当于重构了父类的构造方法
        SchoolMember.__init__(self,name,age,sex)
        # self.name=name
        # self.age=age
        # self.sex=sex
        self.salary=salary
    def teaching(self,course):
        print('%s is teaching %s'%(self.name,course))
#class Student(SchoolMember):
class Student(SchoolMember,Course):                 #演示多继承,继承顺序先右后左，两个父类中都有变量时，会产生重新赋值。
    def __init__(self,name,age,sex,grade):
        SchoolMember.__init__(self,name,age,sex,)
        self.grade=grade
    def pay_tuition(self,amount):
        self.paid_tuition=amount
        print('student %s has paid tution amount %s '%(self.name,amount))

#t=Teacher('Alex',22,'F',3000)
s=Student('helei',24,'F','pys16')
# s2=Student('Yanshuai',23,'F','pys33')
# s3=Student('Nining',22,'M','pys16')
# print(SchoolMember.member)  #此时创建了4个实例
#
# del s3
# print(SchoolMember.member)  #此时删除了一个实例
# print(s.course_name)

# t=Teacher("alex",22,'F',30000)
# print(t.name)
# print(t.age)
# print(t.sex)
# print(t.salary)
# t.tell()
# t.teaching('python')