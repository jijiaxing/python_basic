"""
1.设计一个游戏类
2.属性：
    类属性 top_score 记录游戏历史最高分
    实例属性 player_name 记录玩家姓名
3.方法：
    静态方法 show_help 现实游戏帮助信息
    类方法 show_top_score  现实历史最高分
    实例方法start_game 开始游戏
4.主程序步骤
    1.查看帮助信息
    2.查看历史最高分
    3.创建游戏对象，开始当前玩家游戏
5.实例方法--方法内部需要访问实例属性
        实例方法内部可以使用类名. 访问类属性
6.类方法--方法内部只需要访问类属性
7.静态方法--不需要访问实力属性和类属性
"""
class Game(object):

    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name
    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")


    @classmethod
    def show_top_score(cls):
        print("历史记录路%d"%cls.top_score)

    def start_game(self):  #实例方法
        print("%s开始游戏了"%self.player_name)

Game.show_help()
Game.show_top_score()

game = Game("小明")
game.start_game()