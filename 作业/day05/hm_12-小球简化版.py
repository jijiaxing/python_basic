"""
练习 12 ： 有10个球分别3红、3蓝、4白，现需要将这10个球放入这3个盒子，要求每个盒子至少有一个白球，请用程序实现
提示，每个球都是一个字符串，如 "红1" "红2" "蓝1" "蓝2" ..
每个盒子都是一个列表，找盒子时用随机数

"""

import random

ball_list_1 = ["red1", "red2", "red3", "blue1", "blue2", "blue3"]
ball_list_2 = ["white1", "white2", "white3", "white4"]

box_1 = []
box_2 = []
box_3 = []

box_all = [box_1, box_2, box_3]
# 1- 先保存每个盒子里有一个白球，思路：随机拿一个白球，分别放入每个盒子

for box in box_all:
    random_index = random.randint(0, len(ball_list_2) - 1)  # 获得一个随机下标
    box.append(ball_list_2[random_index])
    # 将白球从盒子中删除
    ball_list_2.pop(random_index)

# 将省下的一个白球，放入　ball_list_1
ball_list_1.extend(ball_list_2)

# 遍历剩下的所有的球
for ball in ball_list_1:
    # 随机找个箱子
    box_indes = random.randint(0, 2)
    # 将球放入箱子
    box_all[box_indes].append(ball)


# 显示结果
for box in box_all:
    print(box)