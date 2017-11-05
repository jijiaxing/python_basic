#3.定义一个函数，返回n的阶乘的最后结果，并打印出如5阶乘"5! = 120"的效果
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(5))