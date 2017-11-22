import pygame
from plane_sprites import *
pygame.init()

#创建游戏窗口
screen = pygame.display.set_mode((480,700))
bg =  pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

#描述英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,300))
pygame.display.update()

#设置游戏时钟
clock = pygame.time.Clock()

#定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)



enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
enemy_group = pygame.sprite.Group(enemy,enemy1)

while True:
   clock.tick(60)
   #捕获事件
   for event in pygame.event.get():
       #判断事件类型是否是退出事件
       if event.type == pygame.QUIT:
           print("游戏推出。。。。")
           pygame.quit()
           exit()

   hero_rect.y -= 1
   if hero_rect.y <= -126:
       hero_rect.y = 700

   #调用blit方法绘制图像
   screen.blit(bg,(0,0))
   screen.blit(hero,hero_rect)
   enemy_group.update()
   enemy_group.draw(screen)
   pygame.display.update()


pygame.quit()