class Women:

    def __init__(self,name):

        self.name = name
        self.__age = 18

    def __secret(self):
        #在对象的方法内部，是可以访问其私有属性的
        print("%s的年龄%d"%(self.name,self.__age))

xiaofang = Women("小芳")
#print(xiaofang.__age)
# 私有方法和属性不可以在外界访问
xiaofang.secret()

