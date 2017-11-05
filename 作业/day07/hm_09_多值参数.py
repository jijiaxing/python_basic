"""
定义支持多值参数的函数
    有时可能需要一个函数能够处理的参数个数是不确定的，这个时候
        可以使用多值参数
    Python中有两种多值参数：
        参数名前增加一个*可以接受元祖
        参数前面增加两个**可以接收字典
    一般给多值参数命名是，习惯使用以下两个名字
        *args----存放元组参数
        **kwargs----存放字典参数

"""
def demo(num,*args,**kwargs):
    print(num)
    print(args)
    print(kwargs)
demo(1,2,3,4,5,name="小明",age=18,gender=True)