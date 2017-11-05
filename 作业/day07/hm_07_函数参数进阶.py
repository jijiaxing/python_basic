
# 问题一：在函数内部，针对参数使用赋值语句，会不会影响
# 调用函数时传递的实际参数变量？----不会！！
# 1无论传递的参数是可变的还是不可变
#     只要针对参数使用赋值语句，会在函数内部修改局部变量的引用，
#         不会影响到外部变量的引用
"""
def demo(num,num_list):
    print("函数内部")
    #赋值语句
    num = 200
    num_list = [1,2,3]
    print(num)
    print(num_list)
    print("函数代码按成")
gl_num = 99
gl_list = [4,5,6]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)
"""
#问题二：如果传递的参数是可变类型，在函数内部。
    # 使用方法修改了数据的内容，同样会影响到外部的数据
"""
def mutable(num_list):
    #num_list = [1,2,3]
    num_list.extend([1,2,3])
    print(num_list)

gl_list=[6,7,8]
mutable(gl_list)
print(gl_list)
"""
#在python中，列表变量调用+=本质上是在执行列表变量的extend
#方法，不会修改变量的引用
def demo(num,num_list):
    print("函数内部代码")
    num += num
    #num_list.extend(num_list)由于是调用方法，不会修改变量的引用
    #函数执行结束后，外部数据同样也会发生变化
    num_list += num_list
    print(num)
    print(num_list)
    print("函数代码完成")
gl_num = 9
gl_list = [1,2,3]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)