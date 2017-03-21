#liuhao
class Teacher:
    def __init__(self,name,birth=None):
        self.name= name
        self.birth=Date(1999,1,24)
        self.course=Course('python',1000,7)
class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
class Course:
    def __init__(self,name,price,period):
        self.name=name
        self.price=price
        self.period=period
t=Teacher('egon')



