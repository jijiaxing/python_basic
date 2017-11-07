# 7. 任意定义一个动物类
    # 使用__init__方法，在创建某个动物对象时，为其添加name、age、color,food等属性，
# 如“熊猫”，5,“黑白”，66，“竹子”
#     为动物类定义一个run方法，调用run方法时打印相关信息，如打印出“熊猫正在奔跑”
#     为动物类定义一个get_age方法，调用get_age方法时打印相关信息，如打印出“这只熊猫今年5岁了”
#     为动物类定义一个eat方法，调用eat方法时打印相关信息，如打印出“熊猫正在吃竹子”
#     通过动物类分别创建出3只不同种类的动物，分别调用它们的方法，让他们“跑起来”，“吃起来”
class Animal:
    def __init__(self,name,age,color,food):
        self.name=name
        self.age=age
        self.color=color
        self.food=food
    def run(self):
        print("[%s]正在奔跑"%self.name)
    def get_age(self):
        print("[%s]有[%s]了"%(self.name,self.age))
    def eat(self):
        print("[%s]正在吃[%s]"%(self.name,self.food))
xiongmao = Animal("熊猫","5","黑白","竹子")
xiongmao.run()
xiongmao.get_age()
xiongmao.eat()