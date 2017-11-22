# . 生成 10 个 1 -- 100 的随机数 并存入列表 num_list，要求不能重复
# 		1- 完成以后对列表排序，获得最大值，和最小值
# 		第一种使用 sort 方法排序
# 		第二种，自己实现排序算法，步骤如下：
# 			1）从下标 0 开始遍历，将列表将最大值与 下标 0 的数值交换
# 			2）从下标 1 开始遍历，将除余数中的最大值与 下标 1 的值交换
# 			3）从下标 2 开始遍历，将除余数中的最大值 与下标 2 的值交换
# 			4) 如此类推，直止最后，将整个列表中所有的数，都按从大到小的序顺排列
# 			提示： 使用 双重 while 循环
import random
num_list = []

while True:
    num = random.randint(1, 100)
    if num in num_list:
        continue
    else:
        num_list.append(num)
    if len(num_list) == 10:
        break

# print(num_list)
# print(max(num_list))
# print(min(num_list))

i=0
while i < len(num_list):
    j=i
    while j<len(num_list):
        if num_list[i] < num_list[j]:
            temp = num_list[i]
            num_list[i]=num_list[j]
            num_list[j]=temp
        j+=1
    i+=1
print(num_list)
"""
方法二：
count_list = []
while True:
    count = 0
    for i in num_list:
        if i > count:
            count = i
    count_list.append(count)
    num_list.remove(count)
    if len(count_list) == 10:
        break
贺印 08:20:40
num_list = []
while True:
    num = random.randint(1, 100)
    if num in num_list:
        continue
    else:
        num_list.append(num)
    if len(num_list) == 10:
        break

print(num_list)

count_list = []
while True:
    count = 0
    for i in num_list:
        if i > count:
            count = i
    count_list.append(count)
    num_list.remove(count)
    if len(count_list) == 10:
        break

print(count_list)
print("最大值是%s" % count_list[0])
print("最小值是%s" % count_list[9])
"""
"""
import random
list = []
i = 0
while i < 10:
    x = random.randint(1, 100)
    if x not in list:
        list.append(x)
        i += 1
m = 0
while m < 10:
    for n in list[m+1: 10]:
        if n > list[m]:
            list[list.index(n)] = list[m]
            list[m] = n
    m += 1
print(list)
"""