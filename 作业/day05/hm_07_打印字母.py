#从键盘获取5个学生的名字，然后随机抽出一名学生去打扫卫生
import random
list = []
i=0
while i<5:

     name = input("请输入姓名;")
     list.append(name)
     i+=1
swepp = int(random.randint(0,4))
print("打扫%s"%list[swepp])

