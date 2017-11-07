# 定义一个电脑类,电脑有品牌,有价格,能放电影,能运行程序。
# 分别创建2个对象,修改其中一个放电影的名称,观察另一个类的变化。
class Computer:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def movie(self,name):
        print("正在运行[%s]"%name)
    def procedure(self,progrom):
        self.progrom = progrom
        self.movie(progrom)
    def __str__(self):
        return ("%s%s"%(self.price,self.brand))
lianxiang = Computer("联想","5000")
print(lianxiang)
lianxiang.movie("经济穿越")
lianxiang.procedure("sbjfegbuie")

