"""
多态：不同的子类对象调用相同的父类方法，产生不同的执行结果
1.多态可以增加代码的灵活度
2.以继承和重写为前提
3.是调用方法的技巧，不影响类内部的设计
"""
class Dog(object):

    def __init__(self,name):
        self.name=name
    def game(self):
        print("%s蹦蹦天天"%self.name)

class Xiaotianquan(Dog):
    def game(self):
        print("%s升天万"%self.name)
class Person(object):

    def __init__(self,name):
        self.name=name
    def game_with_dog(self,dog):
        print("%s和%s快乐的玩耍"%(self.name,dog.name))

    #让狗玩耍
        dog.game()

#wangcai = Dog("旺财")
wangcai=Xiaotianquan("飞天旺财")
xiaoming = Person("小明")
xiaoming.game_with_dog(wangcai)