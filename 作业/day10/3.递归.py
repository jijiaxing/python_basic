#练习 4. 定义函数  使用递归实现 n 的阶乘 ，
#  5 的阶乘 =  5 * 4 * 3 * 2 * 1  即 5 的阶乘 =  5 * 4的阶乘

def jiecheng(n):
    if n == 1:
        return 1
    return n*jiecheng(n-1)
print(jiecheng(5))