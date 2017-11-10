 # 完成双色球案例：
	# 	红球：1个  1 -- 12 的随机数
	# 	蓝球：6个  1 -- 36 的随机数，要求不能重复
	# 	要求，6个蓝球用 2 种方法 实现：
	# 		方法 1- 每次获得随机数以后，判断之前的列表中是否有这个数，如果有就继续产生随机数，如果没有，就放入列表
	# 		方法 2- 模拟一个桶里有 36 个球的情况，随机拿出一个，桶里就少一个，拿出 6 次即获得 6个随机数
import random
red = random.randint(1,12)
blue_list1 = []
blue = []
for i in range(1,37):
     blue_list1.append(i)
 # n = 35
# for j in range(1,7):
#     blue_index  = random.randint(0,n)
#     blue.append(blue_list1[blue_index])
#     blue_list1.pop(blue_index)
#     n -= 1
# print(blue_list1)
# print(blue)

while True:
    bule__ball = random.randint(1,36)
    if bule__ball in blue:
        continue
    else:
        blue.append(bule__ball)
    if len(blue) == 6:
        break
blue.append(red)
print(blue)