class Cat():
    def __init__(self,new_name):
        self.name = new_name
    def __del__(self):
         print("%s我去了"%self.name)
    def __str__(self):
#-------
#使用str方法必须返回字符串
#-----------
        return "我是小猫[%s]"%self.name
tom = Cat("Tom")
print(tom)