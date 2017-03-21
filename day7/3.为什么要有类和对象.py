#liuhao

class Chinese:
    dang='共产党'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def talk(self):
        print("====>>")

p1=Chinese('engo',18,'female')
p1.talk()
