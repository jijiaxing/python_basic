#练习 9 : 使用循环 手工输入 5 个整数，并将其存入列表，使用二种方法求出最大值，和最小值。
#			提示：方法1 使用 sort ，方法2 自己写算法
i = 0
list=[]
max=0
while i<5:
    num = int(input("请输入数字："))
    list.append(num)
    i+=1
"""
list.sort()
#print(list)
print(list[0])
print(list[4])
"""
i=0
while i < 5:
    if max < list[i]:
        max = list[i]


    i+=1
print(max)



