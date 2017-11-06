class Tool(object):

    #使用赋值语句定义类属性
    count = 0
    def __init__(self,name):
        self.name=name

        #让类属性的直加1
        Tool.count += 1

tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3= Tool("刀")
#输出对象的总数
print(Tool.count)
print(tool1.count)