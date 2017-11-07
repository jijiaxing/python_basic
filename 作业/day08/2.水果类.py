#3 定义一个水果类，然后通过水果类，创建苹果对象、橘子对
# 、西瓜对象并分别添加上颜色属性
class Fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def __str__(self):
        return ("我是【%s】，我的颜色【%s]"%(self.name,self.color))
anple = Fruit("苹果","绿色")
juzi  = Fruit("橘子","红色")
xigua = Fruit("西瓜","粉色")
print(anple)
print(juzi)
print(xigua)
