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

class cat(Animal):
    def catch(self):
        print("抓老鼠")
xtq = xiaotianquan()
xtq.sleep()
xtq.bark()
xtq.fly()


#继承的传递性