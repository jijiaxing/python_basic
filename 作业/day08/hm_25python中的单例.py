"""
单例：--让类创建的对象，在系统中只有只有唯一的一个实例
1.定义一个类属性，初始值是None,用于记录单例对象的引用
2.重写new方法
3.如果类属性是is None,调用父类的方法分配内存空间，并在类属性中记录结果
4.返回类属性中记录的对象的引用
"""

class MusicPlayer(object):
    #记录第一个被创建对象的引用
    instance = None
    def __new__(cls, *args, **kwargs):

        #1.判断类属性是否空
        if cls.instance is None:

        #2.调用父类的方法为第一个对象分配空间
            cls.instance = super().__new__(cls)
        #3.返回类属性保存的对象的引用
        return cls.instance

#创建多个对象
player1 =  MusicPlayer()
print(player1)

player2 =  MusicPlayer()
print(player2)