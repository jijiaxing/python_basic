# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。  
# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：  
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。  
# (2)如果n <> k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你,重复执行第一步。  
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
"""
list1 =[]
def is_su_shu(n):
    chu_shu = 2
    while chu_shu < n:
        if n % chu_shu == 0:
            return False
        chu_shu += 1
    return True
def zhishu(n):
    if is_su_shu(n):
        return list1.append(n)
    i=2
    while i<n:
        if n % i==0:
            list1.append(i)
            break
        i += 1
    zhishu(int(n/i))
    print(list1)
zhishu(45)
"""
import math
print("请输入一个正整数：")
n = int(input())
if n <= 0:
    print("请输入正整数")
i=2
if n!=1:
    while i!=n:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i+=1
    print(i)
else:
    print(n)

