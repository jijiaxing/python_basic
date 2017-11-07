# 定义一个汽车类，并在类中定义一个move方法，然后分别创建BMW_X9、AUDI_A9对象，并添加颜色、马力、型号等属性，
# 然后分别打印出属性值、调用move方法
class Car:
    def __init__(self,color,model,horse):
        self.color = color
        self.model = model
        self.horse = horse
    def move(self):
        print("咻咻咻")
    def __str__(self):
        return ("颜色【%s】型号【%s】玛丽【%s】"%(self.color,self.model,self.horse))
BMW_X9 = Car("绿色","1","100")
AUDI_A9 =Car("黄色","2","120")
print(BMW_X9)
print(AUDI_A9)
