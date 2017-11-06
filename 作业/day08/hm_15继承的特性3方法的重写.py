"""
方法一
#如国父类的方法不能满足子类的需求时，可以方法进行重写
class Animal:

    def eat(self):
        print("吃---")
    def drink(self):
        print("喝---")
    def run(self):
        print("跑---")
    def sleep(self):
        print("睡---")
class Dog(Animal):
    #def eat(self):
    #    print("吃")
    #def drink(self):
     #   print("喝")
    #def run(self):
    #   print("跑")
    #def sleep(self):
     #   print("睡")

    def bark(self):
        print("叫")
class xiaotianquan(Dog):
    def fly(self):
        print("飞")
    def bark(self):
        print("叫得很嘹亮")

xtq = xiaotianquan()
#如果子类重写父lei的方法，调用子类中的方法而不是父类的
xtq.bark()
"""
class Animal:

    def eat(self):
        print("吃---")
    def drink(self):
        print("喝---")
    def run(self):
        print("跑---")
    def sleep(self):
        print("睡---")
class Dog(Animal):
    #def eat(self):
    #    print("吃")
    #def drink(self):
     #   print("喝")
    #def run(self):
    #   print("跑")
    #def sleep(self):
     #   print("睡")

    def bark(self):
        print("叫")
class xiaotianquan(Dog):
    def fly(self):
        print("飞")
    def bark(self):
        #1.针对子类特有需求编写代码
        print("叫得很嘹亮")
        #2.使用 super() 调用原本爸爸的方法
        super().bark()
        #也可以用父类名。方法(self)注意一定要用爸爸类，如果使用孝天犬类会出现递归调用，出现死循环
        #Dog.bark(self)不过在python3.0这种不是很推荐使用
        #3.增加其他子类的代码
        print("&&&&&&")

xtq = xiaotianquan()
#如果子类重写父lei的方法，调用子类中的方法而不是父类的
xtq.bark()