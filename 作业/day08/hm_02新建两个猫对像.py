class Cat:
    def eat(self):
        print("%s爱吃鱼"%self.name)
    def drink(self):
        print("%s要喝水"%self.name)
#-----------------
#注意：
# 有哪一个对象调用的方法，方法内部的self就是哪一个对象的引用
#-----------------
#创建猫对象
tom = Cat()
tom.name = "tom"
tom.eat()
tom.drink()
print(tom)

lazy_cat = Cat()
lazy_cat.name="大蓝猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

