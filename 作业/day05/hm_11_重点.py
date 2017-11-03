# 有10个球分别3红、3蓝、4白，现需要将这10个球放入这3个盒子，要求每个盒子至少有一个白球，请用程序实现
#提示，每个球都是一个字符串，如"红1" "红2" "蓝1" "蓝2"..每个盒子都是一个列表，找盒子时用随机数
import random
box1=[]
box2=[]
box3=[]
boxlist = [box1,box2,box3]
ball1=["red1","red2","red3","blue1","blue2","blue3"]
ball2=["white1","white2","white3","white4"]
#放置白球
num=random.randint(0,3)
box1.append(ball2[num])
ball2.pop(num)
num2=random.randint(0,2)
box2.append(ball2[num2])
ball2.pop(num2)
num3=random.randint(0,1)
box3.append(ball2[num3])
ball2.pop(num3)
box_num =random.randint(0,2)
boxlist[box_num].extend(ball2)
#放置其他球
#ball1=["red1","red2","red3","blue1","blue2","blue3"]
while len(ball1)>0:
    baii_random=random.randint(0,len(ball1)-1)
    box_random = random.randint(0, 2)
    boxlist[box_random].append(ball1[baii_random])
    ball1.remove(ball1[baii_random])
print(box1)
print(box2)
print(box3)