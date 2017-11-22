#一个整数，它加上100后是一个完全平方数，加上168又是一个完全平方数，
# 请问该数是多少？  
import math

for num in range(10000):

    a = math.sqrt(num + 100)
    b = math.sqrt(num + 100 + 168)
    if a // 1 == a and b // 1 == b:   #判断是不是整数
        print(num)

