# 练习 3.使用类属性、类方法、静态方法的知识实现以下功能：
# 		小明，小花，小刚，做游戏， 每个人都有一个分数(1 -- 100)，
# 		游戏开始前，显示，“游戏开始了，各位加油啊”
# 		游戏进行中打印每个人的游戏分数
# 		游戏结束后，打印最高分
#
# 		要求：类的声明在 test_01_class.py文件，代码运行在 另一个py文件 ,文件名:  test_01_run.py
import random
class Game:
    top_score = 0
    def __init__(self,name):
        self.name = name
        self.score = 0
    def is_score(self):
        self.score = random.randint(0,100)
        if self.score > Game.top_score:
            Game.top_score = self.score
    @staticmethod
    def start_game():
        print("游戏开始了，各位加油啊")
    @classmethod
    def is_top(cls):
        print("游戏最高分%s"%cls.top_score)
xiaoming = Game("小明")
xiaohua = Game("小花")
xiaomi = Game("小美")
xiaoming.is_score()
xiaohua.is_score()
xiaomi.is_score()
Game.start_game()
Game.is_top()