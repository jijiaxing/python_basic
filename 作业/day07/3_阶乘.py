#3.定义一个函数，返回n的阶乘的最后结果，并打印出如5阶乘"5! = 120"的效果
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
# 方法一　使用递归
def jiechen(n):
    if n == 1:
        return 1
    num = jiechen(n - 1)
    return n * num
# 方法二　
def jiechen2(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result
n = 6
# a = jiechen(n)
a = jiechen2(n)
print("%d! = %d" % (n, a))
