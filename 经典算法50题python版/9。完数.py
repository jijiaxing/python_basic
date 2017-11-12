# 题目：一个数如果恰好等于它的因子之和，这个数就称为 "完数 "。
# 例如6=1＋2＋3.编程   找出1000以内的所有完数。
list1=[]
def yinzi(n):
    list = []
    for i in range(1,n+1):
        if n%i == 0:
            list.append(i)
    sum = 0
    for j in list:
        sum += j
        if sum == n:
            return True
for num in range(1,1000):
    if yinzi(num):
       list1.append(num)
print(list1)

