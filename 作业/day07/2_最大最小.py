#2.使用不定长参数定义一个函数max_min，接受的参数类型是数值，
# 最终返回这些数中的最大值和最小
"""
def max_min(*args):
    max = 0
    min = args[0]
    for n in args:
        if max<n:
             max = n
    for i in args:
        if i<=min:
            n = min
    print("最大值%s"%max)
    print("最小值%s" %min)
list = [6,4,326,653,3,78]
max_min(*list)
"""
#方法二
def max_min(*args):

    i = max(args)     #注意max是函数，注意不要写成args.max这不是内置的
    j = min(args)
    print("最大值%s"%i)
    print("最小值%s" %j)
list = [6,4,326,653,3,78]
max_min(*list)