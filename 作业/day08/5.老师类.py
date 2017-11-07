#6. 定义一个老师类,老师有所授学科,有职位,能教学生,能driver
class Teacher:
    def __init__(self,subject,position):
        self.subject = subject
        self.position = position
    def study(self):
        print("可以教学生")
    def dirver(self):
        print("可以开车")
    def __str__(self):
        return ("我的职务%s我的学科%s"%(self.subject,self.position))
teacher = Teacher("数学","教授")
print(teacher)
teacher.dirver()
teacher.study()