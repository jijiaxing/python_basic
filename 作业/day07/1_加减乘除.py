# 分别定义加减乘除四个函数，然后实现多个数之间的累加累减累除累乘操作，
# 如[1,2,3,4,5]，累加即是1+2+3+4+5，注意当使用除法时，应判断被除数不能为0
def plus(*args):
    sum  = 0
    for n in args:
        sum += n
    print(sum)
def minux(*args):
    sum = 2
    for n in args:
        sum -= n
    print(sum)
def multiply(*args):
    sum = 1
    for n in args:
        sum *= n
    print(sum)
def divide(*args):
    sum = 1
    while sum!=0:
        for n in args:
            sum /= n
    print(sum)
list = [1,2,3,4,5]
plus(*list)
minux(*list)
multiply(*list)
divide(*list)
