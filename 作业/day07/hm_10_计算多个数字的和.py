"""
def sum_numbers(*args):
    num = 0
    for n in args:
        num += n
    return num
print(sum_numbers(1,2,41,14,58))
"""
# 元组和字典的拆包
# 在调用带有多值参数的函数时，如果希望：
#     将一个元组变量，直接传递给args
#     讲一个字典变量，直接传递给kwargs
# 就可以使用拆包，简化参数的传递。拆包的方式是：
#     在元组变量前面加一个*
#     在字典前面加两个**
def demo(*args,**kwargs):

    print(args)
    print(kwargs)
num =(1,2,3)
xiaoming ={"ame=":"小明","age":18}
demo(*num,**xiaoming)
