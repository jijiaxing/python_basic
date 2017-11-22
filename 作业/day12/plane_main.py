import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")


    def __create_sprites(self):


    def start_game(self):
        print("游戏开始...")

        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()


    @staticmethod
    def __game_over():
        print("游戏结束")

        pygame.quit()
        exit()

if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
